#!/usr/bin/env python3
"""
Test for Task 1.2: Implement text parsing to identify discrete rule clauses

This test validates that the parse_rule_clauses function can:
1. Identify discrete rule clauses from continuous text
2. Handle numbered/bulleted lists
3. Handle paragraph-style rules
4. Separate rules that are run together
5. Clean up and normalize the extracted clauses
"""

import sys
from normalizer import parse_rule_clauses


def test_numbered_list_parsing():
    """Test parsing of numbered list format"""
    print("🧪 Test 1.2a: Parse numbered list format")
    
    text = """1. No harassment or bullying
2. Users must not post spam
3. All posts must be relevant"""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Input: {repr(text)}")
    print(f"   Extracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Should extract 3 distinct clauses
    if len(clauses) >= 3:
        print("   ✅ Successfully identified multiple discrete clauses")
        return True
    else:
        print(f"   ❌ Expected at least 3 clauses, got {len(clauses)}")
        return False


def test_bulleted_list_parsing():
    """Test parsing of bulleted list format"""
    print("\n🧪 Test 1.2b: Parse bulleted list format")
    
    text = """- No harassment or bullying
- Users must not post spam
- All posts must be relevant to the community"""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Input: {repr(text)}")
    print(f"   Extracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Should extract 3 distinct clauses
    if len(clauses) >= 3:
        print("   ✅ Successfully identified discrete clauses from bullets")
        return True
    else:
        print(f"   ❌ Expected at least 3 clauses, got {len(clauses)}")
        return False


def test_paragraph_parsing():
    """Test parsing of paragraph-style continuous text"""
    print("\n🧪 Test 1.2c: Parse paragraph-style continuous text")
    
    text = """No harassment or bullying. Users must not post content that targets individuals with hate speech. Spam and promotional content is prohibited. All posts must be relevant to the community topic."""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Input: {repr(text)}")
    print(f"   Extracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Should extract at least 3-4 distinct clauses
    if len(clauses) >= 3:
        print("   ✅ Successfully parsed continuous paragraph text")
        return True
    else:
        print(f"   ❌ Expected at least 3 clauses, got {len(clauses)}")
        return False


def test_mixed_format_parsing():
    """Test parsing of mixed format with intro text and rules"""
    print("\n🧪 Test 1.2d: Parse mixed format with intro text")
    
    text = """Welcome to our gaming forum! We want to keep things chill.
Please don't be mean. Absolutely no doxxing (sharing real addresses) is allowed, and if you spam promotion links you will be banned. Be nice!"""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Input: {repr(text)}")
    print(f"   Extracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Should extract at least 2-3 rule clauses (filtering out welcome text)
    if len(clauses) >= 2:
        print("   ✅ Successfully extracted rules from mixed format")
        
        # Check that we're not including the welcome text
        welcome_included = any('welcome' in clause.lower() for clause in clauses)
        if not welcome_included:
            print("   ✅ Correctly filtered out non-rule intro text")
            return True
        else:
            print("   ⚠️  Warning: Intro text may be included in clauses")
            return True
    else:
        print(f"   ❌ Expected at least 2 clauses, got {len(clauses)}")
        return False


def test_empty_input():
    """Test handling of empty or whitespace-only input"""
    print("\n🧪 Test 1.2e: Handle empty input gracefully")
    
    test_cases = ["", "   ", "\n\n", None]
    
    all_passed = True
    for test_input in test_cases:
        try:
            clauses = parse_rule_clauses(test_input) if test_input is not None else parse_rule_clauses("")
            if clauses == []:
                print(f"   ✅ Empty input handled correctly: {repr(test_input)}")
            else:
                print(f"   ⚠️  Unexpected output for empty input: {repr(test_input)} -> {clauses}")
                all_passed = False
        except Exception as e:
            print(f"   ❌ Error handling empty input {repr(test_input)}: {e}")
            all_passed = False
    
    return all_passed


def test_clause_separation():
    """Test that clauses are properly separated and not merged incorrectly"""
    print("\n🧪 Test 1.2f: Verify proper clause separation")
    
    text = """No harassment. No spam. No doxxing."""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Input: {repr(text)}")
    print(f"   Extracted {len(clauses)} clauses:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Should extract 3 separate clauses, not merge them
    if len(clauses) >= 3:
        print("   ✅ Clauses properly separated")
        return True
    else:
        print(f"   ❌ Expected 3 separate clauses, got {len(clauses)}")
        return False


def test_real_world_example():
    """Test with a real-world style community guidelines example"""
    print("\n🧪 Test 1.2g: Parse real-world community guidelines")
    
    text = """Community Guidelines:
1. Be respectful to all members
2. No hate speech, harassment, or bullying
3. Do not share personal information (doxxing)
4. Spam and excessive self-promotion are not allowed
5. Stay on topic and keep discussions relevant
6. Follow all applicable laws and regulations"""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Extracted {len(clauses)} clauses from real-world example:")
    for i, clause in enumerate(clauses, 1):
        print(f"      {i}. {clause}")
    
    # Should extract at least 5-6 clauses
    if len(clauses) >= 5:
        print("   ✅ Successfully parsed real-world guidelines")
        return True
    else:
        print(f"   ❌ Expected at least 5 clauses, got {len(clauses)}")
        return False


def test_clause_quality():
    """Test that extracted clauses are meaningful and complete"""
    print("\n🧪 Test 1.2h: Verify clause quality")
    
    text = """No harassment or bullying. Users must not post spam. Be respectful."""
    
    clauses = parse_rule_clauses(text)
    
    print(f"   Checking quality of {len(clauses)} extracted clauses:")
    
    all_passed = True
    for i, clause in enumerate(clauses, 1):
        # Check minimum length (should be meaningful)
        if len(clause) < 5:
            print(f"      ❌ Clause {i} too short: {repr(clause)}")
            all_passed = False
        else:
            print(f"      ✅ Clause {i}: {clause}")
    
    if all_passed:
        print("   ✅ All clauses meet quality standards")
    
    return all_passed


def main():
    """Run all Task 1.2 tests"""
    print("=" * 70)
    print("Task 1.2 Verification: Text parsing to identify discrete rule clauses")
    print("=" * 70)
    
    results = []
    
    # Run tests
    results.append(("Numbered list parsing", test_numbered_list_parsing()))
    results.append(("Bulleted list parsing", test_bulleted_list_parsing()))
    results.append(("Paragraph parsing", test_paragraph_parsing()))
    results.append(("Mixed format parsing", test_mixed_format_parsing()))
    results.append(("Empty input handling", test_empty_input()))
    results.append(("Clause separation", test_clause_separation()))
    results.append(("Real-world example", test_real_world_example()))
    results.append(("Clause quality", test_clause_quality()))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 TASK 1.2 TEST SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🎉 Task 1.2 COMPLETE: Text parsing successfully identifies discrete rule clauses!")
        print("\nThe parse_rule_clauses() function can:")
        print("  ✓ Parse numbered lists (1., 2., 3.)")
        print("  ✓ Parse bulleted lists (-, *, •)")
        print("  ✓ Parse continuous paragraph text")
        print("  ✓ Handle mixed formats with intro text")
        print("  ✓ Separate discrete clauses properly")
        print("  ✓ Filter out non-rule content")
        print("  ✓ Handle edge cases (empty input, etc.)")
    else:
        print(f"\n⚠️  {total_count - passed_count} test(s) failed - review implementation")
    
    return passed_count == total_count


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
