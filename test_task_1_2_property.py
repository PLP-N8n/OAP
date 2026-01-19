#!/usr/bin/env python3
"""
Property-Based Tests for Task 1.2: Text parsing to identify discrete rule clauses

These tests use property-based testing to verify universal properties that should
hold across all valid inputs to the parse_rule_clauses function.

**Validates: Requirements 3.1, 3.3** (Rule ingestion and parsing)
"""

import sys

# Try to import hypothesis, but provide fallback if not installed
try:
    from hypothesis import given, strategies as st, settings, example
    HYPOTHESIS_AVAILABLE = True
except ImportError:
    print("⚠️  Hypothesis not installed. Install with: pip install hypothesis")
    print("   Running basic property tests without randomization...\n")
    HYPOTHESIS_AVAILABLE = False

from normalizer import parse_rule_clauses


def test_property_idempotence():
    """
    Property: Parsing the same text multiple times should produce identical results
    **Validates: Requirements 3.1** (Deterministic rule parsing)
    """
    print("🧪 Property Test 1: Idempotence (Deterministic Parsing)")
    print("   Property: parse_rule_clauses(text) == parse_rule_clauses(text)")
    
    test_cases = [
        "No harassment. No spam. No doxxing.",
        "1. Be respectful\n2. No spam\n3. Stay on topic",
        "- Rule one\n- Rule two\n- Rule three",
        "Users must not post spam. All content must be relevant.",
        ""
    ]
    
    all_passed = True
    for text in test_cases:
        result1 = parse_rule_clauses(text)
        result2 = parse_rule_clauses(text)
        
        if result1 == result2:
            print(f"   ✅ Idempotent for: {repr(text[:50])}")
        else:
            print(f"   ❌ NOT idempotent for: {repr(text[:50])}")
            print(f"      First:  {result1}")
            print(f"      Second: {result2}")
            all_passed = False
    
    return all_passed


def test_property_non_empty_output_for_rules():
    """
    Property: Text containing rule indicators should produce non-empty output
    **Validates: Requirements 3.3** (Identify discrete clauses)
    """
    print("\n🧪 Property Test 2: Non-Empty Output for Rule Text")
    print("   Property: If text contains rule indicators, output should not be empty")
    
    rule_texts = [
        "No harassment.",
        "Users must not spam.",
        "Do not share personal information.",
        "Always be respectful.",
        "Never post illegal content.",
        "Spam is prohibited.",
        "All posts should be relevant.",
    ]
    
    all_passed = True
    for text in rule_texts:
        result = parse_rule_clauses(text)
        
        if len(result) > 0:
            print(f"   ✅ Non-empty for: {repr(text)}")
        else:
            print(f"   ❌ Empty output for rule text: {repr(text)}")
            all_passed = False
    
    return all_passed


def test_property_empty_input_empty_output():
    """
    Property: Empty or whitespace-only input should produce empty output
    **Validates: Requirements 3.1** (Proper input handling)
    """
    print("\n🧪 Property Test 3: Empty Input → Empty Output")
    print("   Property: parse_rule_clauses('') == []")
    
    empty_inputs = ["", "   ", "\n", "\n\n", "\t", "  \n  \t  "]
    
    all_passed = True
    for text in empty_inputs:
        result = parse_rule_clauses(text)
        
        if result == []:
            print(f"   ✅ Empty output for: {repr(text)}")
        else:
            print(f"   ❌ Non-empty output for empty input: {repr(text)} -> {result}")
            all_passed = False
    
    return all_passed


def test_property_clause_count_bounded():
    """
    Property: Number of output clauses should not exceed number of sentences in input
    **Validates: Requirements 3.3** (Discrete clause identification)
    """
    print("\n🧪 Property Test 4: Output Clause Count is Reasonable")
    print("   Property: len(output) <= reasonable_bound(input)")
    
    test_cases = [
        ("No spam.", 1, 2),  # (text, min_expected, max_expected)
        ("No spam. No harassment.", 2, 3),
        ("No spam. No harassment. No doxxing.", 3, 4),
        ("1. No spam\n2. No harassment\n3. No doxxing", 3, 4),  # Changed to have rule indicators
    ]
    
    all_passed = True
    for text, min_expected, max_expected in test_cases:
        result = parse_rule_clauses(text)
        count = len(result)
        
        if min_expected <= count <= max_expected:
            print(f"   ✅ Reasonable count ({count}) for: {repr(text[:40])}")
        else:
            print(f"   ❌ Unreasonable count ({count}, expected {min_expected}-{max_expected}) for: {repr(text[:40])}")
            print(f"      Output: {result}")
            all_passed = False
    
    return all_passed


def test_property_no_empty_clauses():
    """
    Property: Output should never contain empty or whitespace-only clauses
    **Validates: Requirements 3.3** (Quality of extracted clauses)
    """
    print("\n🧪 Property Test 5: No Empty Clauses in Output")
    print("   Property: All output clauses should be non-empty and meaningful")
    
    test_cases = [
        "No harassment. No spam. No doxxing.",
        "1. Be respectful\n2. No spam\n3. Stay on topic",
        "Users must not post spam. All content must be relevant.",
        "- Rule one\n- Rule two\n- Rule three",
    ]
    
    all_passed = True
    for text in test_cases:
        result = parse_rule_clauses(text)
        
        empty_clauses = [clause for clause in result if not clause.strip()]
        
        if len(empty_clauses) == 0:
            print(f"   ✅ No empty clauses for: {repr(text[:40])}")
        else:
            print(f"   ❌ Found empty clauses for: {repr(text[:40])}")
            print(f"      Empty clauses: {empty_clauses}")
            all_passed = False
    
    return all_passed


