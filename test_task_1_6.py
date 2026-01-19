#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test for Task 1.6: Write unit tests for rule extraction accuracy

This comprehensive test suite validates that rules are correctly extracted from
various input formats with high accuracy. It tests:
1. Correct extraction from various input formats (numbered, bulleted, paragraph)
2. Accuracy of rule identification
3. Edge cases (empty input, single rule, complex paragraphs)
4. Extracted rules match expected output
5. No false positives (non-rules not extracted)
6. No false negatives (actual rules not missed)
"""

import sys
from normalizer import parse_rule_clauses, normalize_rules_to_json


def test_numbered_format_accuracy():
    """Test accurate extraction from numbered list format"""
    print("🧪 Test 1.6a: Numbered format extraction accuracy")
    
    text = """1. No harassment or bullying
2. Users must not post spam
3. All posts must be relevant to the community"""
    
    clauses = parse_rule_clauses(text)
    
    expected_rules = [
        "No harassment or bullying",
        "Users must not post spam",
        "All posts must be relevant to the community"
    ]
    
    print(f"   Expected: {len(expected_rules)} rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    # Check count
    if len(clauses) != len(expected_rules):
        print(f"   ❌ Count mismatch: expected {len(expected_rules)}, got {len(clauses)}")
        return False
    
    # Check content accuracy
    all_accurate = True
    for i, (extracted, expected) in enumerate(zip(clauses, expected_rules), 1):
        # Normalize for comparison (remove trailing periods, case-insensitive)
        extracted_norm = extracted.rstrip('.').lower()
        expected_norm = expected.rstrip('.').lower()
        
        if extracted_norm == expected_norm:
            print(f"   ✅ Rule {i}: Accurate extraction")
        else:
            print(f"   ❌ Rule {i}: Mismatch")
            print(f"      Expected: {expected}")
            print(f"      Got: {extracted}")
            all_accurate = False
    
    return all_accurate


def test_bulleted_format_accuracy():
    """Test accurate extraction from bulleted list format"""
    print("\n🧪 Test 1.6b: Bulleted format extraction accuracy")
    
    text = """- No hate speech or discrimination
- Spam and promotional content is prohibited
- Be respectful to all members"""
    
    clauses = parse_rule_clauses(text)
    
    expected_count = 3
    expected_keywords = [
        ["hate speech", "discrimination"],
        ["spam", "promotional"],
        ["respectful", "members"]
    ]
    
    print(f"   Expected: {expected_count} rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    if len(clauses) != expected_count:
        print(f"   ❌ Count mismatch")
        return False
    
    # Check that key concepts are present
    all_accurate = True
    for i, (clause, keywords) in enumerate(zip(clauses, expected_keywords), 1):
        clause_lower = clause.lower()
        found_keywords = [kw for kw in keywords if kw in clause_lower]
        
        if len(found_keywords) >= 1:  # At least one keyword should be present
            print(f"   ✅ Rule {i}: Contains expected concepts ({', '.join(found_keywords)})")
        else:
            print(f"   ❌ Rule {i}: Missing expected concepts")
            print(f"      Expected keywords: {keywords}")
            print(f"      Got: {clause}")
            all_accurate = False
    
    return all_accurate


def test_paragraph_format_accuracy():
    """Test accurate extraction from paragraph-style continuous text"""
    print("\n🧪 Test 1.6c: Paragraph format extraction accuracy")
    
    # This is the example from the task specification
    text = """No harassment or bullying. Users must not post content that targets 
individuals with hate speech. Spam and promotional content is prohibited. 
All posts must be relevant to the community topic."""
    
    clauses = parse_rule_clauses(text)
    
    # Should extract 4 distinct rules
    expected_min = 4
    
    print(f"   Expected: At least {expected_min} rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    if len(clauses) < expected_min:
        print(f"   ❌ Too few rules extracted")
        for i, clause in enumerate(clauses, 1):
            print(f"      {i}. {clause}")
        return False
    
    # Check for key concepts
    all_text = " ".join(clauses).lower()
    required_concepts = ["harassment", "hate speech", "spam", "relevant"]
    
    all_present = True
    for concept in required_concepts:
        if concept in all_text:
            print(f"   ✅ Concept '{concept}' found in extracted rules")
        else:
            print(f"   ❌ Concept '{concept}' missing from extracted rules")
            all_present = False
    
    return all_present


def test_single_rule_accuracy():
    """Test accurate extraction of a single rule"""
    print("\n🧪 Test 1.6d: Single rule extraction accuracy")
    
    test_cases = [
        ("No harassment or bullying.", 1),
        ("Users must be respectful at all times.", 1),
        ("Spam is prohibited.", 1),
    ]
    
    all_accurate = True
    for text, expected_count in test_cases:
        clauses = parse_rule_clauses(text)
        
        if len(clauses) == expected_count:
            print(f"   ✅ '{text}' → {len(clauses)} rule (correct)")
        else:
            print(f"   ❌ '{text}' → {len(clauses)} rules (expected {expected_count})")
            all_accurate = False
    
    return all_accurate


def test_empty_input_accuracy():
    """Test that empty input returns no rules (no false positives)"""
    print("\n🧪 Test 1.6e: Empty input accuracy (no false positives)")
    
    test_cases = ["", "   ", "\n\n\n", "\t\t"]
    
    all_accurate = True
    for text in test_cases:
        clauses = parse_rule_clauses(text)
        
        if len(clauses) == 0:
            print(f"   ✅ Empty input '{repr(text)}' → 0 rules (correct)")
        else:
            print(f"   ❌ Empty input '{repr(text)}' → {len(clauses)} rules (should be 0)")
            all_accurate = False
    
    return all_accurate


def test_complex_paragraph_accuracy():
    """Test accurate extraction from complex paragraphs with mixed content"""
    print("\n🧪 Test 1.6f: Complex paragraph extraction accuracy")
    
    text = """Welcome to our gaming forum! We want to keep things chill.
