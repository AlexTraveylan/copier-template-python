import copier
from pathlib import Path
import itertools
import pytest

@pytest.mark.parametrize("is_ruff, is_mypy, is_pytest, is_vscode", itertools.product([True, False], repeat=4))
def test_copier(tmp_path: Path, is_ruff: bool, is_mypy: bool, is_pytest: bool, is_vscode: bool) -> None:
    answers = {
        "project_name": "test",
        "python_version": "3.13",
        "is_ruff": is_ruff,
        "is_mypy": is_mypy,
        "is_pytest": is_pytest,
        "is_vscode": is_vscode,
    }

    copier.run_copy(src_path=str(Path(__file__).parents[1]), dst_path=tmp_path, data=answers)

    assert (tmp_path / "README.md").exists() is True
    assert (tmp_path / "pyproject.toml").exists() is True
    assert (tmp_path / "main.py").exists() is True
    assert (tmp_path / ".python-version").exists() is True
    assert (tmp_path / ".pre-commit-config.yaml").exists() is True
    assert (tmp_path / ".gitignore").exists() is True
    assert (tmp_path / "tests").exists() is True
    assert (tmp_path / "src").exists() is True
    assert (tmp_path / ".vscode").exists() is is_vscode
    assert (tmp_path / ".github").exists() is True