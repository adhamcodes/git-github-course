#!/usr/bin/env python3
"""Repository quality gates for the Git & GitHub course.

The validator intentionally uses only the Python standard library so a fresh clone can
run the same checks locally and in CI without installing project dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = {
    "README.md",
    "START_HERE.md",
    "STUDENT_LAB.md",
    "SAFETY.md",
    "ASSESSMENTS.md",
    "CHEATSHEET.md",
    "CONTRIBUTING.md",
    "LICENSE",
}

MODULES = [
    ("Module_0_Setup", "Module_0_Guide.md", range(1, 4)),
    ("Module_1_Daily_Core", "Module_1_Guide.md", range(4, 9)),
    ("Module_2_Branching", "Module_2_Guide.md", range(9, 13)),
    ("Module_3_Remotes", "Module_3_Guide.md", range(13, 17)),
    ("Module_4_Collaboration", "Module_4_Guide.md", range(17, 21)),
    ("Module_5_Fixing_Mistakes", "Module_5_Guide.md", range(21, 25)),
    ("Module_6_Real_World", "Module_6_Guide.md", range(25, 29)),
]

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_structure(errors: list[str]) -> None:
    for relative in sorted(REQUIRED_ROOT_FILES):
        if not (ROOT / relative).is_file():
            fail(errors, f"Missing required root file: {relative}")

    capstone = ROOT / "Capstone_First_Contribution" / "README.md"
    if not capstone.is_file():
        fail(errors, "Missing capstone README")

    for module_dir, guide_name, lessons in MODULES:
        module = ROOT / module_dir
        if not module.is_dir():
            fail(errors, f"Missing module directory: {module_dir}")
            continue

        if not (module / guide_name).is_file():
            fail(errors, f"Missing module guide: {module_dir}/{guide_name}")

        exercises = module / "Exercises"
        exercise_docs = list(exercises.glob("*.md")) if exercises.is_dir() else []
        if not exercise_docs:
            fail(errors, f"Module has no exercise sheet: {module_dir}/Exercises")

        for lesson in lessons:
            log = module / "Logs" / f"Lesson_{lesson:02d}.md"
            if not log.is_file():
                fail(errors, f"Missing lesson log: {log.relative_to(ROOT)}")


def validate_markdown_links(errors: list[str]) -> None:
    for md in sorted(ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1).strip()
            if not raw_target or raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            # Markdown links may include an optional quoted title after the destination.
            target = raw_target.split(maxsplit=1)[0].strip("<>")
            target = unquote(target).split("#", 1)[0]
            if not target:
                continue

            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(errors, f"Link escapes repository: {md.relative_to(ROOT)} -> {raw_target}")
                continue

            if not resolved.exists():
                fail(errors, f"Broken local link: {md.relative_to(ROOT)} -> {raw_target}")


def validate_file_hygiene(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue

        relative = path.relative_to(ROOT)
        if ".git" in relative.parts:
            continue

        if path.stat().st_size == 0:
            fail(errors, f"Unexpected empty file: {relative}")

        if path.suffix.lower() == ".md":
            text = path.read_text(encoding="utf-8")
            match = PLACEHOLDER.search(text)
            if match:
                fail(errors, f"Placeholder marker {match.group(0)!r} in {relative}")


def main() -> int:
    errors: list[str] = []
    validate_structure(errors)
    validate_markdown_links(errors)
    validate_file_hygiene(errors)

    if errors:
        print("QUALITY GATES: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1

    print("QUALITY GATES: PASS")
    print("Verified required structure, 28 lesson logs, exercise sheets, local links, and file hygiene.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
