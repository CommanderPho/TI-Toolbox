# AI Coding Guidance for TI-Toolbox

Short, actionable notes for an AI coding agent to be immediately productive.

## Big picture
- Major components: CLI scripts (`ti-toolbox/cli/`), Simulator (`ti-toolbox/sim/`),
  Optimizers (`ti-toolbox/opt/`), Analyzers (`ti-toolbox/analyzer/`), GUI (`package/`).
- Data flow: optimizers (Flex-Search / Ex-Search) produce electrode mappings (`electrode_mapping.json`) that are fed into the Simulator for full-resolution runs. Outputs are placed under `derivatives/SimNIBS/...`.
- Why: heavy numerical work is separated (SimNIBS in Docker) from orchestration/analysis (Python code here) and the desktop GUI (Electron in `package/`).

## Critical workflows & commands
- Local test wrapper (host): `./tests/test.sh` — primary way to run tests. Use `--unit-only` for fast runs.
- Inside Dev container: `./tests/run_tests.sh` (container expects `simnibs_python` and SimNIBS present).
- GUI build: `cd package && npm install && npm run build`; dev run with `npm start`.
- Launch desktop app (helper): `./package/start-ti-toolbox.sh`; host+Docker integration via `./loader.sh` which uses `docker-compose.yml`.
- CI/test image: `idossha/ti-toolbox-test:latest` — tests run inside that image; do not run integration scripts directly on host.

## Project-specific conventions
- Always use `./tests/test.sh` from host — it mounts local code into the test image and runs CI-like tests. See `tests/README_TESTING.md` for details.
- Container mount path expectations: development mounts use `/development` inside containers (see `tests/run_tests.sh` and `loader.sh`).
- In-container Python entrypoint is `simnibs_python` (not plain `python`) for tests and scripts that use SimNIBS.
- CLI shell scripts in `ti-toolbox/cli/*.sh` are expected executable; test runner ensures `chmod +x` for these files.

## Integration points & external deps
- SimNIBS (FEM solver) — runs inside Docker; scripts call `simnibs_python`.
- FreeSurfer — required for some integration tests and GUI preprocessing flows.
- Docker / Docker Compose — `./loader.sh` and `docker-compose.yml` orchestrate services used during dev and by the GUI.
- Test image: `idossha/ti-toolbox-test:latest` contains SimNIBS, FreeSurfer, pytest, BATS.

## Common code patterns to follow
- Optimization → simulation pattern: see `ti-toolbox/opt/flex/` and `ti-toolbox/sim/TI.py` — Flex computes electrode positions, Simulator computes fields from montages.
- File locations: outputs written under `derivatives/SimNIBS/sub-{ID}/...` and `derivatives/temp/` for short-lived artifacts.
- Tests: unit tests are plain pytest Python files in `tests/`; integration tests use bash runners + BATS for output validation.

## Quick examples (copyable)
- Run unit tests (host):

  ./tests/test.sh --unit-only

- Full test suite (host):

  ./tests/test.sh --verbose

- Build GUI (dev machine):

  cd package
  npm install
  npm run build

- Start dev environment (desktop + containers):

  ./loader.sh

## Helpful files to inspect
- Architecture & flow: `docs/PIPELINE_FLOW.md`
- Test guidance: `tests/README_TESTING.md` and `tests/run_tests.sh`
- GUI packaging: `package/QUICK_START.md` and GitHub Action ` .github/workflows/release-build.yml`
- Launch helpers: `loader.sh` and `package/start-ti-toolbox.sh`

## What an agent should do first
1. Read `docs/PIPELINE_FLOW.md` to learn pipelines.
2. Run `./tests/test.sh --unit-only` locally to validate environment.
3. Read `ti-toolbox/opt/` and `ti-toolbox/sim/` to understand optimizer→simulator interfaces.

---
If any area is unclear or you want more examples (unit test patterns, optimization inputs/outputs), tell me which section to expand.
