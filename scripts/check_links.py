"""Helyi Markdown-linkcélok ellenőrzése; internetes oldalakat nem kér le."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    files = sorted(ROOT.glob("*.md"))
    for folder in ("docs", "peldak"):
        files.extend(sorted((ROOT / folder).rglob("*.md")))
    errors = []
    count = 0
    for file in files:
        content = re.sub(r"```.*?```", "", file.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            parsed = urlsplit(target.strip("<>"))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            path = (file.parent / unquote(parsed.path)).resolve()
            if not path.is_relative_to(ROOT) or not path.exists():
                errors.append(f"{file.relative_to(ROOT)}: {target}")
    for error in errors:
        print(error)
    print(f"{len(files)} Markdown-fájl, {count} helyi link, {len(errors)} hibás cél.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
