# Session 6 — Start here

Use this folder for both labs. **Work on your own copy outside any existing Git repository.** Open `sms-service/` in your code editor; run lab commands from that folder.

## What you need

- **Python 3.10** and a code editor.
- **Git**, configured with your name/email, and a **GitHub account** with working sign-in/push access. You will create your own repository in Lab 1.
- **Internet access** to install packages and run GitHub Actions.
- **Optional: Docker locally.** The normal lab builds the image on GitHub's runner. Local Docker is needed only to repeat the build on your computer.

The trained model is included. The setup commands install the required Python packages.

## Work in this order

1. Follow [LAB1.md](LAB1.md): test the API, then automate tests and the Docker build.
2. Keep your completed project and repository.
3. Follow [LAB2.md](LAB2.md): choose one independent CI challenge.

## What each file is for

| File | Use |
| --- | --- |
| `README.md` | Start here; tools and file guide. |
| `LAB1.md` | Guided instructions for API testing and GitHub Actions. |
| `LAB2.md` | Independent challenge goals and completion criteria. |
| `sms-service/main.py` | FastAPI application; edit its input rule in Lab 1. |
| `sms-service/test_api.py` | Starter tests; complete and extend them. One TODO is intentional. |
| `sms-service/model.joblib` | Shared trained SMS model; keep beside `main.py`. |
| `sms-service/requirements.txt` | Application packages and their versions. |
| `sms-service/requirements-dev.txt` | Installs application packages plus pytest and HTTPX. Use this for setup. |
| `sms-service/dockerfile` | Instructions used to build the runtime image. Keep the lowercase filename. |
| `sms-service/.dockerignore` | Selects which files Docker receives. Keep it. |
| `sms-service/.gitignore` | Keeps your local environment and caches out of Git. Keep it. |

The last two files may be hidden in your file browser. Copy the whole starter folder, including them. Create `.github/workflows/ci.yml` during Lab 1; it is not supplied as a separate file.
