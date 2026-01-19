#!/usr/bin/env python3
"""
Demo script for Task 1.5: Output structured JSON format with rule clauses

This script demonstrates the complete workflow from Tasks 1.1-1.5:
1. Accept text input
2. Parse text to identify discrete clauses
3. Use NLP techniques for extraction
4. Assign unique identifiers to each clause
5. Add categories and keywords, output structured JSON
"""

import json
from normalizer import (
    parse_rule_clauses, 
    format_rules_json, 
    normalize_rules_to_json,
    categorize_rule,
    extract_keywords
)


def demo_basic_usage():
    """Demonstrate basic usage of the complete JSON formatting"""
    print("=" * 70)
    print("DEMO 1: Basic Usage - Complete JSON Output")
    print("=" * 70)
    
    # Sample community guidelines (from task specification)
    text = """No harassment or bullying. Users must not post content that targets 
    individuals with hate speech. Spam and promotional content is prohibited. 
    All posts must be relevant to the community topic."""
    
    print("\n📝 Input Text:")
    print(f"   {text}")
    
    # Use the complete workflow function
    print("\n🔄 Processing through complete workflow...")
    result = normalize_rules_to_json(text)
    
    print(f"\n✅ Extracted {len(result['rules'])} rules with complete metadata")
    
    # Display each rule
    print("\n📋 Rules with Categories and Keywords:")
    for rule in result['rules']:
        print(f"\n   {rule['id']}:")
        print(f"      Text: {rule['text']}")
        print(f"      Category: {rule['category']}")
        print(f"      Keywords: {', '.join(rule['keywords'])}")
    
    # Show complete JSON output
    print("\n📄 Complete JSON Output:")
    print(json.dumps(result, indent=2))


def demo_categorization():
    """Demonstrate rule categorization"""
    print("\n\n" + "=" * 70)
    print("DEMO 2: Rule Categorization")
    print("=" * 70)
    
    test_rules = [
        "No harassment or bullying of other members.",
        "Spam and promotional content is prohibited.",
        "Do not share personal information (doxxing).",
        "Hate speech and discrimination are not allowed.",
        "All posts must be relevant to the community topic.",
        "Be respectful and kind to all members.",
        "No violent or threatening content."
    ]
    
    print("\n🏷️  Testing categorization on various rules:")
    for rule in test_rules:
        category = categorize_rule(rule)
        print(f"\n   Rule: {rule[:60]}...")
        print(f"   Category: {category}")


def demo_keyword_extraction():
    """Demonstrate keyword extraction"""
    print("\n\n" + "=" * 70)
    print("DEMO 3: Keyword Extraction")
    print("=" * 70)
    
    test_rules = [
        "No harassment or bullying of other members.",
        "Users must not post content that targets individuals with hate speech.",
        "Spam and promotional content is prohibited.",
        "All posts must be relevant to the community topic."
    ]
    
    print("\n🔑 Testing keyword extraction:")
    for rule in test_rules:
        keywords = extract_keywords(rule)
        print(f"\n   Rule: {rule[:60]}...")
        print(f"   Keywords: {', '.join(keywords)}")


def demo_real_world_example():
    """Demonstrate with a real-world community guidelines example"""
    print("\n\n" + "=" * 70)
    print("DEMO 4: Real-World Community Guidelines")
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
    
    # Process through complete workflow
    result = normalize_rules_to_json(text)
    
    print(f"\n✅ Processed {len(result['rules'])} rules")
    
    print("\n📄 Complete JSON Output:")
    print(json.dumps(result, indent=2))


def demo_discord_example():
    """Demonstrate with Discord-style guidelines"""
    print("\n\n" + "=" * 70)
    print("DEMO 5: Discord-Style Guidelines")
    print("=" * 70)
    
    text = """Hey everyone! Welcome to our Discord server. We're excited to have you here.
    
    Please don't be mean to other members. Absolutely no doxxing (sharing real addresses) 
    is allowed, and if you spam promotion links you will be banned. Be nice and have fun!
    
    Thanks for reading!"""
    
    print("\n📝 Input Text (Discord-style guidelines):")
    print(text)
    
    # Process through complete workflow
    result = normalize_rules_to_json(text)
    
    print(f"\n✅ Processed {len(result['rules'])} rules")
    
    print("\n📄 Complete JSON Output:")
    print(json.dumps(result, indent=2))


