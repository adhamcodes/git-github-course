# Module 2 Exercises — Branching

Use the disposable student lab.

## Challenge 1 — Predict branch movement

Create two commits on `main`, create a feature branch, add two more commits there, and draw the commit graph you expect before inspecting it.

Then run:

```bash
git log --oneline --graph --decorate --all
```

Explain what the branch names point to.

## Challenge 2 — Fast-forward vs merge commit

Produce one merge that can fast-forward and one merge where both branches have diverged.

Before each merge, predict the resulting graph.

**Pass when:** you can explain why the outcomes differ without describing branches as folders or copies.

## Challenge 3 — Branch cleanup

Merge a finished feature, verify the work is reachable from `main`, then delete the local feature branch.

Explain why deleting the branch name does not delete commits that remain reachable from `main`.

## Boss check — Unknown graph

Create a small history with at least three branches and six commits. Leave it for a while, return without notes, inspect it, and explain which work is merged and which work remains isolated before running a merge command.
