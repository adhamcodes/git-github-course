# Module 6 Exercises — Real-World Git

Use the disposable student lab. Read [`../../SAFETY.md`](../../SAFETY.md) before rewriting history.

## Challenge 1 — Conflict from divergence

Create a genuine same-line conflict by changing one committed line differently on two diverged branches. Before resolving it, explain:

- what `HEAD` represents
- what each conflict side contains
- what final content you intend to keep

Resolve, commit, and prove the working tree is clean.

## Challenge 2 — Rebase boundary

Rebase an unpublished feature branch onto updated `main`. Compare commit IDs before and after.

Then explain why doing the same rewrite to a shared branch can disrupt collaborators.

## Challenge 3 — Release evidence

Create an annotated version tag in your lab, inspect it, push it, and create a GitHub Release with concise notes tied to actual changes.

## Challenge 4 — Controlled CI lab

Complete the self-contained exercise in [`../../examples/actions/README.md`](../../examples/actions/README.md). You must be able to explain the workflow trigger, job, steps, and why the intentionally failing test blocks the check.

## Boss check — Disaster lab

Combine at least three failures in one practice repository: a merge conflict, remote divergence, and a displaced commit recoverable through reflog. Diagnose before repairing.

**Pass when:** you can narrate repository state first, choose the least destructive appropriate operation, and verify the final graph and working tree.
