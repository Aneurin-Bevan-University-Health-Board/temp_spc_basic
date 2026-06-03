"""Tests for Excel loader — uses a synthetic test file."""
import pandas as pd
import pytest
from pathlib import Path
from src.excel_loader import load_excel


def test_load_excel_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_excel("nonexistent.xlsx")


def test_load_excel_wrong_extension(tmp_path):
    bad_file = tmp_path / "test.txt"
    bad_file.write_text("hello")
    with pytest.raises(ValueError):
        load_excel(bad_file)


def test_load_excel_success(tmp_path):
    # Create a minimal xlsx for testing
    df_in = pd.DataFrame({"metric": [1, 2, 3], "label": ["a", "b", "c"]})
    out = tmp_path / "test.xlsx"
    df_in.to_excel(out, index=False, engine="openpyxl")

    df_out = load_excel(out)
    assert len(df_out) == 3
    assert "metric" in df_out.columns
