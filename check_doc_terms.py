import argparse
import ast
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TRANSLATIONS = ROOT.parent / "i18n_localization_source" / "translations.py"

HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)[\uFF08(]([^\uFF09)]+)[\uFF09)]\s*$", re.M)
TERM_RE = re.compile(r"([\u4e00-\u9fff][\u4e00-\u9fffA-Za-z0-9·/\s+-]{0,30}?)[\uFF08(]([A-Za-z][^\uFF09)\n]{0,80})[\uFF09)]")
PAIR_ENGLISH_RE = re.compile(r"[\uFF08(]([A-Za-z][^\uFF09)\n]{0,80})[\uFF09)]")
TRAILING_ASCII_TERM_RE = re.compile(r"\s+\(([^()]*)\)$")

CONTEXT_PRIORITY = ("Property", "UI", "*", "Operator")
ACCEPTED_DOC_SUFFIXES = (
    "列表",
    "页",
    "颜色",
    "强度",
    "方式",
    "值",
    "量",
    "帧",
)

# English keys that are intentionally broader in help docs than the UI label.
DOC_TERM_OVERRIDES = {
    "nxAttract": "吸引修改器",
    "nxAvoid": "避让修改器",
    "nxBlend": "混合修改器",
    "nxCache": "nx 缓存",
    "nxCollider": "碰撞体修改器",
    "nxColor": "颜色修改器",
    "nxConstraints": "约束修改器",
    "nxCover": "覆盖修改器",
    "nxDirection": "方向修改器",
    "nxDrag": "阻力修改器",
    "nxEmitter": "发射器",
    "nxExplode": "爆炸修改器",
    "nxExplosiaFX": "爆炸特效修改器",
    "nxFlock": "群聚修改器",
    "nxFollowGeo": "跟随几何体修改器",
    "nxFluids": "流体修改器",
    "nxFolder": "nx 文件夹",
    "nxGenerator": "生成器修改器",
    "nxGravity": "重力修改器",
    "nxGroup": "nx 组",
    "nxInfectio": "感染修改器",
    "nxKill": "销毁修改器",
    "nxMesher": "网格化修改器",
    "nxQuestion": "问题修改器",
    "nxLimit": "限制修改器",
    "nxPush": "推力修改器",
    "nxRotate": "旋转修改器",
    "nxSpeed": "速度修改器",
    "nxScale": "缩放修改器",
    "nxSplash": "飞溅修改器",
    "nxTrail": "拖尾修改器",
    "nxTurbulence": "湍流修改器",
    "nxWave": "波浪修改器",
}

# Internal enum constants that may appear in old help text. Treat them as the
# UI English labels so pair checking can catch stale enum-style terms.
ENGLISH_KEY_ALIASES = {
    "ARROW": "Arrow",
    "ARROW_FILLED": "Arrow Filled",
    "AXIS": "Axis",
    "BOX": "Box",
    "BOX3D": "Box 3D",
    "BOX3D_FILLED": "Box 3D Filled",
    "DISC": "Disc",
    "DIRECTION": "Direction",
    "EDGES": "Edges",
    "FIXED": "Fixed",
    "Full Lifetime": "Full Lifespan",
    "HEX": "Hexagonal",
    "Lifetime": "Lifespan",
    "Lifetime Var": "Variation",
    "MESH": "Mesh",
    "NORMAL": "Normal",
    "OBJECT": "Object",
    "PHONG_NORMAL": "Phong Normal",
    "POINTS": "Points",
    "POLY_AREA": "Polygon Area",
    "POLY_CENTER": "Polygon Center",
    "PULSE": "Pulse",
    "PYRAMID": "Pyramid",
    "PYRAMID_FILLED": "Pyramid Filled",
    "RANDOM": "Random",
    "RATE": "Rate",
    "RECT": "Rectangle",
    "REGULAR": "Regular",
    "SHOT": "Shot",
    "SPHERE": "Sphere",
    "SSF": "Screen Space Fluid",
    "TEXTURE": "Texture",
}


def normalize_zh(text):
    text = text.strip()
    match = TRAILING_ASCII_TERM_RE.search(text)
    if match:
        inner = match.group(1)
        if re.search(r"[A-Za-z]", inner):
            text = text[: match.start()].strip()
    return re.sub(r"\s+", " ", text)


