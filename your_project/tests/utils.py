from typing import Tuple

import beavis
import pandas as pd

from your_package.data.read import file_to_df


def assert_df_equal(df: pd.DataFrame, soln: pd.DataFrame):
    """Throws a descriptive error if the dataframes are not equal

    Args:
        df (pd.DataFrame): _description_
        soln (pd.DataFrame): _description_
    """
    try:
        beavis.assert_pd_equality(df, soln)
    except Exception as e:
        print(e)
    pd.testing.assert_frame_equal(df, soln)


def read_prompt_soln(
    name: str, path: str = "tests/unit"
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    prompt = file_to_df(path + "/prompt/" + name)
    soln = file_to_df(path + "/solution/" + name)
    return prompt, soln
