import json
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

# Try to import spaCy for NLP-based parsing (Task 1.3)
try:
    import spacy
    SPACY_AVAILABLE = True
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        # Model not downloaded yet
        SPACY_AVAILABLE = False
        nlp = None
except ImportError:
    SPACY_AVAILABLE = False
    nlp = None

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY_HERE")
client = OpenAI(api_key=api_key)

# ---------------------------------------------------------
# MODULE 1: THE RULEBOOK NORMALIZER
# (Turns messy text into a rigid, numbered list)
# ---------------------------------------------------------

def parse_rule_clauses(raw_text):
    """
    Task 1.2 & 1.3: Implement text parsing to identify discrete rule clauses
    Enhanced with NLP techniques for better extraction
    
    This function takes raw text and identifies discrete rule clauses using
    pattern matching, text analysis, and NLP techniques (when available).
    
    Args:
        raw_text (str): Raw community guidelines or rules text
        
    Returns:
        list: List of identified rule clause strings
    """
    if not raw_text or not raw_text.strip():
        return []
    
    # Normalize whitespace and line breaks
    text = raw_text.strip()
    
    # Task 1.3: Use NLP techniques if spaCy is available
    if SPACY_AVAILABLE and nlp is not None:
        return _parse_with_nlp(text)
    else:
        # Fallback to regex-based parsing (Task 1.2)
        return _parse_with_regex(text)


def _parse_with_nlp(text):
    """
    Task 1.3: Extract individual rules using NLP techniques (spaCy)
    
    Uses linguistic analysis to better identify rule boundaries:
    - Sentence segmentation based on syntactic structure
    - Part-of-speech tagging to identify imperative/modal constructions
    - Dependency parsing to understand sentence structure
    - Named entity recognition to preserve context
    
    Args:
        text (str): Raw text to parse
        
    Returns:
        list: List of extracted rule clauses
    """
    doc = nlp(text)
    clauses = []
    
    # Strategy 1: Use spaCy's sentence segmentation
    # This is more sophisticated than regex as it understands linguistic structure
    for sent in doc.sents:
        sent_text = sent.text.strip()
        
        # Filter out non-rule sentences
        if not _is_likely_rule(sent_text, sent):
            continue
        
        # Clean up the sentence
        cleaned = _clean_clause(sent_text)
        
        if cleaned and len(cleaned) > 5:
            clauses.append(cleaned)
    
    # Strategy 2: If no sentences found or very few, try splitting by line breaks
    # This handles bulleted/numbered lists that spaCy might not segment well
    if len(clauses) < 2:
        lines = text.split('\n')
        numbered_pattern = r'^\s*(\d+[\.\)]\s*|[-*•]\s*)'
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Remove numbering/bullets
            cleaned = re.sub(numbered_pattern, '', line).strip()
            
            if cleaned and len(cleaned) > 5:
                # Check if it's a rule using NLP
                line_doc = nlp(cleaned)
                if any(_is_likely_rule(sent.text, sent) for sent in line_doc.sents):
                    if cleaned not in clauses:  # Avoid duplicates
                        clauses.append(cleaned)
    
    return clauses


