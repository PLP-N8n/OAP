#!/usr/bin/env python3
"""
Tests for Task 1.8 and 1.9:
- Validate parsing across multiple rule formats.
- Validate JSON output structure consistency.
"""

import json
import os
import sys

from normalizer import normalize_rules_to_json


def _load_example(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def _validate_structure(result: dict) -> bool:
    if "rules" not in result or not isinstance(result["rules"], list):
        return False
    for rule in result["rules"]:
        if not isinstance(rule, dict):
            return False
        for key in ("id", "text", "category", "keywords"):
            if key not in rule:
                return False
        if not isinstance(rule["keywords"], list):
            return False
    return True


def test_formats() -> bool:
    print("Test 1.8: Multiple rule formats")
    repo_root = os.path.dirname(__file__)
    reddit_rules = _load_example(os.path.join(repo_root, "examples", "reddit_rules.txt"))

    discord_rules = """1. Be respectful to everyone
2. No NSFW content
3. Do not spam or flood chat
4. Use channels appropriately
5. No advertising without permission
6. Follow the platform terms of service"""

    paragraph_rules = (
        "Welcome to the community. No harassment or bullying. "
        "Users must not post personal information. Spam is prohibited."
    )

    samples = {
        "reddit": reddit_rules,
        "discord": discord_rules,
        "paragraph": paragraph_rules,
    }

    all_passed = True
    for name, text in samples.items():
        result = normalize_rules_to_json(text)
        if not result.get("rules"):
            print(f"FAIL: No rules extracted for {name}")
            all_passed = False
            continue
        if not _validate_structure(result):
            print(f"FAIL: Invalid JSON structure for {name}")
            all_passed = False
            continue
        print(f"PASS: Extracted {len(result['rules'])} rules for {name}")
    return all_passed


def main() -> int:
    print("=" * 70)
    print("Task 1.8/1.9 - Formats and JSON Structure")
    print("=" * 70)
    if test_formats():
        print("\nALL TESTS PASSED")
        return 0
    print("\nTESTS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
