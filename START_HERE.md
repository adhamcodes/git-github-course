# START HERE — Git & GitHub: Zero to Independent

This repository is the **course**. Your practice should happen in a separate throwaway learning repository so you can experiment, break things, recover them, and build real Git history without modifying the curriculum itself.

## 1. What you are learning

- **Git** = version control on your computer. It records project history as commits.
- **GitHub** = a hosting and collaboration platform for Git repositories.

The goal is not memorizing commands. The goal is becoming able to inspect a repository, make changes safely, recover from mistakes, collaborate through branches and pull requests, and understand what Git is doing.

## 2. Create your student lab first

Before Lesson 1, create a folder/repository named something like:

```text
git-github-lab/
├── notes/
├── experiments/
└── README.md
```

All practice, deliberate mistakes, lesson logs, branches, conflicts, resets, and recovery exercises happen there.

**Do not use this course repository as your practice playground.** Treat this repo as read-only curriculum.

See **[STUDENT_LAB.md](STUDENT_LAB.md)** for the exact setup.

## 3. How the course works

Use this loop:

> **LEARN → PREDICT → DO → INSPECT → BREAK/RECOVER → EXPLAIN → PROVE**

For each module:

1. work through the module guide in your student lab,
2. complete the module's `Exercises/README.md` challenges,
3. complete the matching cumulative gate in [ASSESSMENTS.md](ASSESSMENTS.md),
4. advance only when you can do the required work without copying a recipe.

When a task contains a destructive or history-rewriting command, first read **[SAFETY.md](SAFETY.md)**.

## 4. Course order

1. **Module 0 — Setup**: Git vs GitHub, installation, identity, first repository
2. **Module 1 — Daily Core**: status, diff, staging, commits, history, ignore rules
3. **Module 2 — Branching**: branches, switching, merging, branch inspection
4. **Module 3 — Remotes**: clone, push, fetch, pull, upstream tracking, divergence
5. **Module 4 — Collaboration**: forks, pull requests, review, issues, contribution etiquette
6. **Module 5 — Recovery**: restore, stash, amend, revert, reset, reflog
7. **Module 6 — Real World**: conflicts, rebase, tags/releases, controlled GitHub Actions lab
8. **Final Capstone**: complete a real contribution workflow and demonstrate recovery skills

## 5. What to do with the lesson logs

The `Logs/` files in this curriculum are templates/reference worksheets. Copy the relevant log into your own `git-github-lab/notes/` folder and fill it out there.

Do not edit the public curriculum merely to tick boxes.

## 6. The safety rule

Before any command that can discard or rewrite work:

```bash
git status
git diff
git log --oneline --decorate -10
```

Then ask:

> **Is the work committed? Is it pushed/shared? Am I intentionally rewriting or deleting anything?**

If you cannot answer those questions, stop and inspect before continuing.

## 7. The mastery rule

You are ready to move on when you can:

- predict what a command will change,
- run it,
- inspect whether your prediction was correct,
- explain the result,
- recover if you deliberately create a failure,
- pass the module challenge and cumulative gate without command-by-command copying.

Finishing pages is not mastery.

## Start now

1. Open **[STUDENT_LAB.md](STUDENT_LAB.md)**.
2. Create your separate practice repo.
3. Then begin **[Module 0](Module_0_Setup/Module_0_Guide.md)**.

If you get lost later, return to this sentence:

> **Read the lesson. Work in the lab. Inspect constantly. Complete the challenge. Prove the gate.**