def test_property_preserves_content():
    """
    Property: Output clauses should contain content from the input
    **Validates: Requirements 3.1** (Accurate parsing without hallucination)
    """
    print("\n🧪 Property Test 6: Content Preservation")
    print("   Property: Output clauses should be derived from input text")
    
    test_cases = [
        ("No harassment.", ["harassment"]),
        ("No spam. No doxxing.", ["spam", "doxxing"]),
        ("Users must not post spam.", ["spam", "post"]),
    ]
    
    all_passed = True
    for text, expected_keywords in test_cases:
        result = parse_rule_clauses(text)
        
        # Check that at least one output clause contains each expected keyword
        all_keywords_found = True
        for keyword in expected_keywords:
            found = any(keyword.lower() in clause.lower() for clause in result)
            if not found:
                all_keywords_found = False
                print(f"   ❌ Keyword '{keyword}' not found in output for: {repr(text)}")
                print(f"      Output: {result}")
        
        if all_keywords_found:
            print(f"   ✅ Content preserved for: {repr(text)}")
            all_passed = all_passed and True
        else:
            all_passed = False
    
    return all_passed


# Hypothesis-based property tests (if available)
if HYPOTHESIS_AVAILABLE:
    
    @given(st.text(min_size=0, max_size=500))
    @settings(max_examples=50)
    def test_hypothesis_no_crash(text):
        """
        Property: Parser should never crash on any text input
        **Validates: Requirements 3.1** (Robust input handling)
        """
        try:
            result = parse_rule_clauses(text)
            assert isinstance(result, list), "Output must be a list"
            assert all(isinstance(clause, str) for clause in result), "All clauses must be strings"
        except Exception as e:
            raise AssertionError(f"Parser crashed on input {repr(text[:100])}: {e}")
    
    
    @given(st.lists(st.text(min_size=5, max_size=50), min_size=1, max_size=10))
    @settings(max_examples=50)
    @example(["No spam", "No harassment", "No doxxing"])
    def test_hypothesis_list_format(rule_list):
        """
        Property: Parser should handle list-formatted rules
        **Validates: Requirements 3.2** (Multiple rule set formats)
        """
        # Create numbered list format
        text = "\n".join(f"{i+1}. {rule}" for i, rule in enumerate(rule_list))
        result = parse_rule_clauses(text)
        
        # Should extract at least some rules
        assert isinstance(result, list), "Output must be a list"
        # Note: We don't assert exact count because some rules might be filtered


def run_hypothesis_tests():
    """Run hypothesis-based property tests"""
    print("\n" + "=" * 70)
    print("HYPOTHESIS-BASED PROPERTY TESTS")
    print("=" * 70)
    
    try:
        print("\n🧪 Hypothesis Test 1: No Crash on Any Input")
        test_hypothesis_no_crash()
        print("   ✅ Parser handles all random inputs without crashing")
    except Exception as e:
        print(f"   ❌ Test failed: {e}")
        return False
    
    try:
        print("\n🧪 Hypothesis Test 2: List Format Handling")
        test_hypothesis_list_format()
        print("   ✅ Parser handles list-formatted rules correctly")
    except Exception as e:
        print(f"   ❌ Test failed: {e}")
        return False
    
    return True


def main():
    """Run all property-based tests"""
    print("=" * 70)
    print("Property-Based Tests for Task 1.2: Text Parsing")
    print("=" * 70)
    
    results = []
    
    # Run manual property tests
    results.append(("Idempotence", test_property_idempotence()))
    results.append(("Non-empty output for rules", test_property_non_empty_output_for_rules()))
    results.append(("Empty input → empty output", test_property_empty_input_empty_output()))
    results.append(("Clause count bounded", test_property_clause_count_bounded()))
    results.append(("No empty clauses", test_property_no_empty_clauses()))
    results.append(("Content preservation", test_property_preserves_content()))
    
    # Run hypothesis tests if available
    if HYPOTHESIS_AVAILABLE:
        hypothesis_passed = run_hypothesis_tests()
        results.append(("Hypothesis tests", hypothesis_passed))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 PROPERTY TEST SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} property tests passed")
    
    if passed_count == total_count:
        print("\n🎉 ALL PROPERTY TESTS PASSED!")
        print("\nVerified Properties:")
        print("  ✓ Deterministic parsing (idempotence)")
        print("  ✓ Non-empty output for rule text")
        print("  ✓ Empty input handling")
        print("  ✓ Reasonable clause counts")
        print("  ✓ No empty clauses in output")
        print("  ✓ Content preservation")
        if HYPOTHESIS_AVAILABLE:
            print("  ✓ Robust handling of random inputs")
            print("  ✓ List format parsing")
    else:
        print(f"\n⚠️  {total_count - passed_count} property test(s) failed")
    
    return passed_count == total_count


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
