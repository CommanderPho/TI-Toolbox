"""Unit tests for ``tit.jobs.command_history`` and the settings toggle that gates it."""

from __future__ import annotations

from pathlib import Path

from tit.jobs.command_history import append_command_history, format_command, history_path
from tit.server.routes import settings as settings_mod


def test_format_command_quotes_spaces() -> None:
    assert format_command(["simnibs_python", "-m", "tit.sim", "/tmp/my config.json"]) == (
        "simnibs_python -m tit.sim '/tmp/my config.json'"
    )


def test_append_command_history_writes_line(tmp_path: Path) -> None:
    path = append_command_history(
        str(tmp_path),
        job_id="abc123",
        kind="sim",
        argv=["simnibs_python", "-m", "tit.sim", "cfg.json"],
    )
    assert path == history_path(str(tmp_path))
    text = Path(path).read_text(encoding="utf-8")
    assert "abc123" in text
    assert "sim" in text
    assert "simnibs_python -m tit.sim cfg.json" in text


def test_append_command_history_skips_empty_argv(tmp_path: Path) -> None:
    assert append_command_history(str(tmp_path), job_id="x", kind="sim", argv=[]) is None
    assert not (tmp_path / "command_history.log").exists()


def test_command_history_logging_setting_roundtrip(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(
        settings_mod,
        "_project_settings_path",
        lambda: str(tmp_path / "settings.json"),
    )
    assert settings_mod.command_history_logging() is False
    settings_mod._save_project_settings(
        {
            "panels": [],
            "theme": "system",
            "agent_auto_submit": False,
            "command_history_logging": True,
        }
    )
    assert settings_mod.command_history_logging() is True
    body = settings_mod._read_settings()
    assert body["command_history_logging"] is True
