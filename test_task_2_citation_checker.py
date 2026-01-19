#!/usr/bin/env python3
"""
Tests for Step 2: Citation Anchoring Engine.

Covers tasks:
- 2.11 Citation anchoring completeness
- 2.12 Citation text accuracy
- 2.13 Edge cases
- 2.14 Unsupported statements flagged
- 2.15 Real-world comment examples
"""

import sys

from citation_checker import adjudicate_comment


RULES_JSON = {
    "rules": [
        {
            "id": "rule_001",
            "text": "No harassment or bullying.",
            "category": "harassment",
            "keywords": ["harassment", "bullying", "idiot", "loser"],
        },
        {
            "id": "rule_002",
            "text": "No spam or promotional content.",
            "category": "spam",
            "keywords": ["spam", "promotional", "discount", "promo"],
        },
        {
            "id": "rule_003",
            "text": "Do not share personal information about others.",
            "category": "doxxing",
            "keywords": ["personal information", "address", "phone number"],
        },
    ]
}


def assert_citation_complete(result: dict, rules_json: dict) -> bool:
    if result.get("verdict") != "Violation":
        return False
    anchor = result.get("citation_anchor") or {}
    if not anchor.get("rule_id") or not anchor.get("quoted_rule_text"):
        return False
    rule_lookup = {rule["id"]: rule["text"] for rule in rules_json["rules"]}
    return anchor["quoted_rule_text"] == rule_lookup.get(anchor["rule_id"])


def test_exact_match() -> bool:
    print("Test 2.6/2.7: Exact match violation")
    comment = "This is spam. Use my promo code for a discount."
    result = adjudicate_comment(comment, RULES_JSON, exact_threshold=0.2)
    if result.get("verdict") != "Violation":
        print("FAIL: Expected violation for spam content")
        return False
    if not assert_citation_complete(result, RULES_JSON):
        print("FAIL: Citation anchor missing or incorrect")
        return False
    print("PASS: Exact match violation anchored")
    return True


def test_semantic_match() -> bool:
    print("Test 2.3: Semantic similarity violation")
    rules = {
        "rules": [
            {
                "id": "rule_sem",
                "text": "Do not post personal information about others.",
                "category": "doxxing",
                "keywords": [],
            }
        ]
    }
    comment = "Posting personal info like a phone number is not ok."
    result = adjudicate_comment(comment, rules, semantic_threshold=0.1)
    if result.get("verdict") != "Violation":
        print("FAIL: Expected violation via semantic match")
        return False
    if not assert_citation_complete(result, rules):
        print("FAIL: Citation anchor missing or incorrect")
        return False
    print("PASS: Semantic match violation anchored")
    return True


def test_no_violation() -> bool:
    print("Test 2.9: No violation output when no rules match")
    comment = "I disagree with your technical analysis."
    result = adjudicate_comment(comment, RULES_JSON)
    if result.get("verdict") != "No Violation":
        print("FAIL: Expected no violation")
        return False
    if "NO_APPLICABLE_RULE" not in result.get("flags", []):
        print("FAIL: Expected NO_APPLICABLE_RULE flag")
        return False
    print("PASS: No violation correctly returned")
    return True


def test_edge_cases() -> bool:
    print("Test 2.13/2.14: Edge cases and unsupported statements")
    result = adjudicate_comment("", RULES_JSON)
    if result.get("verdict") != "No Violation" or "EMPTY_COMMENT" not in result.get("flags", []):
        print("FAIL: Empty comment should be flagged")
        return False
    result = adjudicate_comment("Hello world", {"rules": []})
    if result.get("verdict") != "No Violation" or "NO_RULES" not in result.get("flags", []):
        print("FAIL: Missing rules should be flagged")
        return False
    print("PASS: Edge cases handled")
    return True


def test_real_world_examples() -> bool:
    print("Test 2.15: Real-world comment examples")
    comment = "You're such an idiot, John Smith from 123 Main Street should shut up"
    result = adjudicate_comment(comment, RULES_JSON, exact_threshold=0.2)
    if result.get("verdict") != "Violation":
        print("FAIL: Expected violation for harassment/doxxing example")
        return False
    if not assert_citation_complete(result, RULES_JSON):
        print("FAIL: Citation anchor missing or incorrect")
        return False
    print("PASS: Real-world example anchored")
    return True


def main() -> int:
    print("=" * 70)
    print("Step 2 - Citation Anchoring Tests")
    print("=" * 70)
    tests = [
        test_exact_match(),
        test_semantic_match(),
        test_no_violation(),
        test_edge_cases(),
        test_real_world_examples(),
    ]
    if all(tests):
        print("\nALL TESTS PASSED")
        return 0
    print("\nTESTS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
