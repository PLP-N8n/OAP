#!/usr/bin/env python3
"""
Property-Based Test for Task 1.7: Rule ingestion determinism.

Validates: Requirement 3.1 (Deterministic rule parsing and ingestion).
"""

import sys

try:
    from hypothesis import given, strategies as st, settings
    HYPOTHESIS_AVAILABLE = True
except ImportError:
    HYPOTHESIS_AVAILABLE = False

from normalizer import normalize_rules_to_json


def test_determinism_examples() -> bool:
    print("Test 1.7a: Determinism on sample inputs")
    samples = [
        "No harassment. No spam. No doxxing.",
        "1. Be respectful\n2. No spam\n3. Stay on topic",
        "- Rule one\n- Rule two\n- Rule three",
        "Users must not post spam. All content must be relevant.",
        "",
    ]

    all_passed = True
    for text in samples:
        result_a = normalize_rules_to_json(text)
        result_b = normalize_rules_to_json(text)
        if result_a != result_b:
            print(f"FAIL: Non-deterministic output for input: {repr(text)}")
            all_passed = False
        else:
            print(f"PASS: Deterministic output for input: {repr(text[:40])}")
    return all_passed


if HYPOTHESIS_AVAILABLE:

    @given(st.text(min_size=0, max_size=300))
    @settings(max_examples=30)
    def test_determinism_hypothesis(text: str) -> None:
        result_a = normalize_rules_to_json(text)
        result_b = normalize_rules_to_json(text)
        assert result_a == result_b, "Non-deterministic output detected"


def run_hypothesis() -> bool:
    print("\nTest 1.7b: Hypothesis-based determinism")
    try:
        test_determinism_hypothesis()
        print("PASS: Hypothesis determinism test")
        return True
    except Exception as exc:
        print(f"FAIL: Hypothesis determinism test failed: {exc}")
        return False


def main() -> int:
    print("=" * 70)
    print("Task 1.7 - Rule Ingestion Determinism")
    print("=" * 70)

    results = [test_determinism_examples()]
    if HYPOTHESIS_AVAILABLE:
        results.append(run_hypothesis())
    else:
        print("Hypothesis not installed; skipping randomized test.")

    if all(results):
        print("\nALL TESTS PASSED")
        return 0

    print("\nTESTS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
