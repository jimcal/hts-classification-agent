interface ClassificationResult {
  htsCode: string;
  confidence: number;
  explanation: string;
  missingAttributes?: string[];
  alternativeCodes?: Array<{
    code: string;
    condition: string;
  }>;
}

export { ClassificationResult }; 