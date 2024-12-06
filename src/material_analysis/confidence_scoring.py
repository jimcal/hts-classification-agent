class ConfidenceScorer:
    def __init__(self):
        # Define weight factors for different confidence components
        self.weights = {
            'image_quality': 0.25,
            'material_detection': 0.35,
            'angle_coverage': 0.20,
            'consistency': 0.20
        }
        
        # Define minimum thresholds for acceptable confidence
        self.thresholds = {
            'minimum_overall': 0.70,
            'minimum_per_component': 0.50
        }

    def score_image_quality(self, image_metadata):
        """
        Evaluates technical quality of submitted images
        Returns score between 0-1
        """
        quality_scores = {
            'resolution': self._check_resolution(image_metadata['resolution']),
            'lighting': self._analyze_lighting(image_metadata['histogram']),
            'focus': self._measure_sharpness(image_metadata['frequency_analysis']),
            'contrast': self._evaluate_contrast(image_metadata['histogram'])
        }
        
        return sum(quality_scores.values()) / len(quality_scores)

    def score_material_detection(self, material_analysis):
        """
        Evaluates confidence in material type detection
        """
        confidence_factors = {
            'texture_clarity': self._evaluate_texture_confidence(material_analysis),
            'boundary_definition': self._evaluate_boundaries(material_analysis),
            'material_consistency': self._check_material_patterns(material_analysis),
            'reference_matching': self._compare_to_reference_database(material_analysis)
        }
        
        return sum(confidence_factors.values()) / len(confidence_factors)

    def score_angle_coverage(self, submitted_angles):
        """
        Evaluates completeness of angle coverage
        """
        required_angles = {'lateral', 'medial', 'top'}
        optional_angles = {'back', '45_degree'}
        
        # Base score on required angles
        base_score = len(submitted_angles & required_angles) / len(required_angles)
        
        # Bonus for optional angles (up to 20% boost)
        bonus = min(0.2, len(submitted_angles & optional_angles) * 0.1)
        
        return min(1.0, base_score + bonus)

    def score_cross_angle_consistency(self, material_analyses):
        """
        Evaluates consistency of material detection across different angles
        """
        material_percentages = []
        for analysis in material_analyses:
            material_percentages.append(analysis['material_composition'])
            
        # Calculate variance in material percentages across angles
        variance = self._calculate_composition_variance(material_percentages)
        
        # Convert variance to confidence score (lower variance = higher confidence)
        return max(0, 1 - (variance * 2))

    def calculate_overall_confidence(self, analysis_results):
        """
        Calculates final weighted confidence score
        """
        scores = {
            'image_quality': self.score_image_quality(analysis_results['image_metadata']),
            'material_detection': self.score_material_detection(analysis_results['material_analysis']),
            'angle_coverage': self.score_angle_coverage(analysis_results['submitted_angles']),
            'consistency': self.score_cross_angle_consistency(analysis_results['angle_analyses'])
        }
        
        # Calculate weighted average
        overall_confidence = sum(
            scores[component] * self.weights[component]
            for component in self.weights
        )
        
        # Check minimum thresholds
        if overall_confidence < self.thresholds['minimum_overall']:
            return {
                'confidence': overall_confidence,
                'status': 'INSUFFICIENT_CONFIDENCE',
                'recommendations': self._generate_improvement_recommendations(scores)
            }
            
        if any(score < self.thresholds['minimum_per_component'] for score in scores.values()):
            return {
                'confidence': overall_confidence,
                'status': 'PARTIAL_CONFIDENCE',
                'weak_components': self._identify_weak_components(scores),
                'recommendations': self._generate_improvement_recommendations(scores)
            }
            
        return {
            'confidence': overall_confidence,
            'status': 'ADEQUATE_CONFIDENCE',
            'component_scores': scores
        }
