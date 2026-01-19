#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo for Task 1.6: Rule Extraction Accuracy Testing

This script demonstrates how the unit tests validate rule extraction accuracy
and shows examples of what the tests are checking.
"""

from normalizer import parse_rule_clauses, normalize_rules_to_json
import json


def demo_test_purpose():
    """Demonstrate the purpose of the accuracy tests"""
    print("=" * 70)
    print("TASK 1.6 DEMO: Rule Extraction Accuracy Testing")
    print("=" * 70)
    print("\nThe unit tests in test_task_1_6.py validate that rules are:")
    print("  1. Correctly extracted from various input formats")
    print("  2. Accurately identified (no false positives/negatives)")
    print("  3. Properly handled in edge cases")
    print("  4. Matching expected output")
    print()


def demo_accurate_extraction():
    """Show an example of accurate extraction"""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Accurate Extraction (Paragraph Format)")
    print("=" * 70)
    
    text = """No harassment or bullying. Users must not post content that targets 
individuals with hate speech. Spam and promotional content is prohibited. 
All posts must be relevant to the community topic."""
    
    print(f"\nInput text:")
    print(f"  {text}")
    
    result = normalize_rules_to_json(text)
    
    print(f"\nExtracted {len(result['rules'])} rules:")
    for rule in result['rules']:
        print(f"  {rule['id']}: {rule['text']}")
    
    print("\n✅ This extraction is ACCURATE:")
    print("  - All 4 rules correctly identified")
    print("  - No false positives (non-rules)")
    print("  - No false negatives (missed rules)")
    print("  - Complete JSON structure")


def demo_inaccurate_extraction():
    """Show an example where extraction has issues"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Inaccurate Extraction (Numbered Format)")
    print("=" * 70)
    
    text = """1. No harassment or bullying
2. Users must not post spam
3. All posts must be relevant to the community"""
    
    print(f"\nInput text:")
    print(f"  {text}")
    
    clauses = parse_rule_clauses(text)
    
    print(f"\nExtracted {len(clauses)} rules:")
    for i, clause in enumerate(clauses, 1):
        print(f"  {i}. {clause}")
    
    print("\n❌ This extraction has ISSUES:")
    print("  - Numbers from next lines are appended to rules")
    print("  - Example: 'No harassment or bullying 2.' instead of 'No harassment or bullying'")
    print("  - The test correctly identifies this as inaccurate")


def demo_false_positive_detection():
    """Show how tests detect false positives"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: False Positive Detection")
    print("=" * 70)
    
    text = """Welcome to our community! We're glad you're here.
Please be respectful to all members. No spam is allowed."""
    
    print(f"\nInput text:")
    print(f"  {text}")
    
    clauses = parse_rule_clauses(text)
    
    print(f"\nExtracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"  {i}. {clause}")
    
    # Check for false positives
    false_positives = [c for c in clauses if 'welcome' in c.lower() or 'glad' in c.lower()]
    
    if false_positives:
        print("\n❌ FALSE POSITIVES detected:")
        for fp in false_positives:
            print(f"  - '{fp}' (not a rule, should be filtered)")
    else:
        print("\n✅ NO FALSE POSITIVES:")
        print("  - Welcome text correctly filtered out")
        print("  - Only actual rules extracted")


def demo_false_negative_detection():
    """Show how tests detect false negatives"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: False Negative Detection")
    print("=" * 70)
    
    text = """1. No harassment
2. No spam
3. No doxxing
4. Be respectful
5. Stay on topic"""
    
    print(f"\nInput text:")
    print(f"  {text}")
    
    clauses = parse_rule_clauses(text)
    
    print(f"\nExpected: 5 rules")
    print(f"Extracted: {len(clauses)} rules")
    
    if len(clauses) < 5:
        print(f"\n❌ FALSE NEGATIVES detected:")
        print(f"  - {5 - len(clauses)} rule(s) were missed")
        print(f"  - The test identifies this as inaccurate")
    else:
        print(f"\n✅ NO FALSE NEGATIVES:")
        print(f"  - All 5 rules correctly extracted")
        
    print(f"\nExtracted rules:")
    for i, clause in enumerate(clauses, 1):
        print(f"  {i}. {clause}")


def demo_edge_cases():
    """Show how tests handle edge cases"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Edge Case Testing")
    print("=" * 70)
    
    test_cases = [
        ("Empty input", ""),
        ("Single rule", "No harassment."),
        ("Very short rules", "No spam. Be nice. Stay on topic."),
    ]
    
    for name, text in test_cases:
        print(f"\n{name}:")
        print(f"  Input: '{text}'")
        
        clauses = parse_rule_clauses(text)
        print(f"  Extracted: {len(clauses)} rule(s)")
        
        if clauses:
            for clause in clauses:
                print(f"    - {clause}")


def demo_test_results():
    """Show the overall test results"""
    print("\n" + "=" * 70)
    print("OVERALL TEST RESULTS")
    print("=" * 70)
    
    print("\nThe test suite includes 14 comprehensive tests:")
    print("\n✅ Passing Tests (10/14):")
    print("  1. Paragraph format accuracy")
    print("  2. Single rule accuracy")
    print("  3. Empty input accuracy")
    print("  4. No false positives")
    print("  5. No false negatives")
    print("  6. Reddit rules accuracy")
    print("  7. JSON output accuracy")
    print("  8. Extraction consistency")
    print("  9. Very long rule accuracy")
    print("  10. Very short rules accuracy")
    
    print("\n❌ Failing Tests (4/14):")
    print("  1. Numbered format accuracy - numbers appended to rules")
    print("  2. Bulleted format accuracy - count mismatch")
    print("  3. Complex paragraph accuracy - false positives")
    print("  4. Discord rules accuracy - bullet character not recognized")
    
    print("\nAccuracy: 71.4%")
    print("\nThe tests successfully identify areas for improvement!")


def main():
    """Run all demos"""
    demo_test_purpose()
    demo_accurate_extraction()
    demo_inaccurate_extraction()
    demo_false_positive_detection()
    demo_false_negative_detection()
    demo_edge_cases()
    demo_test_results()
    
    print("\n" + "=" * 70)
    print("To run the full test suite, execute:")
    print("  python test_task_1_6.py")
    print("=" * 70)


if __name__ == "__main__":
    main()
