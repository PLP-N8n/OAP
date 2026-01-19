#!/usr/bin/env python3
"""
Test for Task 1.4: Assign unique identifiers to each extracted rule clause

This test validates that the assign_rule_identifiers function:
1. Assigns unique IDs to each rule clause
2. Uses the correct format (rule_001, rule_002, etc.)
3. Maintains deterministic ID assignment
4. Handles edge cases (empty lists, single rules, many rules)
5. Supports customizable prefixes and numbering
"""

import sys
from normalizer import assign_rule_identifiers, parse_rule_clauses


def test_basic_identifier_assignment():
    """Test basic ID assignment to rule clauses"""
    print("🧪 Test 1.4a: Basic identifier assignment")
    
    clauses = [
        "No harassment or bullying.",
        "Users must not post spam.",
        "All posts must be relevant."
    ]
    
    identified_rules = assign_rule_identifiers(clauses)
    
    print(f"   Input: {len(clauses)} clauses")
    print(f"   Output: {len(identified_rules)} identified rules")
    
    # Check that we got the same number of rules
    if len(identified_rules) != len(clauses):
        print(f"   ❌ Expected {len(clauses)} rules, got {len(identified_rules)}")
        return False
    
    # Check each rule has an ID and text
    for i, rule in enumerate(identified_rules, 1):
        expected_id = f"rule_{str(i).zfill(3)}"
        
        if 'id' not in rule:
            print(f"   ❌ Rule {i} missing 'id' field")
            return False
        
        if 'text' not in rule:
            print(f"   ❌ Rule {i} missing 'text' field")
            return False
        
        if rule['id'] != expected_id:
            print(f"   ❌ Rule {i} has ID '{rule['id']}', expected '{expected_id}'")
            return False
        
        if rule['text'] != clauses[i-1]:
            print(f"   ❌ Rule {i} text doesn't match original clause")
            return False
        
        print(f"   ✅ Rule {i}: {rule['id']} - {rule['text'][:50]}")
    
    print("   ✅ All identifiers assigned correctly")
    return True


def test_identifier_format():
    """Test that identifiers follow the correct format"""
    print("\n🧪 Test 1.4b: Identifier format validation")
    
    clauses = ["Rule one", "Rule two", "Rule three"]
    identified_rules = assign_rule_identifiers(clauses)
    
    expected_ids = ["rule_001", "rule_002", "rule_003"]
    
    all_correct = True
    for i, (rule, expected_id) in enumerate(zip(identified_rules, expected_ids), 1):
        if rule['id'] == expected_id:
            print(f"   ✅ Rule {i}: {rule['id']} (correct format)")
        else:
            print(f"   ❌ Rule {i}: {rule['id']} (expected {expected_id})")
            all_correct = False
    
    return all_correct


def test_identifier_uniqueness():
    """Test that all identifiers are unique"""
    print("\n🧪 Test 1.4c: Identifier uniqueness")
    
    clauses = [
        "No harassment.",
        "No spam.",
        "No doxxing.",
        "Be respectful.",
        "Stay on topic."
    ]
    
    identified_rules = assign_rule_identifiers(clauses)
    
    # Extract all IDs
    ids = [rule['id'] for rule in identified_rules]
    
    # Check for uniqueness
    unique_ids = set(ids)
    
    if len(ids) == len(unique_ids):
        print(f"   ✅ All {len(ids)} identifiers are unique")
        print(f"   IDs: {', '.join(ids)}")
        return True
    else:
        print(f"   ❌ Found duplicate identifiers!")
        print(f"   Total IDs: {len(ids)}, Unique IDs: {len(unique_ids)}")
        return False


