# SPC Basic Template

Starter project for Statistical Process Control (SPC) work at ABUHB using the `abspc` package from the test PyPI index, with Excel upload support via `openpyxl`.

---

## Quick Start

1. Click **Use this template** → create your repo
2. Open in GitHub Codespaces or clone locally
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Place your Excel data file in `data/input/` (gitignored — will not be committed)
5. Run the example script:

```bash
python scripts/run_spc.py
```

---

## Folder Structure

```
.
├── src/                 # SPC logic and helpers
├── scripts/             # Run scripts
├── notebooks/           # Exploration notebooks
├── data/                # Input/output data (gitignored)
│   ├── input/           # Drop Excel files here
│   └── output/          # Generated charts and reports
├── tests/
├── requirements.txt
└── .env.example
```

> **Important:** `data/` and all Excel/CSV files are gitignored. Never commit patient or sensitive data.

---

## Installing `abspc` from Test PyPI

`abspc` is hosted on the [Test PyPI index](https://test.pypi.org/). Install it alongside dependencies from the main PyPI index:

```bash
pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  abspc
```

This is already wired into `requirements.txt` via pip's `--extra-index-url` mechanism. To install everything:

```bash
pip install -r requirements.txt
```

If you need a specific version:
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ abspc==0.x.x
```

---

## Reading Excel Files

```python
import openpyxl

wb = openpyxl.load_workbook("data/input/your_file.xlsx")
ws = wb.active

for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

Or with pandas:

```python
import pandas as pd

df = pd.read_excel("data/input/your_file.xlsx", sheet_name="Sheet1")
print(df.head())
```

---

## Example SPC Workflow

```python
import pandas as pd
from abspc import ...  # import the relevant abspc functions

# 1. Load data
df = pd.read_excel("data/input/your_file.xlsx")

# 2. Run SPC calculation
# result = abspc.run_chart(df["metric_column"], chart_type="xmr")

# 3. Output / visualise
# result.plot().savefig("data/output/chart.png")
```

Replace the commented lines with the actual `abspc` API once installed.

---

## Important: Data Gitignore

The `.gitignore` in this repo excludes:
- `data/` directory
- All `.xlsx`, `.xls`, `.csv`, `.parquet` files
- Any file matching `*patient*`, `*sensitive*`

This is intentional. **Never override this to commit data files.**

---

## Running Tests

```bash
pytest tests/
```
