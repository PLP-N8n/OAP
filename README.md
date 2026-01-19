# Open Adjudication Protocol - MVP Demo

## 🎯 The Innovation: Citation Anchoring

The Open Adjudication Protocol solves AI moderation hallucination through **Citation Anchoring** - every violation decision must quote an exact rule from the community guidelines.

### The Problem
- AI moderation systems make up violations that don't exist in the rules
- Decisions are opaque and legally indefensible
- No traceability between violations and actual policy text

### The Solution
- **Step 1**: Normalize messy community guidelines into structured rules
- **Step 2**: Require every violation to cite a specific rule clause
- **Step 3**: Professional demo interface for sales presentations

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. **Clone and setup:**
```bash
git clone <repository>
cd open-adjudication-protocol-mvp
pip install -r requirements.txt
```

2. **Configure OpenAI API:**
```bash
# Option 1: Set environment variable
export OPENAI_API_KEY="your-api-key-here"

# Option 2: Edit normalizer.py directly
# Replace "YOUR_OPENAI_API_KEY_HERE" with your actual key
```

### Usage

#### Command Line Demo
```bash
python normalizer.py
```

#### Citation Checker (Step 2)
```bash
python citation_checker.py --rules-text "No harassment. No spam." --comment "This is spam."
```

#### Web Interface Demo
```bash
streamlit run demo_app.py
```

#### Run Tests
```bash
python test_normalizer.py
```

## 📁 File Structure

```
oap-mvp/
├── normalizer.py          # Core citation anchoring engine
├── citation_checker.py    # Step 2: Citation anchoring checker
├── demo_app.py           # Streamlit web interface
├── test_normalizer.py    # Test suite
├── requirements.txt      # Python dependencies
├── examples/
│   ├── reddit_rules.txt  # Sample community guidelines
│   ├── discord_rules.txt  # Sample Discord guidelines
│   ├── twitter_rules.txt  # Sample Twitter/X guidelines
│   └── sample_comments.txt # Test comments
└── README.md
```

## 🔧 How It Works

### Step 1: Rule Normalization
Takes messy community guidelines and converts them to structured JSON:

**Input:**
```
"No harassment or bullying. Spam is prohibited. Be respectful."
```

**Output:**
```json
{
  "rules": [
    {"id": "1.0", "text": "No harassment or bullying", "category": "conduct"},
    {"id": "2.0", "text": "Spam is prohibited", "category": "spam"},
    {"id": "3.0", "text": "Be respectful", "category": "conduct"}
  ]
}
```

### Step 2: Citation Anchoring
Analyzes user comments and requires exact rule citations for violations:

**Input:**
```
Comment: "You're such an idiot!"
Rules: [normalized rules from Step 1]
```

**Output:**
```json
{
  "verdict": "Violation",
  "citation_anchor": {
    "rule_id": "1.0",
    "quoted_rule_text": "No harassment or bullying"
  },
  "reasoning": "The comment contains harassment...",
  "confidence": 0.95
}
```

### Step 3: Demo Interface
Professional Streamlit interface showing:
- Real-time rule normalization
- Interactive violation checking
- Clear citation anchoring display
- Multiple example rule sets and comments

## 🧪 Testing

The MVP includes comprehensive testing:

- **Rule Normalization Tests**: Verify structured output format
- **Citation Anchoring Tests**: Ensure violations cite specific rules
- **Citation Completeness Tests**: Validate all violations have proper citations

Run tests with:
```bash
python test_normalizer.py
```

## 🎬 Demo Script

For sales presentations:

1. **Show the Problem**: 
   - "Current AI moderation makes up violations"
   - "No traceability to actual rules"

2. **Demonstrate Step 1**:
   - Paste messy community guidelines
   - Show clean, structured rule output

3. **Demonstrate Step 2**:
   - Test clear violation → shows exact rule citation
   - Test borderline case → shows "No Violation" 
   - Test edge case → demonstrates precision

4. **The Value Proposition**:
   - "Every decision is legally defensible"
   - "Complete transparency and auditability"
   - "No AI hallucination or made-up violations"

## 🔑 Key Features

### ✅ Citation Anchoring (The Core IP)
- Every violation must quote an exact rule
- No hallucination or made-up violations
- Legally defensible decisions

### ✅ Rule Normalization
- Converts any text format to structured rules
- Handles messy, informal community guidelines
- Maintains original meaning while adding structure

### ✅ Professional Demo Interface
- Clean, intuitive web interface
- Real-time processing
- Multiple example scenarios
- Mobile-responsive design

### ✅ Comprehensive Testing
- Unit tests for core functionality
- Property-based testing concepts
- Real-world example validation

## 🎯 Success Metrics

This MVP proves:
1. **Technical Feasibility**: Can normalize any rule text format
2. **Core Innovation**: Citation anchoring prevents AI hallucination
3. **Market Readiness**: Professional interface for buyer demonstrations
4. **Legal Defensibility**: Every decision traces to specific rule text

## 🚀 Next Steps

After MVP validation:
1. **Database Integration**: Store rules and decisions
2. **API Development**: RESTful endpoints for platform integration
3. **Multi-tenant Architecture**: Support multiple client platforms
4. **Advanced ML**: Semantic matching and confidence scoring
5. **Compliance Features**: DSA Article 17 compliance automation

## 📞 Sales Positioning

**For Investors/Buyers:**
- "We solve the $X billion AI moderation hallucination problem"
- "Every decision is legally defensible with exact rule citations"
- "Ready for DSA compliance and regulatory requirements"
- "Proven technology with working demo"

**Technical Differentiators:**
- Citation anchoring prevents AI hallucination
- Works with any existing community guidelines
- No complex setup or rule rewriting required
- Transparent, auditable decision process

---

**Open Adjudication Protocol** - Making AI moderation transparent, defensible, and trustworthy.