def _is_likely_rule(text, sent_doc=None):
    """
    Task 1.3: Use NLP to determine if a sentence is likely a rule
    
    Analyzes linguistic features to identify rule-like sentences:
    - Modal verbs (must, should, cannot, etc.)
    - Imperative mood (commands)
    - Prohibitive constructions (no, not, never)
    - Obligation/permission language
    
    Args:
        text (str): Sentence text
        sent_doc (spacy.tokens.Span, optional): spaCy sentence object for analysis
        
    Returns:
        bool: True if the sentence is likely a rule
    """
    text_lower = text.lower()
    
    # Rule indicator keywords
    rule_indicators = [
        'must', 'should', 'cannot', "can't", "don't", 'do not',
        'never', 'always', 'prohibited', 'allowed', 'required',
        'no ', 'not ', 'please', 'be ', 'keep', 'avoid',
        'shall', 'will not', "won't", 'forbidden', 'banned',
        'ensure', 'make sure', 'refrain', 'respect', 'report'
    ]
    
    # Check for rule indicators
    has_indicator = any(indicator in text_lower for indicator in rule_indicators)
    
    # Filter out welcome/intro text
    intro_phrases = ['welcome', 'introduction', 'about us', 'overview', 'thank you']
    is_intro = any(phrase in text_lower for phrase in intro_phrases)
    
    if is_intro:
        return False
    
    # If we have spaCy doc, use linguistic analysis
    if sent_doc is not None:
        # Check for modal verbs (MD tag)
        has_modal = any(token.tag_ == 'MD' for token in sent_doc)
        
        # Check for imperative mood (verb at start or after "please")
        has_imperative = False
        if len(sent_doc) > 0:
            first_token = sent_doc[0]
            # Imperative sentences often start with a verb (VB or VBP tag)
            if first_token.pos_ == 'VERB' and first_token.tag_ in ['VB', 'VBP']:
                has_imperative = True
            # Or start with "please" followed by a verb
            elif first_token.text.lower() == 'please' and len(sent_doc) > 1:
                if sent_doc[1].pos_ == 'VERB':
                    has_imperative = True
        
        # Check for negation (no, not, never)
        has_negation = any(token.dep_ == 'neg' for token in sent_doc)
        
        # A sentence is likely a rule if it has any of these features
        if has_modal or has_imperative or has_negation or has_indicator:
            return True
    else:
        # Fallback to keyword-based detection
        return has_indicator
    
    return False


