# hts-classification-agent
AI Agent for HTS code. Starting with Footwear.

# HTS Classification AI Agent

## Project Overview
An AI-powered system for automatically determining Harmonized Tariff Schedule (HTS) codes for footwear products, with a specific focus on US imports. The system combines product information analysis, computer vision for material composition determination, and expert classification rules.

## Repository Structure
```
hts-classification-agent/
├── docs/
│   ├── decision_trees/
│   │   └── footwear_classification.md    # Classification decision tree documentation
│   ├── image_requirements.md             # Image capture specifications
│   └── api_documentation.md              # API specifications (future)
├── src/
│   ├── material_analysis/
│   │   ├── confidence_scoring.py         # Confidence calculation system
│   │   ├── image_analyzer.py             # Image processing and analysis
│   │   └── material_reconciliation.py    # Multi-angle analysis reconciliation
│   ├── classification/
│   │   ├── decision_engine.py            # HTS classification logic
│   │   └── product_resolver.py           # Product information resolution
│   └── api/                              # Future API implementation
├── tests/
│   └── material_analysis/
└── README.md
```

## Development Timeline

### Phase 1: Initial Architecture and Core Components
1. Problem Definition:
   - Current manual process requires cross-referencing multiple data sources
   - Need for automated classification based on product attributes
   - Focus on Chapter 64 (Footwear) for initial implementation

2. Core Decision Tree Development:
   ```mermaid
   graph TD
    A[Start: Footwear Classification] --> B{Is it waterproof?}
    B -->|Yes| C{Made of rubber/plastic?}
    B -->|No| D{What is primary upper material?}
    
    C -->|Yes| E[6401: Waterproof rubber/plastic]
    C -->|No| F[Check other chapters]
    
    D -->|Rubber/Plastic| G{Sports or casual?}
    D -->|Leather| H{Coverage type?}
    D -->|Textile| I{Primary purpose?}
    D -->|Other| J[6405: Other footwear]
    
    G -->|Sports| K[6402.19: Sports footwear]
    G -->|Casual| L[6402.99: Other footwear]
    
    H -->|Covers ankle| M[6403.51: Covers ankle]
    H -->|Below ankle| N[6403.59: Below ankle]
    
    I -->|Sports| O[6404.11: Sports footwear]
    I -->|Other| P[6404.19: Other footwear]
    
    %% Notes for material composition
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#f9f,stroke:#333,stroke-width:2px
    
    %% Critical decision points
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
   ```

3. Material Analysis System:
   - Image requirements specification
   - Confidence scoring system
   - Multi-angle reconciliation logic

### Phase 2: User Interface and Integration
1. Simple text input interface for:
   - GTIN
   - Style ID
   - Product name

2. Image Analysis Interface:
   - Multiple angle upload capability
   - Real-time feedback
   - Material composition visualization

### Future Phases:
1. Batch Processing:
   - CSV file upload
   - Bulk classification
   - Export functionality

2. API Development:
   - RESTful endpoints
   - Authentication
   - Usage monitoring

## Key Technical Components

### 1. Image Analysis System
```python
# Material Analysis Code [Previously Discussed]
class FootwearMaterialAnalyzer:
    [Previous implementation details]
```

### 2. Confidence Scoring
```python /src/material_analysis/confidence_scoring.py
# Confidence Scoring System [Previously Discussed]
class ConfidenceScorer:
```

### 3. Material Reconciliation
```python src/material_analysis/material_reconciliation.py
# Multi-Angle Reconciliation System [Previously Discussed]
class MaterialReconciliation:
```

## Design Decisions and Rationale

### Material Analysis Approach
1. Multiple Angle Requirement:
   - Ensures accurate material composition assessment
   - Reduces errors from occlusion or lighting issues
   - Enables cross-validation of material detection

2. Confidence Scoring:
   - Weighted evaluation of multiple factors
   - Clear threshold requirements
   - Detailed feedback for improvement

3. Material Reconciliation:
   - Hierarchical conflict resolution
   - Material-specific verification rules
   - Weighted angle importance

## Testing Strategy

1. Unit Tests:
   - Individual component validation
   - Edge case handling
   - Error conditions

2. Integration Tests:
   - Multi-component workflows
   - End-to-end classification scenarios

3. Validation Tests:
   - Known product verification
   - Classification accuracy metrics
   - Performance benchmarks

## Next Steps

1. Technical Implementation:
   - Complete core analysis components
   - Develop testing framework
   - Implement basic UI

2. Data Collection:
   - Build reference image database
   - Compile classification examples
   - Document edge cases

3. System Integration:
   - Connect components
   - Implement feedback loops
   - Develop monitoring system

## Contributing
[Standard contribution guidelines to be added]

## License
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.