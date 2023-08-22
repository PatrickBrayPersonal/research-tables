import polars as pl
import re

def drop_pattern(df: pl.DataFrame, pattern: str) -> pl.DataFrame:
    """
    Returns a selection of the dataframe with columns dropped
    by the pattern provided
    Args:
        df (DataFrame):
        pattern (str): regex drop pattern

    Returns:k
        DataFrame:
    """
    pattern_false_cols = [col for col in df.columns if not re.match(pattern, col)]
    return df.select(pattern_false_cols)

def select_pattern(df: pl.DataFrame, pattern: str) -> pl.DataFrame:
    return df.select(pattern)