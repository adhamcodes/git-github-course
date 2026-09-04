# Module 5 Exercises — Fixing Mistakes and Recovery

Use only your disposable student lab. Read [`../../SAFETY.md`](../../SAFETY.md) before destructive commands.

## Challenge 1 — Choose the least destructive tool

Create four separate mistakes:

- staged the wrong file
- changed a tracked file but want its last committed version back
- committed the right change with the wrong message
- committed something that should be undone after it has been shared

For each case, state your intended final state **before** choosing a command.

## Challenge 2 — Stash deliberately

Create tracked work in progress, stash it, verify the working tree state, make an unrelated commit, then restore the stash and resolve any conflict if one appears.

Explain what the stash protected and what it did not.

## Challenge 3 — Recover a displaced commit

Create a disposable commit, move the branch away from it, then recover it using reflog by creating a recovery branch at the correct commit.

**Pass when:** you can prove the commit is reachable again and explain why reflog was useful.

## Boss check — Shared-history decision

Given a mistake already pushed to a branch another person may have pulled, explain why `revert` is usually safer than rewriting that history. Then demonstrate the safe repair in your practice repository.