Please don't be mean. Absolutely no doxxing (sharing real addresses) is allowed, 
and if you spam promotion links you will be banned. Be nice!"""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Extracted {len(clauses)} rules from complex paragraph")
    
    # Should extract at least 2-3 actual rules (filtering out welcome text)
    if len(clauses) < 2:
        print(f"   ❌ Too few rules extracted (expected at least 2)")
        return False
    
    # Check that welcome text is NOT included (no false positives)
    has_welcome = any('welcome' in clause.lower() for clause in clauses)
    has_chill = any('keep things chill' in clause.lower() for clause in clauses)
    
    if has_welcome or has_chill:
        print(f"   ❌ False positive: Non-rule text included in extraction")
        return False
    
    # Check that actual rules ARE included (no false negatives)
    all_text = " ".join(clauses).lower()
    required_concepts = ["doxxing", "spam"]
    
    all_present = True
    for concept in required_concepts:
        if concept in all_text:
            print(f"   ✅ Rule concept '{concept}' correctly extracted")
        else:
            print(f"   ❌ Rule concept '{concept}' missed (false negative)")
            all_present = False
    
    return all_present


def test_no_false_positives():
    """Test that non-rule text is not extracted as rules"""
    print("\n🧪 Test 1.6g: No false positives (non-rules not extracted)")
    
    # Text with clear non-rule content
    text = """Welcome to our community! We're glad you're here.
Thank you for joining us. We hope you enjoy your stay.
Please be respectful to all members. No spam is allowed."""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Extracted {len(clauses)} clauses")
    
    # Check for false positives
    false_positives = []
    for clause in clauses:
        clause_lower = clause.lower()
        if any(phrase in clause_lower for phrase in ['welcome', 'glad', 'thank you', 'hope you enjoy']):
            false_positives.append(clause)
    
    if len(false_positives) > 0:
        print(f"   ❌ Found {len(false_positives)} false positives:")
        for fp in false_positives:
            print(f"      - {fp}")
        return False
    else:
        print(f"   ✅ No false positives detected")
    
    # Check that actual rules were extracted (no false negatives)
    all_text = " ".join(clauses).lower()
    if 'respectful' in all_text and 'spam' in all_text:
        print(f"   ✅ Actual rules correctly extracted")
        return True
    else:
        print(f"   ❌ Actual rules missed (false negatives)")
        return False


def test_no_false_negatives():
    """Test that actual rules are not missed"""
    print("\n🧪 Test 1.6h: No false negatives (actual rules not missed)")
    
    # Text with clear rules that should all be extracted
    text = """1. No harassment
2. No spam
3. No doxxing
4. Be respectful
5. Stay on topic"""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Expected: 5 rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    # All 5 rules should be extracted
    if len(clauses) < 5:
        print(f"   ❌ False negatives: {5 - len(clauses)} rules missed")
        print(f"   Extracted rules:")
        for i, clause in enumerate(clauses, 1):
            print(f"      {i}. {clause}")
        return False
    
    # Check that key concepts are present
    all_text = " ".join(clauses).lower()
    required_concepts = ["harassment", "spam", "doxxing", "respectful", "topic"]
    
    missing_concepts = []
    for concept in required_concepts:
        if concept not in all_text:
            missing_concepts.append(concept)
    
    if len(missing_concepts) > 0:
        print(f"   ❌ Missing concepts (false negatives): {', '.join(missing_concepts)}")
        return False
    else:
        print(f"   ✅ All rules correctly extracted (no false negatives)")
        return True


def test_real_world_reddit_rules():
    """Test with real-world Reddit-style community rules"""
    print("\n🧪 Test 1.6i: Real-world Reddit rules extraction accuracy")
    
    text = """r/Python Community Rules:
