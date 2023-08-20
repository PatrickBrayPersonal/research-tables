import os
import shutil
import sys
from pathlib import Path

import mlflow
import pandas as pd
from loguru import logger
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline


def error(msg: str):
    """Logs and raises a RuntimeError

    Args:
        msg (str): error message

    Raises:
        RuntimeError: _description_
    """
    logger.error(msg)
    raise RuntimeError(msg)


def pipeline_to_name(pipeline: Pipeline, delim: str = "-") -> str:
    """Converts an sklearn pipeline into a string
    describing its components

    Args:
        pipeline (Pipeline): sklearn pipeline
        delim (str, optional): string seperator. Defaults to "-".

    Returns:
        _type_: _description_
    """
    return delim.join([p[0] for p in pipeline.steps])


def log_config(output_dir: Path):
    mlflow.log_artifact(output_dir)


def log_script(path: str):
    script_path = get_script_path()
    shutil.copyfile(script_path, Path(path) / script_path.name)


def flatten_list(init_list: list):
    return [j for sub in init_list for j in sub]


def get_script_path() -> Path:
    # sys.argv[0] is the name of the script that was first executed
    script_name = sys.argv[0]

    # Use os.path.abspath to get the absolute path of the script
    return Path(os.path.abspath(script_name))


def log_best_params(model: BaseEstimator):
    if hasattr(model, "named_steps"):
        model = list(model.named_steps.values())[-1]
        return log_best_params(model)
    elif hasattr(model, "calibrated_classifiers_"):
        model = model.calibrated_classifiers_[0].estimator
        return log_best_params(model)
    elif hasattr(model, "best_estimator_"):
        # in case wrapped in hyperparameter tuner
        best_params = {f"best_{k}": v for k, v in model.best_params_.items()}
        logger.info(str(best_params))
        mlflow.log_params(best_params)
    else:
        logger.warning(f"Best params of {model} not found")


def log_feature_importance(model: BaseEstimator, columns: list, path: str):
    out_path = f"{path}/coefficients.csv"
    model = sk_unwrap(model)

    if hasattr(model, "coef_"):
        coeffs = list(model.coef_.reshape(-1))
        coef_df = pd.DataFrame(
            {"coef_" + feat: [coef] for coef, feat in zip(coeffs, columns)}
        ).T
        coef_df.reset_index().to_csv(out_path, index=True)
        logger.info(str(coef_df))
        mlflow.log_artifact(out_path)


def log_metric(metric: str, performance: any):
    if isinstance(performance, float):
        mlflow.log_metric(metric, performance)
    log_string = f"{metric}: {str(performance)}"
    logger.info(log_string)


def sk_unwrap(model: BaseEstimator) -> BaseEstimator:
    """unwraps models that are wrapped in tuners or other CV objects

    Args:
        model (BaseEstimator): _description_
    """
    if hasattr(model, "named_steps"):
        model = list(model.named_steps.values())[-1]
        return sk_unwrap(model)
    if hasattr(model, "calibrated_classifiers_"):
        model = model.calibrated_classifiers_[0].estimator
        return sk_unwrap(model)
    if hasattr(model, "best_estimator_"):
        # in case wrapped in hyperparameter tuner
        model = model.best_estimator_
        return sk_unwrap(model)
    else:
        return model


def make_logfile(directory: str, filename: str):
    logger.add(f"{directory}/{os.path.basename(filename).split('.')[0]}.log")
