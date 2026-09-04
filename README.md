# Git & GitHub: Zero to Independent

> A hands-on mini-academy for learning Git by using it, breaking it, inspecting it, recovering it, and collaborating with it.

**Start here:** [`START_HERE.md`](START_HERE.md)

This course is designed for beginners who want more than a list of commands. The target is a learner who can look at an unfamiliar repository state, understand what Git is telling them, make a deliberate change, and recover when something goes wrong.

## Learning loop

> **LEARN → PREDICT → DO → INSPECT → BREAK/RECOVER → EXPLAIN → PROVE**

Every module ends in evidence, not just reading.

## Course map

| Module | Capability |
|---|---|
| **0 — Setup** | distinguish Git/GitHub, configure Git, create repositories safely |
| **1 — Daily Core** | status, diff, staging, commits, history, ignore rules |
| **2 — Branching** | isolate work, inspect branches, merge deliberately |
| **3 — Remotes** | clone, push, fetch, pull, tracking, remote/local relationships |
| **4 — Collaboration** | forks, PRs, reviews, Issues, contribution etiquette |
| **5 — Recovery** | restore, stash, amend, revert, reset, reflog, recovery branches |
| **6 — Real World** | conflicts, divergence, rebase boundaries, tags/releases, controlled CI |
| **Capstone** | complete a real contribution workflow and demonstrate recovery skills |

The course contains 28 lessons, module challenge sheets, six cumulative gates plus capstone assessment, and a self-contained GitHub Actions lab.

## Important: use a separate practice repository

Treat this repo as the textbook. Practice in your own disposable **`git-github-lab`** repository.

That separation lets you create conflicts, reset history, recover commits, and make a mess without modifying the curriculum.

Setup: **[`STUDENT_LAB.md`](STUDENT_LAB.md)**

Safety rules: **[`SAFETY.md`](SAFETY.md)**

Cumulative gates: **[`ASSESSMENTS.md`](ASSESSMENTS.md)**

## Mastery gates

The course is not timed. Move forward when you can demonstrate the capability from memory and explain the state changes you caused.

Major cumulative gates cover:

- local Git fundamentals
- branching
- remote/GitHub round trips
- collaboration
- recovery
- a final Git disaster/recovery lab

See **[`ASSESSMENTS.md`](ASSESSMENTS.md)**.

## What you should be able to do when finished

You should be able to:

- explain Git's working tree, staging area, commits, branches, and remotes
- inspect before acting instead of guessing
- create focused commits and useful history
- branch/merge and resolve conflicts
- clone/fetch/pull/push deliberately
- open and review pull requests
- distinguish safe history-preserving recovery from history rewriting
- use reflog to recover displaced committed work
- understand the shared-history boundary for rebase/reset/force operations
- tag a version and understand GitHub Releases
- read, run, deliberately fail, and repair a basic GitHub Actions workflow
- make a small, respectful open-source contribution

## The repository practices what it teaches

This course has its own cross-platform GitHub Actions quality gate. On every push and pull request it checks the required course structure, all 28 lesson logs, module exercise sheets, local Markdown links, file hygiene, and the runnable CI demo.

Run the same core validation locally:

```bash
python scripts/validate_repo.py
```

The controlled Actions lab lives at [`examples/actions/README.md`](examples/actions/README.md).

## Core commands are not the course

You will use these constantly:

```bash
git status
git diff
git add
git commit
git log
git switch
git fetch
git pull
git push
```

But competence comes from knowing **what state they change and why**, not from memorizing syntax.

## Reference

- [`CHEATSHEET.md`](CHEATSHEET.md) — quick command reference
- [Pro Git](https://git-scm.com/book/en/v2) — free official Git book
- [GitHub Docs](https://docs.github.com/en/get-started) — GitHub workflows and product documentation

## Contributing and license

Contributions should preserve the inspection-first, evidence-based learning model. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Licensed under the [`MIT License`](LICENSE).

## Begin

Open **[`START_HERE.md`](START_HERE.md)** and create your student lab before Lesson 1.