def demo_step_by_step():
    """Demonstrate the step-by-step process"""
    print("\n\n" + "=" * 70)
    print("DEMO 6: Step-by-Step Workflow (Tasks 1.1 → 1.5)")
    print("=" * 70)
    
    text = "No harassment. Spam is prohibited. Be respectful to all members."
    
    print("\n📝 Step 1: Accept Text Input (Task 1.1)")
    print(f"   Input: {text}")
    
    print("\n🔍 Step 2-3: Parse and Extract Clauses (Tasks 1.2 & 1.3)")
    clauses = parse_rule_clauses(text)
    print(f"   Extracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    print("\n🏷️  Step 4-5: Format with IDs, Categories, Keywords (Tasks 1.4 & 1.5)")
    result = format_rules_json(clauses)
    
    print("\n📊 Final Structured Output:")
    for rule in result['rules']:
        print(f"\n   {rule['id']}:")
        print(f"      Text: {rule['text']}")
        print(f"      Category: {rule['category']}")
        print(f"      Keywords: {', '.join(rule['keywords'])}")
    
    print("\n📄 JSON Format:")
    print(json.dumps(result, indent=2))


def demo_comparison():
    """Compare input vs output to show transformation"""
    print("\n\n" + "=" * 70)
    print("DEMO 7: Input vs Output Comparison")
    print("=" * 70)
    
    text = """No harassment or bullying. Users must not post content that targets 
individuals with hate speech. Spam and promotional content is prohibited. 
All posts must be relevant to the community topic."""
    
    print("\n📥 INPUT (Messy Text):")
    print("-" * 70)
    print(text)
    print("-" * 70)
    
    result = normalize_rules_to_json(text)
    
    print("\n📤 OUTPUT (Structured JSON):")
    print("-" * 70)
    print(json.dumps(result, indent=2))
    print("-" * 70)
    
    print("\n✨ Transformation Summary:")
    print(f"   • Extracted {len(result['rules'])} discrete rules")
    print(f"   • Assigned unique IDs (rule_001, rule_002, etc.)")
    print(f"   • Categorized each rule by content")
    print(f"   • Extracted relevant keywords")
    print(f"   • Formatted as structured JSON")


def demo_edge_cases():
    """Demonstrate handling of edge cases"""
    print("\n\n" + "=" * 70)
    print("DEMO 8: Edge Cases")
    print("=" * 70)
    
    # Single rule
    print("\n📝 Edge Case 1: Single Rule")
    text1 = "No harassment or bullying."
    result1 = normalize_rules_to_json(text1)
    print(f"   Input: {text1}")
    print(f"   Output: {len(result1['rules'])} rule")
    print(json.dumps(result1, indent=2))
    
    # Empty input
    print("\n📝 Edge Case 2: Empty Input")
    text2 = ""
    result2 = normalize_rules_to_json(text2)
    print(f"   Input: (empty string)")
    print(f"   Output: {len(result2['rules'])} rules")
    print(json.dumps(result2, indent=2))
    
    # Complex rule with multiple concepts
    print("\n📝 Edge Case 3: Complex Rule")
    text3 = "Users must not engage in harassment, bullying, hate speech, or any form of discrimination based on race, gender, religion, or sexual orientation."
    result3 = normalize_rules_to_json(text3)
    print(f"   Input: {text3[:60]}...")
    print(f"   Output:")
    print(json.dumps(result3, indent=2))


def main():
    """Run all demonstrations"""
    print("\n" + "🎯" * 35)
    print("Task 1.5 Demonstration: Output Structured JSON Format")
    print("🎯" * 35)
    
    demo_basic_usage()
    demo_categorization()
    demo_keyword_extraction()
    demo_real_world_example()
    demo_discord_example()
    demo_step_by_step()
    demo_comparison()
    demo_edge_cases()
    
    print("\n\n" + "=" * 70)
    print("✅ All demonstrations complete!")
    print("=" * 70)
    print("\nKey Features Demonstrated:")
    print("  ✓ Complete JSON output with id, text, category, keywords")
    print("  ✓ Automatic rule categorization")
    print("  ✓ Intelligent keyword extraction")
    print("  ✓ Integration with all previous tasks (1.1-1.4)")
    print("  ✓ Edge case handling")
    print("  ✓ Real-world examples (Reddit, Discord)")
    print("\n🎉 Task 1.5 Complete: Rule Text Normalization (Step 1.1) FINISHED!")
    print("\nNext Step: Task 1.6-1.9 - Testing for Step 1")


if __name__ == "__main__":
    main()
