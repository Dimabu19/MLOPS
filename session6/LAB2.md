# Lab 2 — Independent CI challenge

**Time:** 47 minutes. Continue from your completed Lab 1 project: five passing tests, the 500-character rule, the saved model, and working CI. Work on a feature branch in your own training repository.

Choose **one** mission. Use documentation, experiment, and ask the instructor for one hint at a time.

## A — Reject unexpected request fields

The API currently ignores extra JSON fields. The team now wants client mistakes to be visible.

Your improvement must reject a valid `message` accompanied by an unexpected field with **HTTP 422**, while preserving normal requests and existing rules. Add a meaningful automated check and show that it detects the missing policy before the fix. This is a new policy, not a previously agreed requirement.

## B — Verify the response's JSON media type

The existing tests parse the prediction body without checking its declared media type.

Your improvement must check that successful prediction responses declare **`application/json`**, allowing valid media-type parameters. Preserve the status, field and allowed-label checks. Demonstrate detection of a controlled incorrect media type, then restore correct behavior. A synthetic message does not need one particular spam/ham result.

## C — Verify CI on pull requests

The workflow checks pushes. The team also wants changes proposed in pull requests checked.

Retain push checks and add pull-request checks using the same tests and Docker build. Show an actual run triggered by **pull-request activity**, not only an ordinary push. Demonstrate that a controlled failed test blocks the build, then restore passing tests and a successful build for the updated PR. You do not need to merge the PR.

## Success criteria

- Explain one meaningful gap and your improvement.
- Keep the baseline checks, dependencies and saved model.
- Show relevant detection/failure evidence and final passing results.
- Finish with local pytest passing and a successful GitHub Actions run and Docker build for the final commit.
- Explain what your evidence proves and its limits.

Different valid implementations are welcome. One mission is enough. No retraining, publishing, deployment or new service is required.

## Class discussion

**No submission or written report is required.** Be ready to briefly explain:

- Which mission you chose and what you changed.
- How your tests or workflow demonstrate the improvement.
- Your final pytest and CI/build results, including anything still unverified.

## References and access fallback

- [Pydantic configuration](https://pydantic.dev/docs/validation/latest/api/pydantic/config/)
- [FastAPI response headers](https://fastapi.tiangolo.com/advanced/response-headers/)
- [pytest assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [GitHub workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)

If GitHub is unavailable, investigate independently with local pytest and Docker where available, and keep your own results. Mark hosted run/build evidence as **not verified**. Mission C's actual event behavior still needs a hosted PR run; a local check or example log does not prove it.
