import mlflow
import numpy as np
import pandas as pd


def binary_class(df: pd.DataFrame, model_name: str, model_version: int) -> np.ndarray:
    clf = mlflow.sklearn.load_model(model_uri=f"models:/{model_name}/{model_version}")
    y_hat = clf.predict_proba(df[clf.feature_names_in_])[:, 1]
    return y_hat