def _clean_clause(text):
    """
    Clean and normalize a rule clause
    
    Args:
        text (str): Raw clause text
        
    Returns:
        str: Cleaned clause text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Ensure proper ending punctuation
    if text and not text[-1] in '.!?':
        text += '.'
    
    return text


def assign_rule_identifiers(clauses, prefix="rule", start_num=1, padding=3):
    """
    Task 1.4: Assign unique identifiers to each extracted rule clause
    
    Takes a list of rule clause strings and returns a list of dictionaries
    with unique identifiers assigned to each clause.
    
    Args:
        clauses (list): List of rule clause strings
        prefix (str): Prefix for the identifier (default: "rule")
        start_num (int): Starting number for identifiers (default: 1)
        padding (int): Number of digits to pad the number (default: 3)
        
    Returns:
        list: List of dictionaries with 'id' and 'text' keys
        
    Example:
        >>> clauses = ["No harassment", "No spam"]
        >>> assign_rule_identifiers(clauses)
        [
            {"id": "rule_001", "text": "No harassment"},
            {"id": "rule_002", "text": "No spam"}
        ]
    """
    identified_rules = []
    
    for i, clause in enumerate(clauses, start=start_num):
        # Format the identifier with zero-padding
        rule_id = f"{prefix}_{str(i).zfill(padding)}"
        
        identified_rules.append({
            "id": rule_id,
            "text": clause
        })
    
    return identified_rules


def categorize_rule(rule_text):
    """
    Task 1.5: Categorize a rule based on its content
    
    Analyzes the rule text to determine its category using keyword matching
    and semantic analysis.
    
    Args:
        rule_text (str): The text of the rule to categorize
        
    Returns:
        str: The category of the rule (e.g., "conduct", "spam", "hate_speech", etc.)
    """
    text_lower = rule_text.lower()
    
    # Define category patterns with keywords
    category_patterns = {
        "hate_speech": ["hate speech", "hate", "discriminat", "racist", "sexist", "slur", "bigot"],
        "harassment": ["harass", "bully", "intimidat", "threaten", "stalk", "abuse"],
        "doxxing": ["doxx", "personal information", "private information", "address", "phone number", "real name"],
        "spam": ["spam", "promotional", "advertis", "self-promotion", "commercial"],
        "violence": ["violence", "violent", "harm", "attack", "assault", "threat"],
        "nsfw": ["nsfw", "explicit", "sexual", "pornograph", "adult content", "nudity"],
        "misinformation": ["misinformation", "false information", "fake news", "misleading"],
        "relevance": ["relevant", "on topic", "off topic", "community topic", "subject matter"],
        "respect": ["respect", "polite", "civil", "courteous", "kind"],
        "conduct": ["conduct", "behavior", "behave", "appropriate", "inappropriate"]
    }
    
    # Check each category
    for category, keywords in category_patterns.items():
        for keyword in keywords:
            if keyword in text_lower:
                return category
    
    # Default category if no match found
    return "general"


def extract_keywords(rule_text, max_keywords=5):
    """
    Task 1.5: Extract keywords from a rule text
    
    Identifies the most important keywords in a rule using various techniques:
    - Common rule-related terms
    - Nouns and verbs (if NLP is available)
    - Negation terms (no, not, never, etc.)
    
    Args:
        rule_text (str): The text of the rule
        max_keywords (int): Maximum number of keywords to extract (default: 5)
        
    Returns:
        list: List of extracted keywords
    """
    keywords = []
    text_lower = rule_text.lower()
    
    # Remove common punctuation for keyword extraction
    text_clean = re.sub(r'[.,!?;:]', '', text_lower)
    
    # If spaCy is available, use NLP for better keyword extraction
    if SPACY_AVAILABLE and nlp is not None:
        doc = nlp(text_clean)
        
        # Extract nouns, verbs, and adjectives
        for token in doc:
            # Skip stop words, short words, and common words
            if (token.pos_ in ['NOUN', 'VERB', 'ADJ'] and 
                not token.is_stop and 
                len(token.text) > 2 and
                token.text not in ['must', 'should', 'will', 'can', 'may', 'shall']):
                keywords.append(token.text)
        
        # Also look for multi-word expressions (noun chunks)
        for chunk in doc.noun_chunks:
            chunk_text = chunk.text.strip()
            if len(chunk_text.split()) > 1 and len(chunk_text) > 5:
                keywords.append(chunk_text)
    else:
        # Fallback: Extract words based on patterns
        words = text_clean.split()
        
        # Important rule-related terms
        important_terms = [
            'harassment', 'bullying', 'spam', 'promotional', 'hate speech',
            'doxxing', 'violence', 'threat', 'abuse', 'discrimination',
            'respect', 'relevant', 'appropriate', 'prohibited', 'allowed',
            'content', 'post', 'comment', 'user', 'member', 'community'
        ]
        
        for word in words:
            # Add important terms
            if word in important_terms:
                keywords.append(word)
            # Add longer words that aren't common stop words
            elif (len(word) > 4 and 
                  word not in ['should', 'would', 'could', 'their', 'there', 'these', 'those', 'about', 'which']):
                keywords.append(word)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_keywords = []
    for kw in keywords:
        if kw not in seen:
            seen.add(kw)
            unique_keywords.append(kw)
    
    # Limit to max_keywords
    return unique_keywords[:max_keywords]


def format_rules_json(clauses, prefix="rule", start_num=1, padding=3):
    """
    Task 1.5: Output structured JSON format with rule clauses
    
    Takes a list of rule clause strings and returns a complete structured
    JSON format with id, text, category, and keywords for each rule.
    
    This is the main function that combines all previous tasks:
    - Task 1.2 & 1.3: Parse and extract clauses (via parse_rule_clauses)
    - Task 1.4: Assign unique identifiers
    - Task 1.5: Add categories and keywords, format as JSON
    
    Args:
        clauses (list): List of rule clause strings
        prefix (str): Prefix for the identifier (default: "rule")
        start_num (int): Starting number for identifiers (default: 1)
        padding (int): Number of digits to pad the number (default: 3)
        
    Returns:
        dict: Dictionary with 'rules' key containing list of complete rule objects
        
    Example:
        >>> clauses = ["No harassment or bullying.", "Spam is prohibited."]
        >>> format_rules_json(clauses)
        {
            "rules": [
                {
                    "id": "rule_001",
                    "text": "No harassment or bullying.",
                    "category": "harassment",
                    "keywords": ["harassment", "bullying"]
                },
                {
                    "id": "rule_002",
                    "text": "Spam is prohibited.",
                    "category": "spam",
                    "keywords": ["spam", "prohibited"]
                }
            ]
        }
    """
    rules = []
    
    for i, clause in enumerate(clauses, start=start_num):
        # Format the identifier with zero-padding
        rule_id = f"{prefix}_{str(i).zfill(padding)}"
        
        # Categorize the rule
        category = categorize_rule(clause)
        
        # Extract keywords
        keywords = extract_keywords(clause)
        
        # Create the complete rule object
        rule = {
            "id": rule_id,
            "text": clause,
            "category": category,
            "keywords": keywords
        }
        
        rules.append(rule)
    
    return {"rules": rules}


def normalize_rules_to_json(raw_text, prefix="rule", start_num=1, padding=3):
    """
    Complete workflow: Parse raw text and output structured JSON
    
    This function combines all tasks from 1.1 to 1.5:
    1. Accept text input (Task 1.1)
    2. Parse text to identify discrete clauses (Task 1.2)
    3. Extract rules using NLP techniques (Task 1.3)
    4. Assign unique identifiers (Task 1.4)
    5. Add categories and keywords, output JSON (Task 1.5)
    
    Args:
        raw_text (str): Raw community guidelines or rules text
        prefix (str): Prefix for rule identifiers (default: "rule")
        start_num (int): Starting number for identifiers (default: 1)
        padding (int): Number of digits to pad the number (default: 3)
        
    Returns:
        dict: Complete structured JSON with all rules
        
    Example:
        >>> text = "No harassment. No spam. Be respectful."
        >>> result = normalize_rules_to_json(text)
        >>> print(json.dumps(result, indent=2))
    """
    # Step 1-3: Parse and extract clauses
    clauses = parse_rule_clauses(raw_text)
    
    # Step 4-5: Format with IDs, categories, and keywords
    return format_rules_json(clauses, prefix, start_num, padding)


def _parse_with_regex(text):
    """
    Task 1.2: Fallback regex-based parsing when NLP is not available
    
    This is the original implementation from Task 1.2.
    
    Args:
        text (str): Raw text to parse
        
    Returns:
        list: List of extracted rule clauses
    """
    clauses = []
    
    # First, try to identify if text uses explicit numbering or bullets
    numbered_pattern = r'^\s*(\d+[\.\)]\s*|[-*•]\s*)'
    lines = text.split('\n')
    
    # Check if text uses line-based formatting (each line is a rule)
    has_line_formatting = False
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    
    if len(non_empty_lines) > 1:
        # Check if lines start with numbers or bullets
        formatted_lines = sum(1 for line in non_empty_lines if re.match(numbered_pattern, line))
        if formatted_lines >= len(non_empty_lines) * 0.5:  # At least 50% are formatted
            has_line_formatting = True
    
    if has_line_formatting:
        # Parse line-by-line, removing numbering/bullets
        for line in non_empty_lines:
            # Remove leading numbers, bullets, and whitespace
            cleaned = re.sub(numbered_pattern, '', line).strip()
            # For numbered/bulleted lists, be more lenient - include all items
            if cleaned:
                clauses.append(cleaned)
    else:
        # Parse as continuous text - split by sentence boundaries
        # Replace multiple spaces/newlines with single space
        text = re.sub(r'\s+', ' ', text)
        
        # First, try simple period-space split for very short sentences
        simple_split = text.split('. ')
        all_short = all(len(s.strip()) < 30 for s in simple_split if s.strip())
        
        if all_short and len(simple_split) >= 1:
            # Likely a list of short rules like "No X. No Y. No Z."
            for sentence in simple_split:
                cleaned = sentence.strip()
                if cleaned and not cleaned.endswith('.'):
                    cleaned += '.'
                
                # Check if it looks like a rule
                if len(cleaned) > 5:
                    rule_indicators = ['must', 'should', 'cannot', "can't", "don't", 'do not', 
                                     'never', 'always', 'prohibited', 'allowed', 'required',
                                     'no ', 'not ', 'please', 'be ', 'keep', 'avoid']
                    
                    text_lower = cleaned.lower()
                    if any(indicator in text_lower for indicator in rule_indicators):
                        clauses.append(cleaned)
        else:
            # Use more sophisticated splitting for longer sentences
            # Split by periods followed by capital letters or common rule indicators
            sentences = re.split(r'\.(?=\s+(?:[A-Z]|No |Users |All |Do not |Don\'t |Never |Always |Must |Should |Cannot ))', text)
            
            for sentence in sentences:
                cleaned = sentence.strip()
                # Add back the period if it was removed
                if cleaned and not cleaned.endswith('.'):
                    cleaned += '.'
                
                # Filter out very short fragments and common non-rule text
                if len(cleaned) > 10 and not cleaned.lower().startswith('welcome'):
                    # Check if it looks like a rule (contains modal verbs or prohibitions)
                    rule_indicators = ['must', 'should', 'cannot', 'can\'t', 'don\'t', 'do not', 
                                     'never', 'always', 'prohibited', 'allowed', 'required',
                                     'no ', 'not ', 'please', 'be ', 'keep', 'avoid']
                    
                    text_lower = cleaned.lower()
                    if any(indicator in text_lower for indicator in rule_indicators):
                        clauses.append(cleaned)
    
    # Additional cleanup: merge very short clauses with previous ones
    # But only if they don't look like complete rules themselves
    merged_clauses = []
    for clause in clauses:
        # Don't merge if it's a short but complete rule (like "No spam.")
        is_complete_rule = (
            clause.strip().startswith(('No ', 'Do not ', "Don't ", 'Never ', 'Always ')) or
            any(word in clause.lower() for word in ['must', 'should', 'prohibited', 'required', 'allowed'])
        )
        
        if len(clause) < 15 and merged_clauses and not is_complete_rule:
            # Merge with previous clause
            merged_clauses[-1] = merged_clauses[-1] + ' ' + clause
        else:
            merged_clauses.append(clause)
    
    return merged_clauses


def normalize_rules(raw_text):
    print(">> 1. Normalizing Rulebook...")
    system_prompt = """You are the 'Rulebook Normalizer'.
