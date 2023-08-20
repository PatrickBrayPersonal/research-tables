"""
Register feature engineering functions
Accept a dataframe **df** and return a Series
"""
import polars as pl

def pattern_std(df: pl.DataFrame, pattern: str) -> pl.Series:
    """
    Row wise calculations not supported in polars
    """
    raise NotImplementedError("This is not available in Polars")