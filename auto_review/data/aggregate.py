"""
Functions that accept a data parameter **df**
and return a dataframe grouped by the column **column_id**
"""

from pandas import DataFrame
from tsfresh import extract_features

from auto_review.data.transform import transformer


@transformer
def tsfresh(
    df: DataFrame,
    column_id: str,
    column_sort: str,
    default_fc_parameters: dict = None,
    kind_to_fc_parameters: dict = None,
    **kwargs
) -> DataFrame:
    """
    See [tsfresh docs](https://tsfresh.readthedocs.io/en/latest/text/feature_extraction_settings.html) for more details
    Extract features from

    * a :class:`pandas.DataFrame` containing the different time series

    or

    * a dictionary of :class:`pandas.DataFrame` each containing one type of time series

    In both cases a :class:`pandas.DataFrame` with the calculated features will be returned.

    For a list of all the calculated time series features, please see the
    :class:`~tsfresh.feature_extraction.settings.ComprehensiveFCParameters` class,
    which is used to control which features with which parameters are calculated.

    For a detailed explanation of the different parameters (e.g. the columns) and data formats
    please see :ref:`data-formats-label`.

    Examples
    ========

    >>> X = tsfresh(df, column_id='id', column_sort='time', default_fc_parameters='config/tsfresh/ts_default.yaml')

    :param df: The pandas.DataFrame with the time series to compute the features for, or a
            dictionary of pandas.DataFrames.
    :type timeseries_container: pandas.DataFrame or dict

    :param default_fc_parameters: path to yaml mapping from feature calculator names to parameters. Only those names
           which are keys in this yaml will be calculated. See the class:`ComprehensiveFCParameters` for
           more information.
    :type default_fc_parameters: str

    :param kind_to_fc_parameters: path to yaml mapping from kind names to objects of the same type as the ones for
            default_fc_parameters. If you put a kind as a key here, the fc_parameters
            object (which is the value), will be used instead of the default_fc_parameters. This means that kinds, for
            which kind_of_fc_parameters doe not have any entries, will be ignored by the feature selection.
    :type kind_to_fc_parameters: str

    :param column_id: The name of the id column to group by. Please see :ref:`data-formats-label`.
    :type column_id: str

    :param column_sort: The name of the sort column. Please see :ref:`data-formats-label`.
    :type column_sort: str

    :param column_kind: The name of the column keeping record on the kind of the value.
            Please see :ref:`data-formats-label`.
    :type column_kind: str

    :param column_value: The name for the column keeping the value itself. Please see :ref:`data-formats-label`.
    :type column_value: str

    :param n_jobs: The number of processes to use for parallelization. If zero, no parallelization is used.
    :type n_jobs: int

    :param chunksize: The size of one chunk that is submitted to the worker
        process for the parallelisation.  Where one chunk is defined as a
        singular time series for one id and one kind. If you set the chunksize
        to 10, then it means that one task is to calculate all features for 10
        time series.  If it is set it to None, depending on distributor,
        heuristics are used to find the optimal chunksize. If you get out of
        memory exceptions, you can try it with the dask distributor and a
        smaller chunksize.
    :type chunksize: None or int

    :param show_warnings: Show warnings during the feature extraction (needed for debugging of calculators).
    :type show_warnings: bool

    :param disable_progressbar: Do not show a progressbar while doing the calculation.
    :type disable_progressbar: bool

    :param impute_function: None, if no imputing should happen or the function to call for
        imputing the result dataframe. Imputing will never happen on the input data.
    :type impute_function: None or callable

    :param profile: Turn on profiling during feature extraction
    :type profile: bool

    :param profiling_sorting: How to sort the profiling results (see the documentation of the profiling package for
           more information)
    :type profiling_sorting: basestring

    :param profiling_filename: Where to save the profiling results.
    :type profiling_filename: basestring

    :param distributor: Advanced parameter: set this to a class name that you want to use as a
             distributor. See the utilities/distribution.py for more information. Leave to None, if you want
             TSFresh to choose the best distributor.
    :type distributor: class

    :return: The (maybe imputed) DataFrame containing extracted features.
    :rtype: pandas.DataFrame
    """
    agg = extract_features(
        df,
        kind_to_fc_parameters=kind_to_fc_parameters,
        default_fc_parameters=default_fc_parameters,
        column_id=column_id,
        column_sort=column_sort,
        **kwargs
    )
    return agg.reset_index()