def load_translations():
    tree = ast.parse(TRANSLATIONS.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "zh_CN":
                    raw = ast.literal_eval(node.value)
                    break
            else:
                continue
            break
    else:
        raise SystemExit("zh_CN not found in translations.py")

    by_english = defaultdict(list)
    for key, value in raw.items():
        if not isinstance(key, tuple) or len(key) != 2:
            continue
        context, english = key
        if not isinstance(english, str) or not isinstance(value, str):
            continue
        by_english[english].append((context, normalize_zh(value)))
    return by_english


def preferred_translation(items):
    by_context = defaultdict(list)
    for context, zh in items:
        by_context[context].append(zh)
    for context in CONTEXT_PRIORITY:
        values = [zh for zh, _count in Counter(by_context.get(context, [])).most_common()]
        if values:
            return values[0]
    return Counter(zh for _context, zh in items).most_common(1)[0][0]


def canonical_english(english):
    return ENGLISH_KEY_ALIASES.get(english, english)


def term_matches(doc_zh, expected, strict):
    if doc_zh == expected:
        return True
    if doc_zh.endswith(expected):
        return True
    if strict:
        return False
    if len(expected) >= 2 and doc_zh.startswith(expected):
        return True
    if len(expected) == 1:
        return any(doc_zh == expected + suffix for suffix in ACCEPTED_DOC_SUFFIXES)
    return False


def extract_doc_terms(include_h2, scan_body):
    terms = []
    for path in sorted(ROOT.glob("nx*.md")):
        text = path.read_text(encoding="utf-8")
        seen = set()
        for match in HEADING_RE.finditer(text):
            level, chinese, english = match.groups()
            if level == "##" and not include_h2:
                continue
            line = text[: match.start()].count("\n") + 1
            item = (line, normalize_zh(chinese), english.strip())
            seen.add(item)
            terms.append((path.name, line, item[1], item[2]))
        if scan_body:
            for match in TERM_RE.finditer(text):
                chinese, english = match.groups()
                line = text[: match.start()].count("\n") + 1
                item = (line, normalize_zh(chinese), english.strip())
                if item in seen:
                    continue
                terms.append((path.name, line, item[1], item[2]))
    return terms


def prefix_has_expected_term(prefix, expected):
    prefix = normalize_zh(prefix)
    prefix = prefix.rstrip(" ：:，,。.；;、-—")
    if prefix.endswith(expected):
        return True
    return False


def extract_doc_pairs():
    pairs = []
    for path in sorted(ROOT.glob("nx*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, 1):
            for match in PAIR_ENGLISH_RE.finditer(line):
                english = match.group(1).strip()
                prefix = line[: match.start()]
                pairs.append((path.name, line_number, prefix, english, line.strip()))
    return pairs


def main():
    parser = argparse.ArgumentParser(description="Check Chinese help heading terms against translations.py.")
    parser.add_argument("--all-headings", action="store_true", help="also check H2 modifier titles")
    parser.add_argument("--body", action="store_true", help="also scan inline terms in document body")
    parser.add_argument("--pairs", action="store_true", help="check every Chinese（English） pair by English key")
    parser.add_argument("--show-ok", action="store_true", help="print matched terms too")
    parser.add_argument("--strict", action="store_true", help="require exact Chinese heading match")
    args = parser.parse_args()

    translations = load_translations()
    problems = []
    ambiguous = []
    checked = 0

    for file_name, line, doc_zh, english in extract_doc_terms(args.all_headings, args.body):
        english = canonical_english(english)
        if english not in translations:
            continue
        expected = DOC_TERM_OVERRIDES.get(english, preferred_translation(translations[english]))
        variants = sorted(set(zh for _context, zh in translations[english]))
        if len(variants) > 1:
            ambiguous.append((english, variants))
        checked += 1
        if not term_matches(doc_zh, expected, args.strict):
            problems.append((file_name, line, english, doc_zh, expected, variants))
        elif args.show_ok:
            print(f"ok: {file_name}:{line}: {doc_zh}（{english}）")

    if args.pairs:
        for file_name, line, prefix, english, source_line in extract_doc_pairs():
            english = canonical_english(english)
            if english not in translations:
                continue
            expected = DOC_TERM_OVERRIDES.get(english, preferred_translation(translations[english]))
            variants = sorted(set(zh for _context, zh in translations[english]))
            checked += 1
            if not prefix_has_expected_term(prefix, expected):
                problems.append((file_name, line, english, normalize_zh(prefix), expected, variants))
                if args.show_ok:
                    print(f"source: {source_line}")
            elif args.show_ok:
                print(f"ok pair: {file_name}:{line}: {expected}（{english}）")

    seen_ambiguous = set()
    for english, variants in ambiguous:
        if english in seen_ambiguous:
            continue
        seen_ambiguous.add(english)
        if english in DOC_TERM_OVERRIDES:
            continue
        print(f"ambiguous translation: {english} -> {' / '.join(variants)}")

    for file_name, line, english, doc_zh, expected, variants in problems:
        print(f"mismatch: {file_name}:{line}: {doc_zh}（{english}） -> {expected}")
        if len(variants) > 1:
            print(f"  translation variants: {' / '.join(variants)}")

    if problems:
        print(f"checked={checked} mismatches={len(problems)}")
        raise SystemExit(1)
    print(f"ok checked={checked}")


if __name__ == "__main__":
    main()
