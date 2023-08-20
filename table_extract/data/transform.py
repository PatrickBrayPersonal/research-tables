"""
Register functions for filtering and transforming data
Accept a dataframe **df** and return a dataframe
"""
import os
from pathlib import Path

import pandas as pd
from loguru import logger
from pandas import DataFrame

from table_extract.data.read import file_to_df


def transformer(func):
    """
    Decorator for transform functions
    """

    def wrapper(df, *args, **kwargs):
        if isinstance(df, pd.DataFrame) and len(df) == 0:
            raise ValueError("The DataFrame passed is empty.")
        else:
            logger.info(f"Running Transform: {func.__name__}")
            return func(df, *args, **kwargs)

    return wrapper


@transformer
def drop_pattern(df: DataFrame, pattern: str) -> DataFrame:
    """Drops columns from the dataframe that match the regex pattern provided

    Args:
        df (DataFrame):
        pattern (str): regex drop pattern

    Returns:
        DataFrame:
    """
    return df.drop(columns=df.columns[df.columns.str.contains(pattern)])


@transformer
def select_pattern(df: DataFrame, pattern: str) -> DataFrame:
    """Selects columns from the dataframe that match the regex pattern provided

    Args:
        df (DataFrame):
        pattern (str): regex select pattern

    Returns:
        DataFrame:
    """
    return df.filter(regex=pattern)


@transformer
def bar_crawl_join(df):
    path = Path("data/bar_crawl/raw/clean_tac")
    dfs = []
    for f in os.listdir(path):
        tac = file_to_df(str(path / f))
        tac["pid"] = f[0:6]
        dfs.append(tac)
    tac = pd.concat(dfs, ignore_index=True)
    tac_agg = tac.groupby("pid")["TAC_Reading"].max()
    return pd.merge(df, tac_agg, left_on="pid", right_index=True)
