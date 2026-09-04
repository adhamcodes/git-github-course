# Controlled GitHub Actions Lab

This lab removes the need to hunt for a random public workflow. Run it in your disposable `git-github-lab` repository.

## 1. Copy the demo

Copy these files into your student lab:

- `examples/actions/demo/app.py` → `app.py`
- `examples/actions/demo/tests/test_app.py` → `tests/test_app.py`
- `examples/actions/basic-python-ci.yml` → `.github/workflows/ci.yml`

Commit and push them.

## 2. Inspect before running

Open `.github/workflows/ci.yml` and identify:

- the events under `on`
- the job under `jobs`
- the runner
- each step
- the command that decides whether the check passes

## 3. Prove green

Open the Actions tab or the commit checks. Confirm the tests pass.

## 4. Break it deliberately

Change `add(2, 3)` in the test expectation so the test is wrong, commit, and push.

Predict the result before checking GitHub.

Confirm the workflow fails and inspect the failing test output.

## 5. Repair

Fix the test, commit, push, and verify the workflow returns to green.

## Pass condition

You can explain why CI is useful, what caused the red check, and why a green check only proves the checks that actually ran—not all possible correctness.