1. Be respectful and civil
2. No spam or self-promotion
3. Posts must be related to Python
4. No homework help requests
5. Use appropriate post flair
6. No piracy or illegal content"""
    
    clauses = parse_rule_clauses(text)
    
    expected_min = 6
    print(f"   Expected: At least {expected_min} rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    if len(clauses) < expected_min:
        print(f"   ❌ Missed {expected_min - len(clauses)} rules")
        return False
    
    # Check for key concepts
    all_text = " ".join(clauses).lower()
    required_concepts = ["respectful", "spam", "python", "homework", "flair", "piracy"]
    
    found_count = sum(1 for concept in required_concepts if concept in all_text)
    
    if found_count >= 5:  # At least 5 out of 6 concepts should be present
        print(f"   ✅ Found {found_count}/{len(required_concepts)} expected concepts")
        return True
    else:
        print(f"   ❌ Only found {found_count}/{len(required_concepts)} expected concepts")
        return False


def test_real_world_discord_rules():
    """Test with real-world Discord-style server rules"""
    print("\n🧪 Test 1.6j: Real-world Discord rules extraction accuracy")
    
    text = """Discord Server Rules:
• Be respectful to everyone
• No NSFW content
• Don't spam or flood chat
• Use channels appropriately
• No advertising without permission
• Follow Discord's Terms of Service"""
    
    clauses = parse_rule_clauses(text)
    
    expected_min = 6
    print(f"   Expected: At least {expected_min} rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    if len(clauses) < expected_min:
        print(f"   ❌ Missed {expected_min - len(clauses)} rules")
        return False
    
    # Check for key concepts
    all_text = " ".join(clauses).lower()
    required_concepts = ["respectful", "nsfw", "spam", "channels", "advertising"]
    
    found_count = sum(1 for concept in required_concepts if concept in all_text)
    
    if found_count >= 4:  # At least 4 out of 5 concepts should be present
        print(f"   ✅ Found {found_count}/{len(required_concepts)} expected concepts")
        return True
    else:
        print(f"   ❌ Only found {found_count}/{len(required_concepts)} expected concepts")
        return False


def test_json_output_accuracy():
    """Test that complete JSON output maintains accuracy"""
    print("\n🧪 Test 1.6k: JSON output accuracy")
    
    text = """No harassment or bullying. Users must not post spam. 
All posts must be relevant to the community."""
    
    result = normalize_rules_to_json(text)
    
    # Check structure
    if "rules" not in result:
        print(f"   ❌ Missing 'rules' key in JSON output")
        return False
    
    rules = result["rules"]
    expected_min = 3
    
    print(f"   Expected: At least {expected_min} rules")
    print(f"   Extracted: {len(rules)} rules")
    
    if len(rules) < expected_min:
        print(f"   ❌ Too few rules in JSON output")
        return False
    
    # Check that each rule has all required fields
    for i, rule in enumerate(rules, 1):
        required_fields = ["id", "text", "category", "keywords"]
        missing_fields = [field for field in required_fields if field not in rule]
        
        if missing_fields:
            print(f"   ❌ Rule {i} missing fields: {', '.join(missing_fields)}")
            return False
    
    print(f"   ✅ All {len(rules)} rules have complete structure")
    
    # Check content accuracy
    all_text = " ".join(rule["text"] for rule in rules).lower()
    required_concepts = ["harassment", "spam", "relevant"]
    
    missing_concepts = [c for c in required_concepts if c not in all_text]
    
    if missing_concepts:
        print(f"   ❌ Missing concepts in JSON output: {', '.join(missing_concepts)}")
        return False
    else:
        print(f"   ✅ All expected concepts present in JSON output")
        return True


def test_extraction_consistency():
    """Test that extraction is consistent across multiple runs"""
    print("\n🧪 Test 1.6l: Extraction consistency")
    
    text = """No harassment. No spam. Be respectful."""
    
    # Extract multiple times
    results = [parse_rule_clauses(text) for _ in range(3)]
    
    # Check that all results are identical
    first_result = results[0]
    all_identical = all(result == first_result for result in results)
    
    if all_identical:
        print(f"   ✅ Extraction is consistent across multiple runs")
        print(f"   Extracted {len(first_result)} rules each time")
        return True
    else:
        print(f"   ❌ Extraction is inconsistent")
        for i, result in enumerate(results, 1):
            print(f"      Run {i}: {len(result)} rules")
        return False


def test_edge_case_very_long_rule():
    """Test accurate extraction of very long rules"""
    print("\n🧪 Test 1.6m: Very long rule extraction accuracy")
    
    text = """Users must not engage in any form of harassment, bullying, intimidation, 
threatening behavior, stalking, doxxing, or any other conduct that could reasonably 
be considered harmful, offensive, or inappropriate towards other community members, 
moderators, or any individuals mentioned in posts or comments."""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Extracted {len(clauses)} clause(s) from long rule")
    
    # Should extract at least 1 rule
    if len(clauses) < 1:
        print(f"   ❌ Failed to extract long rule")
        return False
    
    # Check that key concepts are preserved
    all_text = " ".join(clauses).lower()
    required_concepts = ["harassment", "bullying", "doxxing"]
    
    found_count = sum(1 for concept in required_concepts if concept in all_text)
    
    if found_count >= 2:
        print(f"   ✅ Long rule extracted with key concepts preserved")
        return True
    else:
        print(f"   ❌ Key concepts lost in extraction")
        return False


def test_edge_case_very_short_rules():
    """Test accurate extraction of very short rules"""
    print("\n🧪 Test 1.6n: Very short rule extraction accuracy")
    
    text = """No spam. Be nice. Stay on topic."""
    
    clauses = parse_rule_clauses(text)
    
    expected_count = 3
    print(f"   Expected: {expected_count} rules")
    print(f"   Extracted: {len(clauses)} rules")
    
    if len(clauses) != expected_count:
        print(f"   ❌ Count mismatch")
        return False
    
    # Check that short rules are preserved
    for i, clause in enumerate(clauses, 1):
        if len(clause) >= 5:  # Should have meaningful content
            print(f"   ✅ Rule {i}: '{clause}' (preserved)")
        else:
            print(f"   ❌ Rule {i}: '{clause}' (too short)")
            return False
    
    return True


def main():
    """Run all Task 1.6 tests"""
    print("=" * 70)
    print("Task 1.6: Unit Tests for Rule Extraction Accuracy")
    print("=" * 70)
    print("\nThis test suite validates that rules are correctly extracted from")
    print("various input formats with high accuracy, testing for:")
    print("  • Correct extraction from different formats")
    print("  • No false positives (non-rules not extracted)")
    print("  • No false negatives (actual rules not missed)")
    print("  • Edge cases handled properly")
    print("=" * 70)
    
    results = []
    
    # Run all tests
    results.append(("Numbered format accuracy", test_numbered_format_accuracy()))
    results.append(("Bulleted format accuracy", test_bulleted_format_accuracy()))
    results.append(("Paragraph format accuracy", test_paragraph_format_accuracy()))
    results.append(("Single rule accuracy", test_single_rule_accuracy()))
    results.append(("Empty input accuracy", test_empty_input_accuracy()))
    results.append(("Complex paragraph accuracy", test_complex_paragraph_accuracy()))
    results.append(("No false positives", test_no_false_positives()))
    results.append(("No false negatives", test_no_false_negatives()))
    results.append(("Reddit rules accuracy", test_real_world_reddit_rules()))
    results.append(("Discord rules accuracy", test_real_world_discord_rules()))
    results.append(("JSON output accuracy", test_json_output_accuracy()))
    results.append(("Extraction consistency", test_extraction_consistency()))
    results.append(("Very long rule accuracy", test_edge_case_very_long_rule()))
    results.append(("Very short rules accuracy", test_edge_case_very_short_rules()))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 TASK 1.6 TEST SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} tests passed")
    
    accuracy_percentage = (passed_count / total_count) * 100
    print(f"Accuracy: {accuracy_percentage:.1f}%")
    
    if passed_count == total_count:
        print("\n🎉 Task 1.6 COMPLETE: Rule extraction accuracy verified!")
        print("\nRule extraction is accurate for:")
        print("  ✓ Numbered lists (1., 2., 3.)")
        print("  ✓ Bulleted lists (-, *, •)")
        print("  ✓ Continuous paragraph text")
        print("  ✓ Complex mixed formats")
        print("  ✓ Real-world community guidelines (Reddit, Discord)")
        print("  ✓ Edge cases (empty, single, very long/short rules)")
        print("  ✓ No false positives (non-rules filtered out)")
        print("  ✓ No false negatives (all rules captured)")
        print("  ✓ Consistent extraction across multiple runs")
        print("  ✓ Complete JSON output with all fields")
    elif accuracy_percentage >= 80:
        print(f"\n✅ Task 1.6 MOSTLY COMPLETE: {accuracy_percentage:.1f}% accuracy")
        print(f"⚠️  {total_count - passed_count} test(s) failed - review for improvements")
    else:
        print(f"\n⚠️  Task 1.6 NEEDS WORK: Only {accuracy_percentage:.1f}% accuracy")
        print(f"❌ {total_count - passed_count} test(s) failed - significant improvements needed")
    
    return passed_count == total_count


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
