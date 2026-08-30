# Cumulative Mastery Assessments

These checks are intentionally cumulative. Do them in your separate `git-github-lab` repository.

Do not read the command solutions while attempting them. Use `git status`, `git diff`, `git log`, `git help`, and official documentation as needed.

## Gate A — Local Git Ready (after Module 1)

Without copying commands:

1. Create a repository.
2. Make two files.
3. Commit only one of them.
4. Explain why the other file was excluded.
5. Modify the committed file.
6. Show the unstaged diff.
7. Stage it.
8. Show the staged diff.
9. Commit it with a useful message.
10. Add an ignore rule and prove it works.

Pass when you can explain the working tree, staging area, and commit history while demonstrating them.

## Gate B — Branching Ready (after Module 2)

1. Start with a clean `main`.
2. Create two feature branches from the same baseline.
3. Make different commits on both.
4. Inspect the graph.
5. Merge one branch.
6. Predict whether the second merge will fast-forward, auto-merge, or conflict.
7. Perform it and explain the result.
8. Clean up merged branches safely.

## Gate C — GitHub Round Trip (after Module 3)

Using a disposable GitHub repository:

1. Clone it on your computer.
2. Make and push a local commit.
3. Make a different commit through GitHub's web editor.
4. Use `fetch` first and inspect the relationship before updating your local branch.
5. Bring the remote change down.
6. Push another local change.
7. Explain `origin`, upstream tracking, fetch, pull, and push.

## Gate D — Collaboration Ready (after Module 4)

In a practice repository or with a study partner:

1. Open an Issue describing a small change.
2. Create a branch for it.
3. Make focused commits.
4. Push the branch.
5. Open a Pull Request linked to the Issue.
6. Read the diff as a reviewer would.
7. Receive or simulate review feedback.
8. Update the same PR with another commit.
9. Merge it and confirm the Issue closes.

## Gate E — Recovery Ready (after Module 5)

You must demonstrate all of these without damaging important work:

- unstage while preserving edits
- stash and restore work
- revert a committed change
- amend an unpublished commit
- use a soft reset and explain the resulting staged state
- deliberately displace a committed change and recover it through reflog + a recovery branch

Before each potentially destructive action, state what you expect to happen.

## Final Disaster Lab (after Module 6)

Create a throwaway repository containing several meaningful commits and branches. Then intentionally create this situation:

1. feature branch and `main` diverge
2. same line changes on both branches
3. merge conflict occurs
4. one local commit becomes "lost" through a deliberate reset
5. remote has a commit local does not yet have

Recover the repository into a clean, understandable state.

Required evidence:

```bash
git status
git log --oneline --graph --decorate --all
git reflog
```

At the end, write a short incident report:

- what happened
- what Git state you observed
- which recovery actions you chose
- why those actions were safer than alternatives
- what you would do differently in an important repository

## Graduation standard

You are not finished because you remember every flag.

You are finished when an unfamiliar Git problem causes you to **inspect first**, form a mental model of the repository state, choose a deliberate operation, and verify the result afterward.
