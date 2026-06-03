"""Example SPC run script — update with your file path and abspc calls."""
from pathlib import Path
from src.excel_loader import load_excel

# Update this path to your input file
INPUT_FILE = Path("data/input/your_data.xlsx")


def main():
    df = load_excel(INPUT_FILE)
    print(df.head())

    # TODO: run abspc chart
    # from abspc import ...
    # result = abspc.run_chart(df["metric"], chart_type="xmr")
    # result.plot().savefig("data/output/chart.png")


if __name__ == "__main__":
    main()
