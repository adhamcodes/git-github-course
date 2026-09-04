# Module 3 Exercises — Remotes

Use your disposable student lab plus its GitHub remote.

## Challenge 1 — Local vs remote truth

Create a local commit without pushing it. Then inspect:

```bash
git status
git log --oneline --decorate --graph --all
git branch -vv
```

Explain what exists locally and what GitHub does not know yet.

## Challenge 2 — Remote changes first

Make a harmless change on GitHub, then return to your local clone.

Do **not** immediately run `git pull`.

First fetch and inspect the difference between your local branch and its remote-tracking branch. Decide how to integrate only after you understand the state.

## Challenge 3 — Two clones

Clone the same practice repository into two separate folders. Make a commit in clone A and push it. In clone B, inspect the stale state, fetch, explain what changed, then integrate deliberately.

## Boss check — Divergence diagnosis

Create one unpublished local commit and one different remote commit so the branch diverges. Before integrating anything, draw the graph and explain your available choices.

**Pass when:** `fetch → inspect → decide` feels natural and `pull` is no longer a mystery command.
