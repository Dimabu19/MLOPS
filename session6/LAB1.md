# Lab 1 — Test and automate the SMS API

**Guided lab:** 25 minutes for API tests, then 35 minutes for GitHub Actions. Use the same `sms-service/` project throughout.

## A. Test the API

### 1. Set up

Open a terminal **inside `sms-service/`**. Create and activate the environment, then install the packages.

Windows PowerShell:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

macOS/Linux:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

TestClient calls the application directly. You do not need to start Uvicorn. Keep `model.joblib` beside `main.py`; importing the app loads the model.

### 2. Run the health test

Read `test_health` in `test_api.py`. It checks HTTP 200 and `{"status": "ok"}`.

```bash
python -m pytest -q test_api.py::test_health
```

Expected: **1 passed**. An `assert` defines what must be true.

### 3. Complete the core tests

In `test_valid_prediction`, replace `{"TODO"}` with `{"spam", "ham"}`. Keep the status and `label` checks. We check the allowed labels, not one guessed prediction for the synthetic example.

In `test_invalid_input`, keep the existing cases and add these two payloads to its list:

```python
{"message": None},
{"message": 123},
```

The schema already rejects missing, null, numeric, empty and whitespace-only messages with HTTP 422. Here, 422 is the expected result. The loop is one test function.

```bash
python -m pytest -q
```

Expected: **3 passed**. The original TODO intentionally fails until completed.

### 4. Test a new input limit

Our new application rule is **1–500 characters after trimming spaces**. This is a rule for this API, not a universal SMS limit.

Append to `test_api.py`:

```python
def test_maximum_length_is_accepted():
    response = client.post("/predict", json={"message": "x" * 500})
    assert response.status_code == 200
    assert response.json()["label"] in {"spam", "ham"}


def test_overlong_message_is_rejected():
    response = client.post("/predict", json={"message": "x" * 501})
    assert response.status_code == 422
```

Run `python -m pytest -q`. Expected **before adding the rule: 1 failed, 4 passed**. The overlong-message test detects a requirement the starter does not yet enforce.

In `main.py`, update only the request constraint:

```python
class SMSRequest(BaseModel):
    message: Annotated[str, StringConstraints(
        strip_whitespace=True, min_length=1, max_length=500
    )]
```

Keep the other application code. Run `python -m pytest -q` again. Expected: **5 passed**.

These tests check API behavior; they do not measure precision or recall. Continue with these completed files.

## B. Automate the tests and Docker build

### 5. Prepare your repository and workflow

Create an **empty repository under your own GitHub account**, for example `sms-api-ci`. Leave the README, license and `.gitignore` initialization options unselected. Copy its repository URL for the push step.

Your local repository root will be the existing **`sms-service/` folder**, directly containing `main.py`, the model and tests. Keep the terminal there. The handout's outer folder is not the repository root.

In your editor, create `.github/workflows/ci.yml` inside `sms-service/`, including the two directories. Paste:

```yaml
name: SMS API CI

on: [TODO_TRIGGER]

permissions:
  contents: read

jobs:
  check-and-build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v7.0.1

      - name: Set up Python
        uses: actions/setup-python@v7.1.0
        with:
          python-version: "TODO_PYTHON_VERSION"

      - name: Install dependencies
        run: python -m pip install -r requirements-dev.txt

      - name: Run API tests
        run: TODO_TEST_COMMAND

      - name: Build Docker image
        run: TODO_BUILD_COMMAND
```

Complete the four TODOs **before pushing**:

| Placeholder | Replace with | Why |
| --- | --- | --- |
| `TODO_TRIGGER` | `push` | Check each pushed change. |
| `TODO_PYTHON_VERSION` | `3.10` | Match the supplied project. Keep the quotes. |
| `TODO_TEST_COMMAND` | `python -m pytest -q` | Run the same local tests. |
| `TODO_BUILD_COMMAND` | `docker build -f dockerfile -t sms-api:ci .` | Build the image after tests pass. |

Checkout brings your files onto the runner; setup-python selects Python. Installing `requirements-dev.txt` includes both runtime and test packages. The final `.` in the build command means the repository root is the build context. `-f dockerfile` selects the lowercase filename.

### 6. Commit and push

Run from **`sms-service/`**, which should be your own working copy outside another repository:

```bash
git init
git branch -M main
git add main.py model.joblib requirements.txt requirements-dev.txt test_api.py dockerfile .dockerignore .gitignore .github/workflows/ci.yml
git status --short
```

Check that the model and workflow are staged and no TODO remains in either the label assertion or YAML. The local `.venv/` should stay out of Git.

```bash
git commit -m "Add SMS API tests and CI"
git remote add origin "PASTE_YOUR_REPOSITORY_URL_HERE"
git push -u origin main
```

Replace the quoted URL placeholder with the actual URL of your empty repository. Use normal GitHub authentication. Your password or token does not belong in the YAML.

### 7. Inspect the run

On GitHub, confirm the model and workflow appear in **Code**. Open **Actions → SMS API CI → your pushed commit → check-and-build**.

Find:

- **Run API tests:** `5 passed`.
- **Build Docker image:** successful build of `sms-api:ci`.
- **Overall job:** success.

If a step fails, read its error, correct the file, then commit and push the correction. Inspect the new commit's run. Re-running an old run does not include unpushed edits.

**Done:** keep this project and repository for Lab 2. The image was built on the runner; it was not published, deployed or saved as a downloadable release. No model training occurs.

## Quick troubleshooting

| Problem | Check |
| --- | --- |
| Missing pytest/HTTPX | Activate the lab environment and install `requirements-dev.txt`. |
| `main` or model not found | Run from the folder containing `main.py` and `model.joblib`. |
| PowerShell blocks activation | Use `.\.venv\Scripts\python.exe` instead of `python` for pip/pytest commands. |
| Label TODO or overlong-input failure | Finish Stage A; do not weaken the assertions. |
| No workflow appears / invalid YAML | Check `.github/workflows/ci.yml`, indentation, completed TODOs and the pushed commit. |
| Model missing in CI | Confirm `model.joblib` is committed and visible on GitHub. |
| Docker build fails | Read the build log; check lowercase `dockerfile`, required files and final `.`. |
| Git requests name/email | Configure your own Git identity with instructor help, then retry the commit. |
| Push denied | Check your repository URL and GitHub sign-in with the instructor. |

If GitHub is unavailable, complete the local tests. With local Docker running, use `docker build -f dockerfile -t sms-api:ci .`. Record actual local results and mark hosted CI as **not verified**. An illustrative failed run has a failed test and skipped build; a successful run has passing tests and a completed build. Those descriptions are not evidence of your own hosted run.

References: [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/), [pytest](https://docs.pytest.org/en/stable/getting-started.html), [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
