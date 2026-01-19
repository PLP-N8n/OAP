#!/usr/bin/env python3
"""
Simple test script for the Open Adjudication Protocol MVP
Tests the core citation anchoring functionality
"""

import json
from normalizer import normalize_rules, adjudicate_dispute

def test_rule_normalization():
    """Test that rules are properly normalized into structured format"""
    print("🧪 Testing Rule Normalization...")
    
    raw_rules = """No harassment or bullying. 
    Users must not post spam or promotional content. 
    All posts must be relevant to the community."""
    
    try:
        normalized = normalize_rules(raw_rules)
        
        # Check structure
        assert 'rules' in normalized, "Missing 'rules' key in output"
        assert len(normalized['rules']) > 0, "No rules extracted"
        
        # Check each rule has required fields
        for rule in normalized['rules']:
            assert 'id' in rule, f"Rule missing 'id': {rule}"
            assert 'text' in rule, f"Rule missing 'text': {rule}"
            
        print(f"✅ Successfully normalized {len(normalized['rules'])} rules")
        return normalized
        
    except Exception as e:
        print(f"❌ Rule normalization failed: {e}")
        return None

def test_citation_anchoring(normalized_rules):
    """Test that violations are properly anchored to specific rules"""
    print("\n🧪 Testing Citation Anchoring...")
    
    test_cases = [
        {
            "comment": "You're such an idiot and a loser!",
            "should_violate": True,
            "description": "Clear harassment"
        },
        {
            "comment": "Check out my amazing product at mysite.com!",
            "should_violate": True,
            "description": "Promotional spam"
        },
        {
            "comment": "I disagree with your technical analysis.",
            "should_violate": False,
            "description": "Respectful disagreement"
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n  Test {i}: {test_case['description']}")
        print(f"  Comment: '{test_case['comment']}'")
        
        try:
            verdict = adjudicate_dispute(test_case['comment'], normalized_rules)
            
            # Check structure
            assert 'verdict' in verdict, "Missing 'verdict' in output"
            
            is_violation = verdict['verdict'] == 'Violation'
            expected = test_case['should_violate']
            
            if is_violation == expected:
                print(f"  ✅ Correct verdict: {verdict['verdict']}")
                if is_violation and 'citation_anchor' in verdict:
                    anchor = verdict['citation_anchor']
                    print(f"  📎 Cited rule: {anchor.get('quoted_rule_text', 'N/A')}")
            else:
                print(f"  ❌ Wrong verdict: Expected {'Violation' if expected else 'No Violation'}, got {verdict['verdict']}")
            
            results.append({
                'test': test_case['description'],
                'correct': is_violation == expected,
                'verdict': verdict
            })
            
        except Exception as e:
            print(f"  ❌ Test failed with error: {e}")
            results.append({
                'test': test_case['description'],
                'correct': False,
                'error': str(e)
            })
    
    return results

def test_citation_completeness(normalized_rules):
    """Test that all violations have proper citations"""
    print("\n🧪 Testing Citation Completeness...")
    
    violation_comment = "You're a complete moron and should go die!"
    
    try:
        verdict = adjudicate_dispute(violation_comment, normalized_rules)
        
        if verdict.get('verdict') == 'Violation':
            # Must have citation anchor
            assert 'citation_anchor' in verdict, "Violation missing citation_anchor"
            
            anchor = verdict['citation_anchor']
            assert 'rule_id' in anchor, "Citation missing rule_id"
            assert 'quoted_rule_text' in anchor, "Citation missing quoted_rule_text"
            
            # Quoted text should not be empty
            quoted_text = anchor.get('quoted_rule_text', '').strip()
            assert quoted_text, "Citation has empty quoted_rule_text"
            
            print(f"✅ Citation completeness verified")
            print(f"   Rule ID: {anchor.get('rule_id')}")
            print(f"   Quoted text: '{quoted_text}'")
            
            return True
        else:
            print("ℹ️  No violation detected, citation completeness not applicable")
            return True
            
    except Exception as e:
        print(f"❌ Citation completeness test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Open Adjudication Protocol - MVP Test Suite")
    print("=" * 50)
    
    # Test 1: Rule Normalization
    normalized_rules = test_rule_normalization()
    if not normalized_rules:
        print("\n❌ Cannot proceed - rule normalization failed")
        return
    
    # Test 2: Citation Anchoring
    anchoring_results = test_citation_anchoring(normalized_rules)
    
    # Test 3: Citation Completeness
    completeness_passed = test_citation_completeness(normalized_rules)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    
    correct_count = sum(1 for r in anchoring_results if r.get('correct', False))
    total_count = len(anchoring_results)
    
    print(f"Rule Normalization: ✅ PASSED")
    print(f"Citation Anchoring: {correct_count}/{total_count} tests passed")
    print(f"Citation Completeness: {'✅ PASSED' if completeness_passed else '❌ FAILED'}")
    
    if correct_count == total_count and completeness_passed:
        print("\n🎉 ALL TESTS PASSED - MVP is working correctly!")
    else:
        print("\n⚠️  Some tests failed - check implementation")

if __name__ == "__main__":
    main()