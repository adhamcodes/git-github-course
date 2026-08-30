# CAPSTONE — Real Contribution + Recovery Proof + GitHub Profile

**Goal:** Prove you can use Git and GitHub independently in a realistic workflow, recover from mistakes without panic, and present your work professionally.

This capstone has **three parts**. Complete all three.

---

## Part A — Make one respectful real contribution

Use the full external-contribution workflow:

> discover → read project rules → fork if needed → clone → branch → inspect → change → test → commit → push → PR → review

### Find a contribution

Prefer one of these:

- an explicitly labeled beginner / `good first issue` task
- a documentation correction you can verify
- a small bug with clear reproduction and maintainer interest
- a project you already use and understand enough to improve responsibly

Practice-only option: [First Contributions](https://github.com/firstcontributions/first-contributions).

Discovery sites can help you browse, but **the target repository's own contribution instructions are authoritative**.

### Before touching code

Check:

- `README.md`
- `CONTRIBUTING.md`
- open Issues and existing PRs
- issue/PR templates
- code of conduct if present
- whether maintainers want an Issue before implementation
- whether the task is assigned or already being worked on

Do not open drive-by PRs that create review work without adding useful value.

### Required workflow

1. identify one small contribution
2. document why it is appropriate
3. fork only if you lack write access / the project workflow expects a fork
4. clone the correct repository
5. configure `upstream` when using a fork
6. create a focused branch
7. make only the intended change
8. run the project's requested validation
9. inspect `git status`, `git diff`, and staged diff
10. create one or more coherent commits
11. push your branch
12. open a clear PR
13. respond professionally to feedback if any arrives

### Evidence to save

In your student workspace, record:

```text
repository:
issue/task:
branch:
commit(s):
PR URL:
validation performed:
what I learned from review:
```

### Part A passes when

- [ ] you followed the target project's contribution rules
- [ ] your PR is small and understandable
- [ ] commit/PR text explains the change clearly
- [ ] you did not include unrelated cleanup
- [ ] requested validation was performed
- [ ] a real PR exists, even if maintainers ultimately decline or close it

A merge is great evidence, but maintainers owe you neither a merge nor a response.

---

## Part B — Git disaster/recovery practical

A Git user is not independent if everything is fine only while nothing goes wrong.

Use your **disposable student lab**, never important work.

### Scenario 1 — recover a displaced commit

1. create and commit a file called `recovery-proof.txt`
2. record the commit hash
3. make at least one later commit
4. intentionally move the branch backward in the safe disposable environment
5. use `git reflog` to locate the displaced commit
6. recover it by creating a branch:

```bash
git switch -c recovered-work <hash>
```

7. verify `recovery-proof.txt` exists there
8. explain what happened to the branch pointer versus the commit

### Scenario 2 — resolve a real merge conflict

Create two branches that modify the **same line differently after they diverge**. Merge them to produce a conflict.

You must:

```bash
git status
```

- identify the conflicted path
- inspect the conflict markers
- choose the intended final content
- remove markers
- stage the resolved file
- complete the merge
- inspect the resulting graph

### Scenario 3 — diagnose local/remote divergence

Create one local commit and one different GitHub-side commit before synchronizing.

Then:

```bash
git fetch
git status
git log --oneline --graph --decorate --all
```

Explain the graph **before** integrating. Resolve without using raw force push.

### Part B passes when

- [ ] you recover a displaced committed change using reflog
- [ ] you resolve a deliberately created merge conflict
- [ ] you diagnose local/remote divergence from the graph
- [ ] you can name which operations in the exercise rewrote/moved history and which preserved it

---

## Part C — Build an honest, professional GitHub profile

The goal is **clarity and evidence**, not pretending to be more experienced than you are.

### Profile README

GitHub displays a profile README when you have a public repository whose name exactly matches your username and contains a root `README.md`.

Your profile should communicate:

- who you are
- what you are currently building/learning
- what kinds of engineering problems interest you
- a few projects that actually support those claims
- how someone can understand or contact you, if you want that public

Avoid giant walls of badges or skill logos that imply expertise you cannot demonstrate yet.

### Repository presentation checklist

For the strongest repositories you intend to feature:

- [ ] descriptive name
- [ ] concise repository description
- [ ] useful README
- [ ] clear project status
- [ ] setup/run instructions when relevant
- [ ] screenshots/demo where that genuinely helps
- [ ] no committed secrets
- [ ] understandable commit history
- [ ] license when you intentionally want others to reuse the work

### Pinning rule

Pin **evidence**, not clutter. Four strong repositories beat six weak/random ones.

### Part C passes when

- [ ] a stranger can understand your current direction quickly
- [ ] every major claim on your profile is supported by evidence or clearly worded as a goal/current learning direction
- [ ] your strongest public repos are easy to understand
- [ ] you understand how the profile README repository works

---

# Final oral/practical check

Without the cheatsheet, explain and demonstrate the relationship between:

```text
working tree
staging area
commit
branch
HEAD
remote
origin/main
fork
Pull Request
```

Then explain what you would inspect first in each situation:

1. “Git says I have changes but I don't know what they are.”
2. “My push was rejected.”
3. “I think I lost a commit.”
4. “A merge has conflicts.”
5. “I staged something I didn't want to commit.”
6. “I want to contribute to a repository I don't own.”

The expected behavior is not memorizing one rescue command. It is **inspect state → understand the boundary → choose the least destructive operation that solves the actual problem**.

---

# Course complete when

- [ ] all module transition conditions are complete
- [ ] cumulative gates in [`../ASSESSMENTS.md`](../ASSESSMENTS.md) are passed
- [ ] Part A real contribution is complete
- [ ] Part B recovery practical is complete
- [ ] Part C profile presentation is complete
- [ ] you can complete the normal local/remote/PR workflow without step-by-step instructions
- [ ] you can investigate common Git problems without immediately reaching for destructive commands

At that point the target is not “I memorized Git.” It is:

> **I can inspect a repository, reason about its state, collaborate safely, and recover when I make a mistake.**