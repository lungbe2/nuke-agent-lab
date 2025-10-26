import pytest
from pathlib import Path
from tools import nuke_agent as na


def test_load_code_and_preview(tmp_path: Path):
    p = tmp_path / "t.txt"
    p.write_text("a" * 500, encoding="utf-8")
    code = na.load_code(p)
    assert len(code) == 500
    preview = na.prepare_preview(code, length=50)
    assert preview.endswith("...")
    assert len(preview) == 53  # 50 chars + '...'


def test_get_nuke_prompt_known_and_unknown():
    assert isinstance(na.get_nuke_prompt("vibe-refine"), str)
    unk = na.get_nuke_prompt("no-such-nuke")
    assert "Unknown nuke" in unk


def test_run_nuke_returns_structure(tmp_path: Path):
    p = tmp_path / "script.py"
    p.write_text("print('hi')", encoding="utf-8")
    res = na.run_nuke(p, "vibe-refine")
    assert res["file"].endswith("script.py")
    assert "prompt" in res and "preview" in res and isinstance(res["code_len"], int)


def test_load_code_missing(tmp_path: Path):
    missing = tmp_path / "missing.txt"
    with pytest.raises(FileNotFoundError):
        na.load_code(missing)