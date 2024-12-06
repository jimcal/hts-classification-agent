# HTS Classification Decision Tree for Footwear (Chapter 64)
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
