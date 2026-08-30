# Cumulative Mastery Assessments

These are practical gates, not quizzes. Perform them in your separate disposable **`git-github-lab`** repository.

You may use `git help` and official documentation unless a gate explicitly says closed-reference. Do not follow a memorized solution script. The goal is to inspect state, choose operations deliberately, and explain what happened.

---

## Gate 1 — Local Git Fundamentals (after Module 1)

### Practical

Without copying a command sequence:

1. create or reset a disposable practice repository
2. make two new files
3. inspect the state
4. stage only one file
5. inspect exactly what is staged
6. commit it with a useful message
7. explain why the other file was excluded
8. modify the committed file
9. show its unstaged diff
10. stage it and prove the same change moved into the staged diff
11. commit it
12. create an ignore rule and prove it works
13. show your final history

### Oral check

Explain:

- working tree
- staging area/index
- commit
- `HEAD`
- `git diff` vs `git diff --staged`
- why `.gitignore` is not secret-removal

### Pass standard

You can create focused commits without blindly staging everything, and you can explain the state before and after each operation.

---

## Gate 2 — Branching (after Module 2)

### Practical

1. start from a clean `main`
2. create two branches from the same baseline
3. make different commits on both branches
4. inspect the graph and identify the branch tips
5. compare branch content/history
6. merge one branch into `main`
7. predict what will happen when integrating the other branch
8. perform the integration
9. inspect the resulting graph
10. safely delete branches that are no longer needed

### Oral check

Explain:

- branch vs folder copy
- branch vs commit
- `HEAD`
- merge direction
- fast-forward vs divergent/three-way merge
- what `git branch -d` protects you from in common cases

### Pass standard

You can reason from the graph rather than guessing what a branch or merge will do.

---

## Gate 3 — Remote / GitHub Round Trip (after Module 3)

Use a disposable GitHub repository.

### Practical

1. connect or clone the repository locally
2. identify `origin`, local `main`, and `origin/main`
3. make and push a local commit
4. make a different commit through GitHub's web editor
5. **fetch first**
6. inspect the graph and the commits/diff between local and remote-tracking branches
7. integrate the remote change safely
8. create one local commit while also creating a different GitHub-side commit before synchronizing
9. fetch and diagnose the resulting divergence
10. integrate it without raw force push
11. push the resolved history

### Oral check

Explain:

- remote
- `origin`
- local branch vs remote-tracking branch
- upstream tracking
- fetch
- pull
- push
- why a rejected push is not an instruction to force-push

### Pass standard

You can complete and diagnose a local↔GitHub round trip while inspecting before integrating.

---

## Gate 4 — Collaboration (after Module 4)

Use a repository you control for the full lifecycle, and use a fork-based practice repository to demonstrate external contribution setup.

### Practical

1. show the difference between branch, clone, and fork
2. in a fork, show `origin` and `upstream`
3. in your own repo, open an Issue describing a small change and acceptance criteria
4. create a focused branch
5. inspect/stage/commit the implementation
6. push the branch and open a Pull Request linked to the Issue
7. inspect the PR diff as a reviewer
8. receive or simulate review feedback
9. update the **same PR** with another commit
10. merge it using an appropriate merge method
11. verify the linked Issue state

### Oral check

Explain what you would inspect before opening a PR to a project you do not own:

- contribution guide
- existing Issues/PRs
- assignment/maintainer expectations
- validation requirements
- project scope

### Pass standard

You can use GitHub as a collaboration system rather than merely as file hosting.

---

## Gate 5 — Recovery (after Module 5)

Every destructive experiment must happen only in disposable work.

### Practical

Demonstrate all of these:

1. unstage a change while preserving the edit
2. stash and restore work
3. deliberately discard a throwaway uncommitted edit and explain why Git may not recover it
4. amend an unpublished commit
5. soft-reset an unpublished commit and explain the staged result
6. revert a committed change and show that history is preserved
7. deliberately displace a **committed** change with a controlled reset
8. find that commit in reflog
9. recover it using a new recovery branch

### Safety narration

Before each risky action, state:

- what can change in the working tree
- what can change in the index
- what can happen to branch history
- whether another person could already depend on the commit

### Pass standard

You choose recovery operations based on the state/problem instead of treating undo commands as interchangeable.

---

## Gate 6 — Real-World Git / Disaster Lab (after Module 6)

Create a throwaway repository with several meaningful commits and branches.

Then intentionally construct this situation:

1. `main` and a feature branch diverge
2. both modify the same line differently
3. a merge conflict occurs
4. resolve the conflict and inspect the merge graph
5. create a local commit and a different remote commit to produce local/remote divergence
6. fetch and diagnose it before integration
7. integrate it without raw force push
8. create another committed change
9. deliberately displace that commit in the disposable repo
10. recover it with reflog + a recovery branch
11. create an annotated version tag and inspect it
12. inspect a basic GitHub Actions workflow and identify trigger/jobs/steps

### Required evidence

Capture or record the relevant output from:

```bash
git status
git branch -vv
git remote -v
git log --oneline --graph --decorate --all
git reflog
```

### Incident report

Write a short report:

- what state you intentionally created
- what evidence told you what was happening
- what you predicted before each recovery step
- which operations preserved history
- which operations rewrote/moved history
- why your chosen recovery was safer than tempting alternatives
- what you would do differently in an important/shared repository

### Pass standard

You can enter an unfamiliar-looking Git problem, inspect first, form a reasonable model, recover deliberately, and verify the result.

---

# Graduation standard

Passing all six gates means you are ready for the capstone.

You are **not** expected to remember every Git flag.

You are expected to have this response to confusion:

> **inspect → model the current state → predict → choose the least destructive appropriate operation → verify**

That is the independence target of this course.