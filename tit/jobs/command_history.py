"""Project-level command history log and shell-escaped argv formatting.

When Settings → Project → command history logging is on, each admitted job appends one
line to ``command_history.log`` under the project directory so a run can be replayed
outside the desktop app. The same formatter feeds the job detail "Copy command" button.
"""

from __future__ import annotations

import os
import shlex
from datetime import datetime, timezone


HISTORY_FILENAME = "command_history.log"


def format_command(argv: list[str]) -> str:
    """POSIX shell-escaped command line suitable for pasting into bash (container)."""
    return shlex.join(argv)


def history_path(project_dir: str) -> str:
    return os.path.join(project_dir, HISTORY_FILENAME)


def append_command_history(
    project_dir: str,
    *,
    job_id: str,
    kind: str,
    argv: list[str],
) -> str | None:
    """Append one history line; return the log path, or ``None`` if the write failed.

    Line shape: ``<iso8601> <job_id> <kind> <shell-escaped argv>``.
    """
    if not project_dir or not argv:
        return None
    path = history_path(project_dir)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"{stamp} {job_id} {kind} {format_command(argv)}\n"
    try:
        os.makedirs(project_dir, exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        return None
    return path
