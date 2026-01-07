#!/usr/bin/env bash
set -euo pipefail

# List simulations for a subject without relying on a venv.

script_dir="$(cd -- "$(dirname "$0")" && pwd)"

ti_toolbox_dir="$script_dir/ti-toolbox"
if [ ! -d "$ti_toolbox_dir" ]; then
  ti_toolbox_dir="/mnt/c/Users/pho/repos/TI-Toolbox/ti-toolbox"
fi

if [ ! -d "$ti_toolbox_dir" ]; then
  echo "TI-Toolbox directory not found. Adjust ti_toolbox_dir in script." >&2
  exit 1
fi

export PYTHONPATH="${ti_toolbox_dir}:${PYTHONPATH:-}"

subject_id="${1:-phohale}"
export SUBJECT_ID="$subject_id"

if [ -z "${PROJECT_DIR_NAME:-}" ]; then
  echo "Warning: PROJECT_DIR_NAME is not set; PathManager may return an empty list." >&2
fi

python_bin="simnibs_python"
if ! command -v "$python_bin" >/dev/null 2>&1; then
  python_bin="python"
fi

"$python_bin" - <<'PYCODE'
import os
from core import PathManager

subject = os.environ.get("SUBJECT_ID", "phohale")
pm = PathManager()
sims = pm.list_simulations(subject)
print(f"Available simulations for {subject}: {sims}")
PYCODE