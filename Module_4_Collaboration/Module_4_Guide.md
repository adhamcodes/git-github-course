# MODULE 4 — Collaboration (Lessons 17–20)

**Goal:** Learn the collaboration workflow used on real GitHub projects: fork/clone when appropriate, branch, commit, push, open a Pull Request, review changes, respond to feedback, and connect work to Issues.

**Primary references:**
- [GitHub Docs — Pull Requests](https://docs.github.com/en/pull-requests)
- [GitHub Docs — Forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks)
- [GitHub Docs — Issues](https://docs.github.com/en/issues)

---

## Lesson 17 — Fork vs clone vs branch: choose the right boundary

### LEARN

These are different operations:

- **branch** — a line of development inside one Git repository
- **clone** — create a local copy of a Git repository and its history
- **fork** — create a GitHub-hosted repository under another account/namespace based on an existing repository

You do **not** need to fork every repository you work on.

Typical cases:

```text
Your own repo / collaborator access
    clone → branch → push → PR

External project without write access
    fork → clone your fork → branch → push → PR to upstream project
```

Before contributing to an external project, read its `README`, `CONTRIBUTING.md`, issue/PR templates, code of conduct, and any maintainer instructions. A technically correct change can still be an unwanted contribution if you ignore project rules.

### DO

Choose a practice repository that explicitly welcomes beginner contributions, such as:

<https://github.com/firstcontributions/first-contributions>

Fork it on GitHub, then clone **your fork**:

```bash
git clone <url-of-your-fork>
cd first-contributions
git remote -v
```

Add the original project as a second remote named `upstream`:

```bash
git remote add upstream <url-of-original-repository>
git remote -v
```

Mental model:

```text
origin   = your fork
upstream = original project
```

Those names are conventions, not magic.

### TRANSITION CONDITION

Explain when you need a fork and when a normal branch is enough. Show `origin` and `upstream` in a fork-based practice repository.

---

## Lesson 18 — Create a focused Pull Request

### LEARN

A Pull Request is a GitHub collaboration object that proposes merging one branch into another and provides a place for diff review, discussion, checks, and approval.

A good beginner PR is:

- small
- focused on one purpose
- based on project instructions
- easy to review
- explained clearly

Do not mix unrelated cleanup into a PR just because you noticed it.

### DO

Before changing anything:

```bash
git status
git switch -c add-my-name
```

Make the contribution required by the practice repo.

Inspect before committing:

```bash
git status
git diff
git add <intended-file>
git diff --staged
git commit -m "Add <your-name> to contributors"
```

Inspect history and push the branch:

```bash
git log --oneline --decorate -5
git push -u origin add-my-name
```

On GitHub, open the Pull Request. In the description explain:

- what changed
- why
- anything the reviewer should know

If the project has a PR template, follow it instead of deleting it.

### TRANSITION CONDITION

From memory, create a focused branch, inspect/stage/commit only the intended change, push the branch, and open a clear PR.

---

## Lesson 19 — Review the diff, respond to feedback, update the same PR

### LEARN

PR review is not an exam. It is a collaboration process around the proposed change.

Reviewers may:

- comment on lines
- ask questions
- request changes
- approve
- rely on automated checks

When you push another commit to the **same PR branch**, GitHub updates the PR automatically.

A useful response pattern is:

1. understand the feedback
2. ask if unclear
3. make the smallest appropriate change
4. inspect it locally
5. commit and push to the same branch
6. reply explaining what changed

Do not resolve review comments you do not actually understand just to make the UI green.

### DO

On your own practice repository, create a second account/collaborator scenario if available—or simulate review on a PR you own.

Inspect the tabs:

- Conversation
- Commits
- Checks (if present)
- Files changed

Read the actual diff before merging.

Make one improvement on the PR branch:

```bash
git switch <pr-branch>
# edit

git diff
git add <file>
git diff --staged
git commit -m "Address review feedback"
git push
```

Refresh the PR and confirm the new commit/diff appears.

### MERGE METHODS — RECOGNIZE, DON'T WORSHIP

GitHub commonly offers:

- merge commit
- squash and merge
- rebase and merge

Different projects choose different history policies. As a contributor, follow the repository's convention. You do not need one universal “best” merge method.

### TRANSITION CONDITION

You can inspect a PR diff, update an existing PR by pushing another commit, and explain why review feedback changes the branch rather than requiring a brand-new PR.

---

## Lesson 20 — Issues, linking work, and contribution etiquette

### LEARN

Issues can represent bugs, feature requests, investigations, or tasks—but repositories use Issues differently.

Before opening one:

- search existing Issues
- read templates/instructions
- confirm the repo actually accepts the type of request
- provide reproduction/context instead of “it doesn't work”

Closing keywords such as:

```text
Closes #12
Fixes #12
Resolves #12
```

can connect a PR to an Issue and, in supported same-repository/default-branch workflows, automatically close it when the PR is merged.

### DO — YOUR OWN PRACTICE REPO

Use a repo you own so you can safely exercise the complete lifecycle:

1. open an Issue describing a small change with acceptance criteria
2. create a branch named after the task
3. make the change
4. open a PR
5. reference the issue with `Closes #<number>`
6. inspect the PR diff
7. merge it
8. confirm the issue state afterward

### OPEN-SOURCE ETIQUETTE CHECK

Before the capstone, be able to answer:

- Did the maintainers ask for an Issue before a PR?
- Is this issue already assigned?
- Is there a contribution guide?
- Am I changing only what the PR claims to change?
- Did I run whatever validation the project asks for?
- Am I comfortable if maintainers decline the contribution?

### TRANSITION CONDITION

Create and complete an Issue→branch→PR→review→merge loop in a repository you control, and explain how you would behave differently in someone else's project.

---

## Module 4 gate

You are ready for recovery when you can:

- [ ] distinguish branch, clone, and fork
- [ ] use `origin` and `upstream` in a fork workflow
- [ ] read contribution instructions before changing an external project
- [ ] open a focused PR from a branch
- [ ] inspect a PR diff and respond to review feedback
- [ ] recognize common merge methods without assuming one is universally correct
- [ ] use Issues and PR links deliberately
- [ ] describe respectful open-source contribution etiquette

Then complete **Gate 4 — Collaboration** in [`../ASSESSMENTS.md`](../ASSESSMENTS.md) before Module 5.