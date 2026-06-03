"""Excel loading helpers for SPC input data."""
import pandas as pd
from pathlib import Path


def load_excel(filepath: str | Path, sheet_name: str = 0) -> pd.DataFrame:
    """
    Load an Excel file into a pandas DataFrame.

    Args:
        filepath: Path to the .xlsx file.
        sheet_name: Sheet name or index (default: first sheet).

    Returns:
        DataFrame of the sheet contents.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Excel file not found: {path}")
    if path.suffix not in (".xlsx", ".xls"):
        raise ValueError(f"Expected .xlsx or .xls, got: {path.suffix}")

    df = pd.read_excel(path, sheet_name=sheet_name, engine="openpyxl")
    print(f"Loaded {len(df)} rows from {path.name} (sheet: {sheet_name})")
    return df
