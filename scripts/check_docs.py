"""Check ULPG documentation integrity using only the Python standard library.

Checks repository files, relative inline Markdown links, and guide structure.
Does not evaluate landing-page behavior, accessibility, or external URLs.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "LICENSE", "NOTICE.md", "AGENTS.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "GOVERNANCE.md", "CHANGELOG.md",
    "docs/guide.md", "docs/human-workflow.md", "docs/agent-workflow.md",
    "docs/references.md", "templates/page-brief.md", "templates/review.md",
    "templates/decision-record.md", "templates/third-party-inventory.md",
    "templates/performance-budget.md", "examples/editorial-review.md",
    ".github/workflows/docs.yml",
)


def main():
    errors = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or not path.stat().st_size:
            errors.append(f"Missing or empty required file: {relative}")

    files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    links_checked = 0
    for path in files:
        relative = path.relative_to(ROOT)
        content = path.read_text(encoding="utf-8")
        if not content.startswith("# ") and "ISSUE_TEMPLATE" not in path.parts:
            errors.append(f"{relative}: expected a top-level title")
        # Ignore task prompts and other fenced code; inspect inline links only.
        prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", content, flags=re.M | re.S)
        for match in re.finditer(r"\[[^\]\n]+\]\(([^)\n]+)\)", prose):
            destination = match.group(1).strip().strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f"{relative}: link leaves repository: {destination}")
            elif not target.exists():
                errors.append(f"{relative}: missing local link target: {destination}")
            links_checked += 1

    guide = ROOT / "docs/guide.md"
    if guide.is_file():
        text = guide.read_text(encoding="utf-8")
        sections = re.findall(r"^## (\d+)\. ", text, flags=re.M)
        if sections != [str(number) for number in range(1, 21)]:
            errors.append("Guide must retain ordered top-level sections 1 through 20")
        if "**Version:** 0.3.0" not in text:
            errors.append("Guide version must match initial edition 0.3.0; update checker for a release")

    if errors:
        print("Documentation checks failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Passed: {len(files)} Markdown files, {links_checked} local links, "
          "required files, and guide structure.")
    print("External links and landing-page quality were not tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
