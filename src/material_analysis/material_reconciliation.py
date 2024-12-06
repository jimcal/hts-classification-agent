class MaterialReconciliation:
    def __init__(self):
        self.angle_weights = {
            'lateral': 0.35,    # Side view shows largest surface area
            'medial': 0.35,     # Inner side equally important
            'top': 0.20,        # Top view shows additional materials
            'back': 0.10        # Heel construction verification
        }
        
        # Define material priority rules for conflict resolution
        self.material_hierarchy = {
            'leather': {
                'priority': 1,
                'common_confusions': ['synthetic_leather', 'suede'],
                'verification_rules': self._leather_verification_rules()
            },
            'textile': {
                'priority': 2,
                'common_confusions': ['mesh', 'knit'],
                'verification_rules': self._textile_verification_rules()
            },
            'synthetic': {
                'priority': 3,
                'common_confusions': ['leather', 'textile'],
                'verification_rules': self._synthetic_verification_rules()
            }
        }

    def reconcile_analyses(self, angle_analyses):
        """
        Combines material analyses from multiple angles into a single coherent result
        """
        # First pass: Weighted average of material percentages
        initial_composition = self._calculate_weighted_composition(angle_analyses)
        
        # Detect and resolve conflicts
        conflicts = self._identify_material_conflicts(angle_analyses)
        if conflicts:
            resolved_composition = self._resolve_conflicts(
                initial_composition, 
                conflicts, 
                angle_analyses
            )
        else:
            resolved_composition = initial_composition
        
        # Validate against material rules
        validated_composition = self._validate_material_rules(resolved_composition)
        
        # Generate confidence metrics
        confidence_metrics = self._calculate_reconciliation_confidence(
            initial_composition,
            resolved_composition,
            validated_composition,
            conflicts
        )
        
        return {
            'material_composition': validated_composition,
            'confidence_metrics': confidence_metrics,
            'resolution_notes': self._generate_resolution_notes(conflicts)
        }

    def _calculate_weighted_composition(self, angle_analyses):
        """
        Calculates weighted average of material percentages across angles
        """
        weighted_composition = {}
        total_weight = sum(
            self.angle_weights[analysis['angle']]
            for analysis in angle_analyses
            if analysis['angle'] in self.angle_weights
        )
        
        for material in self._get_all_materials(angle_analyses):
            weighted_sum = sum(
                analysis['composition'].get(material, 0) * 
                self.angle_weights.get(analysis['angle'], 0)
                for analysis in angle_analyses
            )
            weighted_composition[material] = weighted_sum / total_weight
            
        return weighted_composition

    def _identify_material_conflicts(self, angle_analyses):
        """
        Identifies areas where material detection differs significantly between angles
        """
        conflicts = []
        materials = self._get_all_materials(angle_analyses)
        
        for material in materials:
            percentages = [
                analysis['composition'].get(material, 0)
                for analysis in angle_analyses
            ]
            
            if max(percentages) - min(percentages) > 0.15:  # 15% threshold
                conflicts.append({
                    'material': material,
                    'variation_range': max(percentages) - min(percentages),
                    'angles': self._identify_conflicting_angles(
                        material, 
                        angle_analyses
                    )
                })
                
        return conflicts

    def _resolve_conflicts(self, composition, conflicts, angle_analyses):
        """
        Resolves material conflicts using material hierarchy and verification rules
        """
        resolved_composition = composition.copy()
        
        for conflict in conflicts:
            material = conflict['material']
            
            # Apply material-specific verification rules
            if material in self.material_hierarchy:
                rules = self.material_hierarchy[material]['verification_rules']
                verification_result = rules(angle_analyses, conflict)
                
                if verification_result['verified']:
                    resolved_composition[material] = verification_result['percentage']
                else:
                    # Fall back to alternative material if verification fails
                    alternative = verification_result['alternative_material']
                    resolved_composition[alternative] = (
                        resolved_composition.get(alternative, 0) + 
                        resolved_composition[material]
                    )
                    resolved_composition.pop(material)
                    
        return self._normalize_percentages(resolved_composition)

    def _validate_material_rules(self, composition):
        """
        Validates and adjusts composition to meet material classification rules
        """
        validated = composition.copy()
        
        # Rule 1: Primary material must be at least 50%
        primary_material = max(validated.items(), key=lambda x: x[1])[0]
        if validated[primary_material] < 0.5:
            # Adjust compositions to ensure primary material exceeds 50%
            shortfall = 0.5 - validated[primary_material]
            validated[primary_material] = 0.5
            
            # Proportionally reduce other materials
            total_others = sum(v for k, v in validated.items() if k != primary_material)
            if total_others > 0:
                reduction_factor = (1 - 0.5) / total_others
                for material in validated:
                    if material != primary_material:
                        validated[material] *= reduction_factor
                        
        return validated

    def _calculate_reconciliation_confidence(self, initial, resolved, validated, conflicts):
        """
        Calculates confidence metrics for the reconciliation process
        """
        metrics = {
            'initial_confidence': self._calculate_initial_confidence(initial),
            'resolution_confidence': self._calculate_resolution_confidence(conflicts),
            'validation_confidence': self._calculate_validation_confidence(
                resolved, 
                validated
            )
        }
        
        # Overall confidence is the weighted average of component confidences
        metrics['overall_confidence'] = sum(metrics.values()) / len(metrics)
        
        return metrics