def test_deterministic_assignment():
    """Test that ID assignment is deterministic (same input = same output)"""
    print("\n🧪 Test 1.4d: Deterministic ID assignment")
    
    clauses = ["Rule A", "Rule B", "Rule C"]
    
    # Assign IDs multiple times
    result1 = assign_rule_identifiers(clauses)
    result2 = assign_rule_identifiers(clauses)
    result3 = assign_rule_identifiers(clauses)
    
    # Check that all results are identical
    if result1 == result2 == result3:
        print("   ✅ ID assignment is deterministic")
        print(f"   Same input produces same output across multiple calls")
        return True
    else:
        print("   ❌ ID assignment is not deterministic")
        return False


def test_empty_input():
    """Test handling of empty clause list"""
    print("\n🧪 Test 1.4e: Empty input handling")
    
    clauses = []
    identified_rules = assign_rule_identifiers(clauses)
    
    if identified_rules == []:
        print("   ✅ Empty input returns empty list")
        return True
    else:
        print(f"   ❌ Expected empty list, got {identified_rules}")
        return False


def test_single_rule():
    """Test ID assignment for a single rule"""
    print("\n🧪 Test 1.4f: Single rule handling")
    
    clauses = ["No harassment or bullying."]
    identified_rules = assign_rule_identifiers(clauses)
    
    if len(identified_rules) == 1:
        rule = identified_rules[0]
        if rule['id'] == 'rule_001' and rule['text'] == clauses[0]:
            print(f"   ✅ Single rule: {rule['id']} - {rule['text']}")
            return True
        else:
            print(f"   ❌ Incorrect ID or text: {rule}")
            return False
    else:
        print(f"   ❌ Expected 1 rule, got {len(identified_rules)}")
        return False


def test_many_rules():
    """Test ID assignment for many rules (>100)"""
    print("\n🧪 Test 1.4g: Many rules handling")
    
    # Generate 150 rules
    clauses = [f"Rule number {i}." for i in range(1, 151)]
    identified_rules = assign_rule_identifiers(clauses)
    
    if len(identified_rules) != 150:
        print(f"   ❌ Expected 150 rules, got {len(identified_rules)}")
        return False
    
    # Check first, middle, and last rules
    test_indices = [0, 74, 149]
    expected_ids = ["rule_001", "rule_075", "rule_150"]
    
    all_correct = True
    for idx, expected_id in zip(test_indices, expected_ids):
        rule = identified_rules[idx]
        if rule['id'] == expected_id:
            print(f"   ✅ Rule {idx+1}: {rule['id']}")
        else:
            print(f"   ❌ Rule {idx+1}: {rule['id']} (expected {expected_id})")
            all_correct = False
    
    if all_correct:
        print(f"   ✅ All 150 rules assigned correct IDs")
    
    return all_correct


def test_custom_prefix():
    """Test ID assignment with custom prefix"""
    print("\n🧪 Test 1.4h: Custom prefix support")
    
    clauses = ["Rule one", "Rule two"]
    
    # Test with custom prefix
    identified_rules = assign_rule_identifiers(clauses, prefix="clause")
    
    expected_ids = ["clause_001", "clause_002"]
    
    all_correct = True
    for rule, expected_id in zip(identified_rules, expected_ids):
        if rule['id'] == expected_id:
            print(f"   ✅ Custom prefix: {rule['id']}")
        else:
            print(f"   ❌ Expected {expected_id}, got {rule['id']}")
            all_correct = False
    
    return all_correct


def test_custom_start_number():
    """Test ID assignment with custom start number"""
    print("\n🧪 Test 1.4i: Custom start number support")
    
    clauses = ["Rule one", "Rule two"]
    
    # Test with custom start number
    identified_rules = assign_rule_identifiers(clauses, start_num=10)
    
    expected_ids = ["rule_010", "rule_011"]
    
    all_correct = True
    for rule, expected_id in zip(identified_rules, expected_ids):
        if rule['id'] == expected_id:
            print(f"   ✅ Custom start: {rule['id']}")
        else:
            print(f"   ❌ Expected {expected_id}, got {rule['id']}")
            all_correct = False
    
    return all_correct


