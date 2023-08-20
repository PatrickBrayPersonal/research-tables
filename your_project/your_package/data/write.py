"""
Register data writers
Accept a dataframe **df**
"""
from re import match

import pandas as pd

from your_package.utils import error


def df_to_file(df: pd.DataFrame, path: str, **kwargs):
    funcs = {
        r".*\.parquet": df.to_parquet,
        r".*\.p": df.to_pickle,
        r".*\.csv": df.to_csv,
        r".*\.xlsx": df.to_excel,
    }
    for pattern, func in funcs.items():
        if match(pattern, path) is not None:
            func(path, **kwargs)
            return True
    error(f"{path} does not match a known file pattern {', '.join(list(funcs.keys()))}")
