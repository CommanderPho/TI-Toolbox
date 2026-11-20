#!/usr/bin/env bash
set -euo pipefail

# List simulations for a subject (v3 layout: tit.paths.PathManager).

script_dir="$(cd -- "$(dirname "$0")" && pwd)"

# Prefer repo-local package root so `import tit` works without an install.
export PYTHONPATH="${script_dir}${PYTHONPATH:+:${PYTHONPATH}}"

subject_id="${1:-phohale}"
export SUBJECT_ID="$subject_id"

if [ -z "${PROJECT_DIR:-}" ] && [ -z "${PROJECT_DIR_NAME:-}" ]; then
  echo "Warning: PROJECT_DIR / PROJECT_DIR_NAME is not set; PathManager may return an empty list." >&2
fi

python_bin="simnibs_python"
if ! command -v "$python_bin" >/dev/null 2>&1; then
  python_bin="python"
fi

"$python_bin" - <<'PYCODE'
import os
from tit.paths import PathManager

subject = os.environ.get("SUBJECT_ID", "phohale")
pm = PathManager()
sims = pm.list_simulations(subject)
print(f"Available simulations for {subject}: {sims}")
PYCODE
