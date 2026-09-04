from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


def run(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        check=check,
        text=True,
        capture_output=True,
    )


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as temp:
        repo = Path(temp) / "lab"
        repo.mkdir()
        run(repo, "init", "-b", "main")
        run(repo, "config", "user.name", "Course Smoke Test")
        run(repo, "config", "user.email", "course-smoke@example.invalid")

        color = repo / "color.txt"
        write(color, "Color: blue\n")
        run(repo, "add", "color.txt")
        run(repo, "commit", "-m", "Add baseline color")

        run(repo, "switch", "-c", "change-color")
        write(color, "Color: red\n")
        run(repo, "add", "color.txt")
        run(repo, "commit", "-m", "Change color to red")

        run(repo, "switch", "main")
        write(color, "Color: green\n")
        run(repo, "add", "color.txt")
        run(repo, "commit", "-m", "Change color to green")

        conflict = run(repo, "merge", "change-color", check=False)
        if conflict.returncode == 0:
            raise AssertionError("expected same-line merge conflict")
        if "UU color.txt" not in run(repo, "status", "--short").stdout:
            raise AssertionError("conflicted path was not reported as unmerged")

        write(color, "Color: purple\n")
        run(repo, "add", "color.txt")
        run(repo, "commit", "-m", "Resolve color conflict")
        if run(repo, "status", "--porcelain").stdout.strip():
            raise AssertionError("working tree should be clean after conflict resolution")

        recoverable = repo / "recoverable.txt"
        write(recoverable, "recover me\n")
        run(repo, "add", "recoverable.txt")
        run(repo, "commit", "-m", "Add recoverable commit")
        recoverable_sha = run(repo, "rev-parse", "HEAD").stdout.strip()

        run(repo, "reset", "--hard", "HEAD^")
        reflog = run(repo, "reflog", "--format=%H").stdout.splitlines()
        if recoverable_sha not in reflog:
            raise AssertionError("reflog did not retain the displaced commit")

        run(repo, "branch", "recovery", recoverable_sha)
        recovered = run(repo, "show", "recovery:recoverable.txt").stdout
        if recovered != "recover me\n":
            raise AssertionError("recovery branch did not restore displaced committed work")

    print("GIT BEHAVIOR SMOKE TEST: PASS")


if __name__ == "__main__":
    main()
