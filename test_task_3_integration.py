#!/usr/bin/env python3
"""
Integration tests for Step 3 (end-to-end workflow).

Covers:
- 3.17 End-to-end workflow validation
- 3.18 Real community guidelines test
- 3.19 Error handling for malformed inputs
"""

import os
import sys

from citation_checker import adjudicate_comment
from normalizer import normalize_rules_to_json


def test_end_to_end() -> bool:
    print("Test 3.17: End-to-end workflow")
    raw_rules = "No harassment. No spam. No doxxing."
    rules_json = normalize_rules_to_json(raw_rules)
    comment = "This is spam. Buy now."
    result = adjudicate_comment(comment, rules_json)
    if result.get("verdict") != "Violation":
        print("FAIL: Expected violation for spam content")
        return False
    if not result.get("citation_anchor"):
        print("FAIL: Missing citation anchor")
        return False
    print("PASS: End-to-end workflow")
    return True


def test_real_guidelines() -> bool:
    print("Test 3.18: Real-world guidelines")
    repo_root = os.path.dirname(__file__)
    rules_path = os.path.join(repo_root, "examples", "reddit_rules.txt")
    with open(rules_path, "r", encoding="utf-8") as handle:
        raw_rules = handle.read()
    rules_json = normalize_rules_to_json(raw_rules)
    comment = "Check out my affiliate link. This is spam."
    result = adjudicate_comment(comment, rules_json)
    if result.get("verdict") != "Violation":
        print("FAIL: Expected violation for spam example")
        return False
    print("PASS: Real-world guidelines")
    return True


def test_error_handling() -> bool:
    print("Test 3.19: Error handling for malformed inputs")
    result = adjudicate_comment("Hello", None)
    if result.get("verdict") != "No Violation" or "NO_RULES" not in result.get("flags", []):
        print("FAIL: Expected NO_RULES flag for missing rules")
        return False
    result = adjudicate_comment("", {"rules": []})
    if result.get("verdict") != "No Violation" or "EMPTY_COMMENT" not in result.get("flags", []):
        print("FAIL: Expected EMPTY_COMMENT flag for blank input")
        return False
    print("PASS: Error handling")
    return True


def main() -> int:
    print("=" * 70)
    print("Step 3 - Integration Tests")
    print("=" * 70)
    tests = [test_end_to_end(), test_real_guidelines(), test_error_handling()]
    if all(tests):
        print("\nALL TESTS PASSED")
        return 0
    print("\nTESTS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
