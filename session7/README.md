# Session 7 — Start here

Use this folder for all four labs. Work on your own copy and keep your answers.

All SMS, incidents and service facts are synthetic classroom examples. No live API, trained model, AWS, Docker or GitHub setup is needed.

## Parts, objectives and main goals

| Part | Objective | Main goals |
| --- | --- | --- |
| 1. What should we monitor? | Distinguish service health from prediction quality. | Identify service signals; Check predictions against labels; Use summaries to protect privacy. |
| 2. Drift in SMS messages | Explain changing SMS patterns and their limits. | Compare reference and current batches; Distinguish data and concept drift; Measure length and URL-like patterns. |
| 3. A simple monitoring report | Generate and interpret a simple monitoring report. | Prepare two monitoring features; Run Evidently and explain one chart; State what remains unknown. |
| 4. What happens after an alert? | Choose a response to a monitoring alert. | Inspect data and processing; Assess available quality evidence; Justify monitoring, investigation or retraining. |
| 5. Guided lab and recap | Investigate an SMS incident and justify an action. | Compare batches and interpret drift; Separate observations from unknowns; Submit a report and decision. |

## Work in this order

| Guide | Working folder | Hands-on time | Task |
| --- | --- | ---: | --- |
| [LAB1.md](LAB1.md) | lab1/ | 10 min | Find incorrect classifications despite HTTP 200. |
| [LAB2.md](LAB2.md) | lab2/ | 15 min | Complete one mean calculation and compare SMS features. |
| [LAB3.md](LAB3.md) | lab3/ | 25 min | Generate or inspect a report and explain one chart. |
| [LAB4.md](LAB4.md) | lab4/ | 45 min | Investigate a new incident and justify an action. |

The complete session is 180 minutes, including 95 minutes of hands-on work. Prepare Python 3.10 and the pinned packages before class for Labs 2–4. Lab 1 needs only a spreadsheet or text editor. Use a separate environment from the existing saved model.

Open each working folder in your editor and run that guide’s commands there. Keep the supplied folder structure. Notebook cells use their lab folder as the working directory; run_report.py also works from elsewhere.

## File guide

| Files | Use |
| --- | --- |
| LAB1.md–LAB4.md | Setup, timing, tasks and fallback instructions. |
| lab1/records.csv, WORKSHEET.md | Six simulated requests and an answer sheet. |
| lab2/starter.py, reference.csv, current.csv | Supplied features with one TODO and two ten-message batches. |
| lab2/requirements.txt, WORKSHEET.md, EXPECTED_RESULTS.md | Setup, interpretation and calculated fallback. |
| lab3/monitoring_report.ipynb, lab4/monitoring_incident.ipynb | Short complete notebooks. |
| lab3/ and lab4/monitoring.py, run_report.py | Feature/report code and complete runnable scripts. |
| lab3/ and lab4/requirements.txt | Same tested packages: Evidently 0.7.23, pandas 2.2.3, NumPy 2.2.6, ipykernel 7.3.0. |
| lab3/ and lab4/data/ | Synthetic reference/current CSVs. |
| lab3/ and lab4/output/ | Prepared HTML, feature summary and actual chart for fallback. |
| lab3/WORKSHEET.md | Short interpretation submission. |
| lab4/INCIDENT.md, HINTS.md, submission_template.md | Incident evidence, optional hints and a 3–5 sentence decision. |
| lab3/ and lab4/TROUBLESHOOTING.md | Brief fixes and the fallback procedure. |

If setup fails, inspect the prepared report, chart and summary and answer the same questions. Data drift describes changing inputs; reliable labels and matching predictions are needed to judge quality.
