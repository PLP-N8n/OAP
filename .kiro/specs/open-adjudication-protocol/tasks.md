# Implementation Tasks: Open Adjudication Protocol MVP

## "Sale-Ready" Plan - 3 Steps to Prove Core Value

This MVP focuses on proving the core Citation Anchoring innovation with minimal complexity. No databases, no APIs, no complex ML - just scripts that demonstrate the "Safety Gate" concept.

## Step 1: The "Normalizer" Script (Python)

**Goal**: Prove you can turn messy text into structured rules
**Validates**: Requirements 3.1, 3.2, 3.3 (Rule ingestion and parsing)

### 1.1 Rule Text Normalization
- [x] 1.1 Create Python script `normalizer.py` that accepts text input
- [x] 1.2 Implement text parsing to identify discrete rule clauses
- [x] 1.3 Extract individual rules from paragraph text using NLP techniques
- [x] 1.4 Assign unique identifiers to each extracted rule clause
- [x] 1.5 Output structured JSON format with rule clauses

**Input Example**: 
```
"No harassment or bullying. Users must not post content that targets individuals with hate speech. Spam and promotional content is prohibited. All posts must be relevant to the community topic."
```

**Output Example**:
```json
{
  "rules": [
    {
      "id": "rule_001",
      "text": "No harassment or bullying",
      "category": "conduct",
      "keywords": ["harassment", "bullying"]
    },
    {
      "id": "rule_002", 
      "text": "Users must not post content that targets individuals with hate speech",
      "category": "hate_speech",
      "keywords": ["hate speech", "targeting", "individuals"]
    },
    {
      "id": "rule_003",
      "text": "Spam and promotional content is prohibited", 
      "category": "spam",
      "keywords": ["spam", "promotional", "prohibited"]
    },
    {
      "id": "rule_004",
      "text": "All posts must be relevant to the community topic",
      "category": "relevance", 
      "keywords": ["relevant", "community", "topic"]
    }
  ]
}
```

### 1.2 Testing for Step 1
- [x] 1.6 Write unit tests for rule extraction accuracy
- [x] 1.7 Write property test for rule ingestion determinism
- [x] 1.8 Test with various rule formats (Reddit rules, Discord guidelines, etc.)
- [x] 1.9 Validate JSON output structure consistency

## Step 2: The "Citation" Script (The Core IP)

**Goal**: Prove the "Safety Gate" works - every violation must cite a specific rule
**Validates**: Requirements 2.1, 2.2, 2.3 (Citation Anchoring System)

### 2.1 Citation Anchoring Engine
- [x] 2.1 Create Python script `citation_checker.py` that takes user comment + rules JSON
- [x] 2.2 Implement exact text matching between comment and rule violations
- [x] 2.3 Implement semantic similarity matching for rule violations
- [x] 2.4 Create citation confidence scoring (0-1 scale)
- [x] 2.5 Flag statements that cannot be anchored to any rule

### 2.2 Violation Detection Logic
- [x] 2.6 Analyze user comment for potential rule violations
- [x] 2.7 Match violations to specific rule clauses from Step 1 output
- [x] 2.8 Generate violation report with exact rule citations
- [x] 2.9 Implement "No Violation" output when no rules are matched
- [x] 2.10 Ensure every violation statement includes rule quote

**Input Example**:
```python
# User comment
comment = "This stupid moderator is clearly biased against conservatives. What a joke!"

# Rules from Step 1
rules_json = {...} # Output from normalizer.py
```

**Output Examples**:
```
# Violation found
"Violation: 'This stupid moderator is clearly biased' violates Rule 001: 'No harassment or bullying'"

# No violation found  
"No Violation (No Quote Found)"
```

### 2.3 Testing for Step 2
- [x] 2.11 Write property test for citation anchoring completeness
- [x] 2.12 Write property test for citation text accuracy
- [x] 2.13 Test edge cases (borderline violations, ambiguous content)
- [x] 2.14 Validate that unsupported statements are flagged
- [x] 2.15 Test with real-world comment examples

## Step 3: The "Demo" Interface (Streamlit)

**Goal**: Make it look professional for potential buyers
**Validates**: Requirements 4.1, 4.4 (Transparent output generation)

### 3.1 Streamlit Web Interface
- [x] 3.1 Create Streamlit app `demo_app.py` with clean UI
- [x] 3.2 Build input form for pasting rule text (Step 1 input)
- [x] 3.3 Display normalized rules output in formatted JSON
- [x] 3.4 Create input form for user comment (Step 2 input)
- [x] 3.5 Display violation analysis with highlighted citations

### 3.2 Demo User Experience
- [x] 3.6 Add example rule sets (Reddit, Discord, Twitter guidelines)
- [x] 3.7 Include sample problematic comments for testing
- [x] 3.8 Create clear before/after comparison showing citation anchoring
- [x] 3.9 Add explanation text about the "Safety Gate" concept
- [x] 3.10 Style interface professionally for sales presentations

### 3.3 Demo Features
- [x] 3.11 Real-time processing (paste rules → see normalized output)
- [x] 3.12 Interactive violation checking (paste comment → see analysis)
- [x] 3.13 Export functionality for rules JSON and violation reports
- [x] 3.14 Clear visual indicators for violations vs. no violations
- [x] 3.15 Mobile-responsive design for demos on tablets/phones

### 3.4 Testing for Step 3
- [x] 3.16 Test UI with various screen sizes and devices
- [x] 3.17 Validate end-to-end workflow (rules → normalization → citation)
- [x] 3.18 Test with real community guidelines from major platforms
- [x] 3.19 Ensure error handling for malformed inputs
- [x] 3.20 Performance testing with large rule sets

## Technical Implementation Notes

### Dependencies
- **Python 3.8+** for core scripts
- **spaCy or NLTK** for natural language processing
- **scikit-learn** for semantic similarity matching
- **Streamlit** for web interface
- **pytest** for testing framework

### File Structure
```
oap-mvp/
├── normalizer.py          # Step 1: Rule normalization
├── citation_checker.py    # Step 2: Citation anchoring  
├── demo_app.py           # Step 3: Streamlit interface
├── tests/
│   ├── test_normalizer.py
│   ├── test_citation.py
│   └── test_integration.py
├── examples/
│   ├── reddit_rules.txt
│   ├── discord_rules.txt
│   └── sample_comments.txt
└── requirements.txt
```

### Success Criteria
1. **Step 1**: Can parse any community guidelines text into structured JSON rules
2. **Step 2**: Every violation detection includes exact rule citation or returns "No Violation"
3. **Step 3**: Professional demo interface that clearly shows the value proposition

### Timeline
- **Week 1**: Step 1 (Normalizer script + tests)
- **Week 2**: Step 2 (Citation checker + tests)  
- **Week 3**: Step 3 (Streamlit demo + integration)
- **Week 4**: Polish, real-world testing, sales preparation

This MVP proves the core Citation Anchoring concept without the complexity of databases, APIs, or multi-tenant architecture. Once this demonstrates market fit, the full system from the design document can be built incrementally.
