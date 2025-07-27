import pytest
import shutil
from pathlib import Path

@pytest.fixture(autouse=True)
def clean_tmp_path(tmp_path: Path) -> None:
    shutil.rmtree(tmp_path)