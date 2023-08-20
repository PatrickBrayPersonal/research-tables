"""
Register data readers
"""
from re import match

import polars as pl

from your_package.utils import error


def file_to_df(path: str, **kwargs):
    funcs = {
        r".*\.parquet": pl.read_parquet,
        r".*\.csv": pl.read_csv,
        r".*\.xlsx": pl.read_excel,
    }
    for pattern, func in funcs.items():
        if match(pattern, path) is not None:
            return func(path, **kwargs)
    error(f"{path} does not match a known file pattern {', '.join(list(funcs.keys()))}")
