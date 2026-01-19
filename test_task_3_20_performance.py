#!/usr/bin/env python3
"""
Performance check for Step 3.20: Large rule set handling.
"""

import sys
import time

from citation_checker import adjudicate_comment
from normalizer import normalize_rules_to_json


def test_large_rule_set() -> bool:
    print("Test 3.20: Large rule set performance")
    raw_rules = "\n".join(f"{i}. No harassment or bullying rule {i}." for i in range(1, 501))
    start = time.perf_counter()
    rules_json = normalize_rules_to_json(raw_rules)
    normalize_time = time.perf_counter() - start

    comment = "This is harassment and bullying."
    start = time.perf_counter()
    result = adjudicate_comment(comment, rules_json)
    adjudicate_time = time.perf_counter() - start

    if result.get("verdict") != "Violation":
        print("FAIL: Expected violation for spam content")
        return False

    print(f"Normalization time: {normalize_time:.3f}s")
    print(f"Adjudication time: {adjudicate_time:.3f}s")
    return True


def main() -> int:
    print("=" * 70)
    print("Step 3 - Performance Test")
    print("=" * 70)
    if test_large_rule_set():
        print("\nPERFORMANCE TEST PASSED")
        return 0
    print("\nPERFORMANCE TEST FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