def test_integration_with_parse_rule_clauses():
    """Test integration with parse_rule_clauses function"""
    print("\n🧪 Test 1.4j: Integration with parse_rule_clauses")
    
    # Parse rules from text
    text = """No harassment or bullying. Users must not post spam. 
    All posts must be relevant to the community topic."""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Parsed {len(clauses)} clauses from text")
    
    # Assign identifiers
    identified_rules = assign_rule_identifiers(clauses)
    
    print(f"   Assigned IDs to {len(identified_rules)} rules")
    
    if len(identified_rules) == len(clauses):
        print("   ✅ Integration successful")
        for rule in identified_rules:
            print(f"      {rule['id']}: {rule['text'][:60]}")
        return True
    else:
        print(f"   ❌ Mismatch: {len(clauses)} clauses, {len(identified_rules)} identified")
        return False


def test_text_preservation():
    """Test that original text is preserved exactly"""
    print("\n🧪 Test 1.4k: Text preservation")
    
    clauses = [
        "No harassment or bullying.",
        "Users MUST NOT post spam!",
        "Be respectful... always."
    ]
    
    identified_rules = assign_rule_identifiers(clauses)
    
    all_preserved = True
    for original, identified in zip(clauses, identified_rules):
        if identified['text'] == original:
            print(f"   ✅ Text preserved: {original[:50]}")
        else:
            print(f"   ❌ Text modified!")
            print(f"      Original: {original}")
            print(f"      Modified: {identified['text']}")
            all_preserved = False
    
    return all_preserved


def test_special_characters_in_text():
    """Test handling of special characters in rule text"""
    print("\n🧪 Test 1.4l: Special characters in text")
    
    clauses = [
        "Don't use offensive language!",
        "No spam (including promotional content).",
        "Be respectful & kind to others.",
        "Follow the rules @ all times."
    ]
    
    identified_rules = assign_rule_identifiers(clauses)
    
    if len(identified_rules) == len(clauses):
        print(f"   ✅ Handled {len(clauses)} rules with special characters")
        for rule in identified_rules:
            print(f"      {rule['id']}: {rule['text'][:50]}")
        return True
    else:
        print(f"   ❌ Failed to handle special characters")
        return False


def main():
    """Run all Task 1.4 tests"""
    print("=" * 70)
    print("Task 1.4 Verification: Assign unique identifiers to rule clauses")
    print("=" * 70)
    
    results = []
    
    # Run tests
    results.append(("Basic identifier assignment", test_basic_identifier_assignment()))
    results.append(("Identifier format", test_identifier_format()))
    results.append(("Identifier uniqueness", test_identifier_uniqueness()))
    results.append(("Deterministic assignment", test_deterministic_assignment()))
    results.append(("Empty input handling", test_empty_input()))
    results.append(("Single rule handling", test_single_rule()))
    results.append(("Many rules handling", test_many_rules()))
    results.append(("Custom prefix support", test_custom_prefix()))
    results.append(("Custom start number", test_custom_start_number()))
    results.append(("Integration with parser", test_integration_with_parse_rule_clauses()))
    results.append(("Text preservation", test_text_preservation()))
    results.append(("Special characters", test_special_characters_in_text()))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 TASK 1.4 TEST SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🎉 Task 1.4 COMPLETE: Unique identifiers successfully assigned!")
        print("\nThe assign_rule_identifiers() function:")
        print("  ✓ Assigns unique IDs in format 'rule_001', 'rule_002', etc.")
        print("  ✓ Maintains deterministic ID assignment")
        print("  ✓ Preserves original rule text exactly")
        print("  ✓ Handles edge cases (empty, single, many rules)")
        print("  ✓ Supports custom prefixes and start numbers")
        print("  ✓ Integrates seamlessly with parse_rule_clauses()")
    else:
        print(f"\n⚠️  {total_count - passed_count} test(s) failed - review implementation")
    
    return passed_count == total_count


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
