#!/usr/bin/env python3
"""
Demo script for Task 1.4: Assign unique identifiers to rule clauses

This script demonstrates the complete workflow from Tasks 1.1-1.4:
1. Accept text input
2. Parse text to identify discrete clauses
3. Use NLP techniques for extraction
4. Assign unique identifiers to each clause
"""

import json
from normalizer import parse_rule_clauses, assign_rule_identifiers


def demo_basic_usage():
    """Demonstrate basic usage of the identifier assignment"""
    print("=" * 70)
    print("DEMO 1: Basic Usage")
    print("=" * 70)
    
    # Sample community guidelines
    text = """No harassment or bullying. Users must not post content that targets 
    individuals with hate speech. Spam and promotional content is prohibited. 
    All posts must be relevant to the community topic."""
    
    print("\n📝 Input Text:")
    print(f"   {text}")
    
    # Step 1: Parse clauses
    print("\n🔍 Step 1: Parse rule clauses...")
    clauses = parse_rule_clauses(text)
    print(f"   Found {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Step 2: Assign identifiers
    print("\n🏷️  Step 2: Assign unique identifiers...")
    identified_rules = assign_rule_identifiers(clauses)
    print(f"   Assigned IDs to {len(identified_rules)} rules:")
    for rule in identified_rules:
        print(f"      {rule['id']}: {rule['text']}")
    
    # Step 3: Show JSON output
    print("\n📄 JSON Output:")
    print(json.dumps({"rules": identified_rules}, indent=2))


def demo_real_world_example():
    """Demonstrate with a real-world community guidelines example"""
    print("\n\n" + "=" * 70)
    print("DEMO 2: Real-World Community Guidelines")
    print("=" * 70)
    
    # Reddit-style community guidelines
    text = """Welcome to our community! Please follow these guidelines:

1. Be respectful to all members
2. No hate speech, harassment, or bullying
3. Do not share personal information (doxxing)
4. Spam and excessive self-promotion are not allowed
5. Stay on topic and keep discussions relevant
6. Follow all applicable laws and regulations"""
    
    print("\n📝 Input Text (Reddit-style guidelines):")
    print(text)
    
    # Parse and identify
    clauses = parse_rule_clauses(text)
    identified_rules = assign_rule_identifiers(clauses)
    
    print(f"\n🏷️  Extracted and Identified {len(identified_rules)} Rules:")
    for rule in identified_rules:
        print(f"   {rule['id']}: {rule['text'][:60]}{'...' if len(rule['text']) > 60 else ''}")
    
    print("\n📄 JSON Output:")
    print(json.dumps({"rules": identified_rules}, indent=2))


def demo_custom_configuration():
    """Demonstrate custom prefix and numbering"""
    print("\n\n" + "=" * 70)
    print("DEMO 3: Custom Configuration")
    print("=" * 70)
    
    text = "No spam. Be respectful. Stay on topic."
    clauses = parse_rule_clauses(text)
    
    print("\n📝 Input Text:")
    print(f"   {text}")
    print(f"\n   Parsed {len(clauses)} clauses")
    
    # Default configuration
    print("\n🏷️  Default Configuration (prefix='rule', start=1):")
    default_rules = assign_rule_identifiers(clauses)
    for rule in default_rules:
        print(f"   {rule['id']}: {rule['text']}")
    
    # Custom prefix
    print("\n🏷️  Custom Prefix (prefix='guideline'):")
    custom_prefix = assign_rule_identifiers(clauses, prefix="guideline")
    for rule in custom_prefix:
        print(f"   {rule['id']}: {rule['text']}")
    
    # Custom start number
    print("\n🏷️  Custom Start Number (start=10):")
    custom_start = assign_rule_identifiers(clauses, start_num=10)
    for rule in custom_start:
        print(f"   {rule['id']}: {rule['text']}")


def demo_edge_cases():
    """Demonstrate handling of edge cases"""
    print("\n\n" + "=" * 70)
    print("DEMO 4: Edge Cases")
    print("=" * 70)
    
    # Single rule
    print("\n📝 Edge Case 1: Single Rule")
    text1 = "No harassment or bullying."
    clauses1 = parse_rule_clauses(text1)
    rules1 = assign_rule_identifiers(clauses1)
    print(f"   Input: {text1}")
    print(f"   Output: {rules1}")
    
    # Empty input
    print("\n📝 Edge Case 2: Empty Input")
    text2 = ""
    clauses2 = parse_rule_clauses(text2)
    rules2 = assign_rule_identifiers(clauses2)
    print(f"   Input: (empty string)")
    print(f"   Output: {rules2}")
    
    # Many rules
    print("\n📝 Edge Case 3: Many Rules (10 rules)")
    text3 = ". ".join([f"Rule number {i}" for i in range(1, 11)]) + "."
    clauses3 = parse_rule_clauses(text3)
    rules3 = assign_rule_identifiers(clauses3)
    print(f"   Input: {len(clauses3)} rules")
    print(f"   First 3 IDs: {[r['id'] for r in rules3[:3]]}")
    print(f"   Last 3 IDs: {[r['id'] for r in rules3[-3:]]}")


def demo_complete_workflow():
    """Demonstrate the complete workflow from raw text to identified rules"""
    print("\n\n" + "=" * 70)
    print("DEMO 5: Complete Workflow (Tasks 1.1 → 1.4)")
    print("=" * 70)
    
    # Messy, real-world input
    text = """Hey everyone! Welcome to our Discord server. We're excited to have you here.
    
    Please don't be mean to other members. Absolutely no doxxing (sharing real addresses) 
    is allowed, and if you spam promotion links you will be banned. Be nice and have fun!
    
    Thanks for reading!"""
    
    print("\n📝 Task 1.1: Accept Text Input")
    print("   ✅ Text input accepted")
    print(f"   Length: {len(text)} characters")
    
    print("\n🔍 Task 1.2 & 1.3: Parse and Extract Rule Clauses")
    clauses = parse_rule_clauses(text)
    print(f"   ✅ Extracted {len(clauses)} rule clauses")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause[:60]}{'...' if len(clause) > 60 else ''}")
    
    print("\n🏷️  Task 1.4: Assign Unique Identifiers")
    identified_rules = assign_rule_identifiers(clauses)
    print(f"   ✅ Assigned unique IDs to {len(identified_rules)} rules")
    
    print("\n📊 Final Output:")
    output = {"rules": identified_rules}
    print(json.dumps(output, indent=2))
    
    print("\n✅ Complete workflow successful!")
    print("   Next: Task 1.5 will add categories and keywords")


def main():
    """Run all demonstrations"""
    print("\n" + "🎯" * 35)
    print("Task 1.4 Demonstration: Assign Unique Identifiers to Rule Clauses")
    print("🎯" * 35)
    
    demo_basic_usage()
    demo_real_world_example()
    demo_custom_configuration()
    demo_edge_cases()
    demo_complete_workflow()
    
    print("\n\n" + "=" * 70)
    print("✅ All demonstrations complete!")
    print("=" * 70)
    print("\nKey Features Demonstrated:")
    print("  ✓ Unique ID assignment (rule_001, rule_002, etc.)")
    print("  ✓ Integration with parse_rule_clauses()")
    print("  ✓ Custom prefixes and numbering")
    print("  ✓ Edge case handling")
    print("  ✓ Complete workflow from raw text to identified rules")
    print("\nNext Step: Task 1.5 - Add categories and keywords to complete JSON output")


if __name__ == "__main__":
    main()
