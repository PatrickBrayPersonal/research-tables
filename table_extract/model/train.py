"""
Scripts for training models

must accept argument **model**
"""

import mlflow


def sklearn(model, X, y, **kwargs):
    """
    Fit the model to the training data.
    """

    mlflow.sklearn.autolog()
    model.fit(X, y, **kwargs)
    return model
