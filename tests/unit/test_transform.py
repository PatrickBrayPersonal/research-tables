"""
Unit Test the functions from table_extract/data/transform.py
"""


import fire

from tests.utils import assert_df_equal, read_prompt_soln
from table_extract.data.transform import drop_pattern, select_pattern


def test_drop_pattern():
    """
    Example Unit Test
    -----------------

    1. create a starting dataframe in csv
        tests/unit/prompt/drop_pattern.csv
    2. manually create the desired solution
        tests/unit/solution/drop_pattern.csv
    """
    # read in your prompt and solution tables
    df, soln = read_prompt_soln("drop_pattern.csv")
    # call your function to test, optionally with arguments
    df = drop_pattern(df, "test.*")
    # This function throws an error if the dataframes are not equal
    assert_df_equal(df, soln)


def test_select_pattern():
    df, soln = read_prompt_soln("select_pattern.csv")
    df = select_pattern(df, "test.*")
    assert_df_equal(df, soln)


if __name__ == "__main__":
    fire.Fire()
