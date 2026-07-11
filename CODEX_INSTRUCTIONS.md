# Codex instructions: publish this project as a GitHub repository

## Goal

Turn the current folder into a clean, public-facing research portfolio repository named:

```text
hurricane-resilient-supply-chain
```

The repository should present the project professionally without changing the scientific results.

## Important constraints

1. **Do not invent, recompute, or rewrite numerical findings.** Treat the values already stated in `README.md` and stored under `results/` as the approved public results.
2. **Do not upload the raw file `ibtracs_NA.csv`.** It is intentionally excluded in `.gitignore` and must be downloaded from NOAA/NCEI by users who want to rebuild the pipeline.
3. **Do not restore files from old folders, checkpoints, drafts, or discarded outputs.** This ZIP already contains the curated public version.
4. **Do not execute Gurobi optimization cells unless a valid Gurobi installation and license are available.** Saved tables and figures are provided for inspection.
5. **Do not select a software license without asking the user.** Choosing a license changes reuse permissions.
6. Keep the repository in English, because it will be used for international graduate applications and research presentation.
7. Preserve the current research framing: this is a comparison of decision value across risk representations, not a claim that complex ML unconditionally dominates simpler models.

## Repository checks

Run:

```bash
python scripts/validate_repository.py
```

Do not publish until the script exits successfully.

Also inspect the staged files before committing:

```bash
git status
git diff --cached --stat
```

Confirm that the raw IBTrACS CSV, local virtual environments, notebook checkpoints, local absolute paths, and discarded result folders are absent.

## GitHub publishing workflow

1. Confirm that the authenticated GitHub account is `Evelyn-R7`; do not publish under a different account.
2. Confirm that `PROFILE_SNIPPET.md` links to `https://github.com/Evelyn-R7/hurricane-resilient-supply-chain`.
3. Initialize Git if this folder is not already a repository.
4. Use `main` as the default branch.
5. Create a **public** GitHub repository named `hurricane-resilient-supply-chain` under `Evelyn-R7`.
6. Commit the curated project files with a clear initial commit message, for example:

```text
Add hurricane-resilient supply chain research project
```

7. Push the `main` branch.
8. Add a concise GitHub repository description:

```text
Comparing static, interpretable, and ML-based hurricane risk representations in two-stage CVaR supply chain design.
```

9. Add relevant repository topics:

```text
supply-chain-resilience
hurricane-risk
stochastic-optimization
cvar
machine-learning
gurobi
scenario-reduction
predict-then-optimize
```

10. Verify that the README image, Mermaid pipeline, tables, citations, and links render correctly on GitHub.
11. Do not enable GitHub Pages unless the user asks for a separate website.

## GitHub profile integration

After the project repository is live:

1. Open the profile repository `Evelyn-R7/Evelyn-R7`.
2. Read its current README before editing.
3. Integrate the project block from `PROFILE_SNIPPET.md` into the existing project section, preserving all current content unless a duplicate must be replaced.
4. Use the live repository URL already present in the snippet.
5. Commit and push the profile README update separately with a clear message.
6. Recommend pinning the project repository on the profile, but do not remove another pinned repository without the user's instruction.

This project demonstrates an end-to-end research workflow spanning public-data engineering, predictive modeling, scenario construction, and stochastic optimization.

## Final report to the user

After publishing, report:

- project repository URL;
- project branch and latest commit;
- profile repository URL and profile README commit;
- validation result;
- whether the repository is public or private;
- any placeholder that still needs user input;
- any step not completed and the exact reason.
