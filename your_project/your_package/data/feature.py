"""
Register feature engineering functions
Accept a dataframe **df** and return a Series
"""
from pandas import DataFrame, Series


def pattern_std(df: DataFrame, pattern: str) -> Series:
    """Calculate the standard deviation of columns matching a pattern
    returns standard deviation for each row in the dataframe

    Args:
        df (DataFrame): _description_
        pattern (str): _description_

    Returns:
        Series: _description_
    """
    return df.filter(regex=pattern).std(axis=1)
