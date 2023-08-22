"""
Register functions for evaluating model performance
Integrated with mlflow experiment tracking
Must accept arguments **model**, **X**, and **y**
"""
import mlflow
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    log_loss,
    roc_auc_score,
)
from loguru import logger

from auto_review.model.visualize import binary_violin, pr_curve, roc_auc_curve


def evaluator(func):
    """
    TODO: Decorator for evaluate functions
    """

    def wrapper(df, *args, **kwargs):
        if isinstance(df, pd.DataFrame) and len(df) == 0:
            raise ValueError("The DataFrame passed is empty.")
        else:
            logger.info(f"Running Transform: {func.__name__}")
            return func(df, *args, **kwargs)

    return wrapper



def binary_class(model, X, y, **kwargs):
    """
    Evaluate the model on the test data.
    """
    y_hat = model.predict_proba(X)[:, 1]
    # Run mlflow autolog using the test data
    binary_metrics = [
        average_precision_score,
        brier_score_loss,
        log_loss,
        roc_auc_score,
    ]
    for metric in binary_metrics:
        mlflow.log_metric(metric.__name__, metric(y, y_hat))
    binary_vis = [roc_auc_curve, pr_curve, binary_violin]
    for vis in binary_vis:
        vis(y, y_hat)
