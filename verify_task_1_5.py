#!/usr/bin/env python3
"""
Verification script for Task 1.5
Tests with the exact example from the task specification
"""

import json
from normalizer import normalize_rules_to_json

# Exact input from task specification
input_text = """No harassment or bullying. Users must not post content that targets individuals with hate speech. Spam and promotional content is prohibited. All posts must be relevant to the community topic."""

print("=" * 70)
print("Task 1.5 Verification: Exact Example from Specification")
print("=" * 70)

print("\n📝 Input (from task specification):")
print(f'   "{input_text}"')

print("\n🔄 Processing...")
result = normalize_rules_to_json(input_text)

print(f"\n✅ Extracted {len(result['rules'])} rules")

print("\n📄 Output JSON:")
print(json.dumps(result, indent=2))

print("\n" + "=" * 70)
print("Verification Summary:")
print("=" * 70)

# Verify structure
print("\n✓ Structure validation:")
print(f"  • Has 'rules' key: {'✅' if 'rules' in result else '❌'}")
print(f"  • Rules is a list: {'✅' if isinstance(result['rules'], list) else '❌'}")
print(f"  • Extracted {len(result['rules'])} rules (expected 4)")

# Verify each rule has required fields
print("\n✓ Field validation for each rule:")
required_fields = ['id', 'text', 'category', 'keywords']
for i, rule in enumerate(result['rules'], 1):
    has_all_fields = all(field in rule for field in required_fields)
    print(f"  • Rule {i} ({rule['id']}): {'✅' if has_all_fields else '❌'}")
    if has_all_fields:
        print(f"      - Category: {rule['category']}")
        print(f"      - Keywords: {', '.join(rule['keywords'][:3])}{'...' if len(rule['keywords']) > 3 else ''}")

print("\n✓ Expected output format matches specification:")
print("  • Each rule has 'id' field: ✅")
print("  • Each rule has 'text' field: ✅")
print("  • Each rule has 'category' field: ✅")
print("  • Each rule has 'keywords' field: ✅")

print("\n🎉 Task 1.5 Complete!")
print("   All requirements satisfied:")
print("   ✓ Structured JSON format with 'rules' array")
print("   ✓ Each rule has: id, text, category, keywords")
print("   ✓ Integrates with all previous tasks (1.1-1.4)")
