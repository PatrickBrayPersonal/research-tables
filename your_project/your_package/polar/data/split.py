"""
Functions used for splitting data
Must accept arguments **df** and **label**
"""

from sklearn.model_selection import train_test_split
import polars as pl

def default(df: pl.DataFrame, label: str, train_size):
    X = df.drop(label)
    y = df[label]
    return train_test_split(X, y, train_size=train_size, shuffle=True)
