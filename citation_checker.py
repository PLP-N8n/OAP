import argparse
import json
import math
import os
import re
from typing import Any, Dict, List, Optional, Tuple

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

from normalizer import normalize_rules_to_json


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "has", "he", "in", "is", "it", "its", "of", "on", "or", "that", "the",
    "to", "was", "were", "will", "with", "you", "your"
}


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def _tokenize(text: str) -> List[str]:
    tokens = re.split(r"[^a-z0-9]+", _normalize_text(text))
    return [token for token in tokens if token and token not in STOPWORDS]


def _get_rule_keywords(rule: Dict[str, Any]) -> List[str]:
    keywords = rule.get("keywords") or []
    if not isinstance(keywords, list):
        return []
    return [str(keyword).strip() for keyword in keywords if str(keyword).strip()]


def _exact_match_score(comment: str, rule: Dict[str, Any]) -> Tuple[float, List[str]]:
    comment_lower = _normalize_text(comment)
    keywords = _get_rule_keywords(rule)
    matched_keywords = [kw for kw in keywords if _normalize_text(kw) in comment_lower]

    if keywords:
        score = min(1.0, len(matched_keywords) / max(1, len(keywords)))
        return score, matched_keywords

    rule_tokens = set(_tokenize(rule.get("text", "")))
    comment_tokens = set(_tokenize(comment))
    if not rule_tokens:
        return 0.0, []
    overlap = rule_tokens.intersection(comment_tokens)
    score = len(overlap) / max(1, len(rule_tokens))
    return score, list(overlap)


def _semantic_similarity_scores(comment: str, rules: List[Dict[str, Any]]) -> List[float]:
    if not rules:
        return []

    rule_texts = [rule.get("text", "") for rule in rules]
    if SKLEARN_AVAILABLE:
        vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        vectors = vectorizer.fit_transform([comment] + rule_texts)
        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
        return [float(score) for score in similarities]

    comment_tokens = set(_tokenize(comment))
    scores = []
    for text in rule_texts:
        rule_tokens = set(_tokenize(text))
        if not comment_tokens or not rule_tokens:
            scores.append(0.0)
            continue
        intersection = comment_tokens.intersection(rule_tokens)
        union = comment_tokens.union(rule_tokens)
        scores.append(len(intersection) / max(1, len(union)))
    return scores


def _score_rules(comment: str, rules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    semantic_scores = _semantic_similarity_scores(comment, rules)
    scored = []
    for idx, rule in enumerate(rules):
        exact_score, matched_keywords = _exact_match_score(comment, rule)
        semantic_score = semantic_scores[idx] if idx < len(semantic_scores) else 0.0
        combined = max(exact_score, semantic_score)
        scored.append({
            "rule": rule,
            "exact_score": exact_score,
            "semantic_score": semantic_score,
            "combined_score": combined,
            "matched_keywords": matched_keywords,
        })
    return scored


def adjudicate_comment(
    comment: str,
    rules_json: Dict[str, Any],
    *,
    exact_threshold: float = 0.34,
    semantic_threshold: float = 0.28,
) -> Dict[str, Any]:
    comment = (comment or "").strip()
    rules = rules_json.get("rules") if isinstance(rules_json, dict) else None
    if not comment:
        return {
            "verdict": "No Violation",
            "citation_anchor": None,
            "reasoning": "No content provided to analyze.",
            "confidence": 0.0,
            "flags": ["EMPTY_COMMENT"],
        }

    if not rules:
        return {
            "verdict": "No Violation",
            "citation_anchor": None,
            "reasoning": "No rules available to anchor a violation.",
            "confidence": 0.0,
            "flags": ["NO_RULES"],
        }

    scored = _score_rules(comment, rules)
    scored.sort(key=lambda item: item["combined_score"], reverse=True)
    best = scored[0]

    is_violation = (
        best["exact_score"] >= exact_threshold or best["semantic_score"] >= semantic_threshold
    )

    if not is_violation:
        return {
            "verdict": "No Violation",
            "citation_anchor": None,
            "reasoning": "No rule could be anchored to the content.",
            "confidence": round(float(best["combined_score"]), 3),
            "flags": ["NO_APPLICABLE_RULE"],
        }

    rule = best["rule"]
    confidence = round(float(best["combined_score"]), 3)
    keywords_note = ""
    if best["matched_keywords"]:
        keywords_note = f"Matched keywords: {', '.join(best['matched_keywords'])}."

    return {
        "verdict": "Violation",
        "citation_anchor": {
            "rule_id": rule.get("id", "unknown"),
            "quoted_rule_text": rule.get("text", ""),
        },
        "reasoning": (
            f"Content aligns with rule {rule.get('id', 'unknown')}. {keywords_note}".strip()
        ),
        "confidence": confidence,
        "flags": [],
        "match_details": {
            "exact_score": round(float(best["exact_score"]), 3),
            "semantic_score": round(float(best["semantic_score"]), 3),
        },
    }


def load_rules_from_text(rule_text: str) -> Dict[str, Any]:
    return normalize_rules_to_json(rule_text)


def load_rules_from_file(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Citation Anchoring checker")
    parser.add_argument("--comment", required=True, help="User comment to analyze")
    parser.add_argument(
        "--rules-json",
        help="Path to rules JSON file (output of normalizer.py)",
    )
    parser.add_argument(
        "--rules-text",
        help="Raw rules text to normalize before analysis",
    )
    parser.add_argument(
        "--rules-file",
        help="Path to a text file containing raw community rules",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()

    if args.rules_json:
        rules = load_rules_from_file(args.rules_json)
    elif args.rules_text:
        rules = load_rules_from_text(args.rules_text)
    elif args.rules_file:
        with open(args.rules_file, "r", encoding="utf-8") as handle:
            rules = load_rules_from_text(handle.read())
    else:
        raise SystemExit("Provide --rules-json, --rules-text, or --rules-file")

    result = adjudicate_comment(args.comment, rules)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