Take the raw text provided and output a JSON list of individual, atomic rules.
Format: {"rules": [{"id": "1.0", "text": "exact rule text...", "category": "conduct|spam|doxxing|harassment", "keywords": ["key", "words"]}, ...]}
Do not change the meaning. Just split and number them."""

    response = client.chat.completions.create(
        model="gpt-4o",  # Or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": raw_text}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)

# ---------------------------------------------------------
# MODULE 2: THE CITATION ANCHOR ENGINE
# (The "Safety Gate" Logic)
# ---------------------------------------------------------
def adjudicate_dispute(user_comment, normalized_rules):
    print(">> 2. Running Citation Anchoring...")
    system_prompt = f"""You are the Open Adjudication Engine.

THE RULES:
{json.dumps(normalized_rules)}

THE TASK:
Analyze the USER COMMENT.

THE CONSTRAINT (CITATION ANCHORING):
You may ONLY find a violation if you can quote an exact string from 'THE RULES' that contradicts the comment.
If you cannot find a direct quote, you MUST return "verdict": "No Violation".

Output JSON format:
{{
    "verdict": "Violation" | "No Violation",
    "citation_anchor": {{
        "rule_id": "ID of the rule",
        "quoted_rule_text": "Exact text from the rulebook"
    }},
    "reasoning": "Explanation...",
    "confidence": 0.95
}}"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_comment}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)

