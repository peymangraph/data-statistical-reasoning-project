"""Download and freeze the San Francisco 311 dataset used for Project 2.

This script downloads the public DataSF view `syr9-3867` as CSV and saves the
exact snapshot beside `analysis.ipynb` as `sf311_cases.csv`.
"""

from pathlib import Path

import pandas as pd

DATA_URL = "https://data.sfgov.org/resource/syr9-3867.csv?$limit=50000"
OUTPUT_FILE = Path(__file__).resolve().parent / "sf311_cases.csv"


def main() -> None:
    """Download the public SF311 CSV snapshot and validate rubric minimums."""
    df = pd.read_csv(DATA_URL)

    if len(df) < 500:
        raise ValueError(f"Expected at least 500 rows, received {len(df):,}.")
    if df.shape[1] < 6:
        raise ValueError(f"Expected at least 6 columns, received {df.shape[1]}.")

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved {len(df):,} rows and {df.shape[1]} columns to {OUTPUT_FILE}")
    print("Columns:")
    for column in df.columns:
        print(f"- {column}")


if __name__ == "__main__":
    main()
