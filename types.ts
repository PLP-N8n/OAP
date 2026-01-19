export interface AdjudicationResult {
  verdict: 'VIOLATION' | 'NO_VIOLATION';
  citation: string | null;
  reasoning: string;
}

export interface DemoState {
  rulebook: string;
  content: string;
  isLoading: boolean;
  result: AdjudicationResult | null;
  error: string | null;
}