# ---------------------------------------------------------
# DEMO EXECUTION
# (This is what you record for the demo video)
# ---------------------------------------------------------
if __name__ == "__main__":
    import sys
    
    # Check if text input is provided via command line
    if len(sys.argv) > 1:
        # Use command-line argument as input
        raw_community_rules = " ".join(sys.argv[1:])
        print(f"Processing input: {raw_community_rules[:100]}...")
        
        # Normalize the rules
        rules_json = normalize_rules(raw_community_rules)
        print("\n--- NORMALIZED CONSTITUTION ---")
        print(json.dumps(rules_json, indent=2))
    else:
        # A. The Messy Input (Simulating a Client's FAQ)
        raw_community_rules = """Welcome to our gaming forum! We want to keep things chill.
Please don't be mean. Absolutely no doxxing (sharing real addresses) is allowed, and if you spam promotion links you will be banned. Be nice!"""

        # B. The "Bad" User Comment
        user_message = "Ha! I know where you live. You are at 42 Wallaby Way, Sydney."

        # Step 1: Normalize
        rules_json = normalize_rules(raw_community_rules)
        print("\n--- NORMALIZED CONSTITUTION ---")
        print(json.dumps(rules_json, indent=2))

        # Step 2: Adjudicate
        verdict_json = adjudicate_dispute(user_message, rules_json)
        print("\n--- ADJUDICATION OUTPUT (WITH ANCHOR) ---")
        print(json.dumps(verdict_json, indent=2))
