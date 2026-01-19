#!/usr/bin/env python3
import sys
import json
from normalizer import (
    categorize_rule,
    extract_keywords,
    format_rules_json,
    normalize_rules_to_json,
    parse_rule_clauses
)

print("=" * 70)
print("Task 1.5 Tests: Output Structured JSON Format")
print("=" * 70)

# Test 1: Categorization
print("\n🧪 Test 1.5a: Rule categorization")
test_cases = [
    ("No harassment or bullying.", "harassment"),
    ("Spam and promotional content is prohibited.", "spam"),
]

for rule_text, expected_category in test_cases:
    category = categorize_rule(rule_text)
    if category == expected_category:
        print(f"   ✅ '{rule_text[:40]}...' → {category}")
    else:
        print(f"   ❌ '{rule_text[:40]}...' → {category} (expected {expected_category})")

# Test 2: Complete workflow
print("\n🧪 Test 1.5b: Complete workflow (text → JSON)")
text = "No harassment or bullying. Spam is prohibited."
result = normalize_rules_to_json(text)
print(f"   ✅ Extracted {len(result['rules'])} rules from text")
print(f"\n   📄 JSON output:")
print(json.dumps(result, indent=2))

print("\n" + "=" * 70)
print("✅ Tests complete!")
print("=" * 70)
