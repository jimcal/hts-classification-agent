interface Product {
  identifier: string;  // GTIN or style ID
  name?: string;
  attributes: {
    primaryMaterial?: string;
    constructionMethod?: string;
    coverage?: 'low' | 'mid' | 'high';
    demographic?: 'men' | 'women' | 'children';
    purpose?: string;
    [key: string]: any;  // Allow for additional attributes
  };
}

interface ProductQuery {
  identifier: string;
  knownAttributes?: Partial<Product['attributes']>;
}

export { Product, ProductQuery }; 