#!/usr/bin/env python3

import argparse
import pandas as pd
import numpy as np


def summarize_csv(file_path):
    df = pd.read_csv(file_path)
    df['ResponseTimeMs'] = df['ResponseTime'] / 1000  # µs → ms

    summary = {
        'Total Requests': len(df),
        'Successful Requests': df['Success'].sum(),
        'Failed Requests': len(df) - df['Success'].sum(),
        'Average Response Time (ms)': round(df['ResponseTimeMs'].mean(), 2),
        'Min Response Time (ms)': df['ResponseTimeMs'].min(),
        'Max Response Time (ms)': df['ResponseTimeMs'].max(),
        'P95 Response Time (ms)': np.percentile(df['ResponseTimeMs'], 95),
        'Error Rate (%)': round((~df['Success']).sum() / len(df) * 100, 2)
    }

    print("\nLoad Test Summary:\n" + "-" * 25)
    for key, value in summary.items():
        print(f"{key:<30} {value}")
    print("-" * 25)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize Syncload CSV results")
    parser.add_argument("--file", required=True, help="Path to CSV file")
    args = parser.parse_args()

    summarize_csv(args.file)
