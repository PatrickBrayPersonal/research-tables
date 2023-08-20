"""
Evaluate model performance
functions must accept arguments **y** and **y_hat**
"""


import matplotlib.pyplot as plt
import mlflow
import numpy as np
from sklearn.calibration import calibration_curve
from sklearn.metrics import auc, precision_recall_curve, roc_curve

from table_extract.utils import error


def pr_curve(y: np.ndarray, y_hat: np.ndarray):
    precisions, recalls, thresholds = precision_recall_curve(y, y_hat)
    # plot the precision recall curve
    fig = plt.figure()
    plt.plot(recalls, precisions, "b-")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision Recall Curve for Binary Classification")
    mlflow.log_figure(fig, "test_pr_curve.png")
    plt.close()


def roc_auc_curve(y: np.ndarray, y_hat: np.ndarray):
    """calculate false positive rate and true positive rate for different thresholds


    Args:
        y (np.ndarray): _description_
        y_hat (np.ndarray): _description_
    """
    fpr, tpr, thresholds = roc_curve(y, y_hat)

    # calculate the area under the curve (AUC)
    roc_auc = auc(fpr, tpr)

    # plot the ROC curve
    fig = plt.figure()
    plt.plot(fpr, tpr, "b-")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC Curve (AUC = {round(roc_auc, 3)})")
    mlflow.log_figure(fig, "test_roc_auc_curve.png")
    plt.close()


def binary_violin(y: np.ndarray, y_hat: np.ndarray):
    """
    make a matplotlib violiplot of the binary probabilities predicted by y_hat
    """
    # make a violin plot in matplotlib using y and y_hat
    labels = y.unique()
    if len(labels) > 2:
        error(f"y must be binary {labels}")
    fig = plt.figure()
    plt.violinplot(
        (y_hat[y.values == labels[0]], y_hat[y.values == labels[1]]),
        positions=labels,
        showmeans=True,
    )
    plt.ylabel("Predicted Probability")
    plt.xlabel("True Label")
    plt.title("Binary Probability Violin Plot")
    mlflow.log_figure(fig, "test_binary_violin.png")
    plt.close()


def calibration_plot(y: np.ndarray, y_hat: np.ndarray):
    """Creates a calibration curve

    Args:
        y (np.ndarray):
        y_hat (np.ndarray):
    """
    # Get calibration curve
    fraction_of_positives, mean_predicted_value = calibration_curve(y, y_hat, n_bins=10)

    # Plot the calibration curve
    fig, ax1 = plt.subplots(figsize=(10, 8))

    # Plot the calibration curve
    ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
    ax1.plot(
        mean_predicted_value,
        fraction_of_positives,
        "s-",
        label="Calibration Curve",
    )
    ax1.set_ylabel("Fraction of positives")
    ax1.set_xlabel("Mean predicted value")
    ax1.legend(loc="upper left")
    ax1.set_title("Calibration plot")

    ax2 = ax1.twinx()
    ax2.hist(
        y_hat,
        range=(0, 1),
        bins=10,
        label="Predictions distribution",
        alpha=0.2,
        color="blue",
    )
    ax2.set_ylabel("Count")
    fig.tight_layout()
    mlflow.log_figure(fig, "calibration_curve.png")
    plt.close()


def regression_predictions(y: iter, y_hat: iter):
    """Plots predictions against real values for regression

    Args:
        y (iter): true labels
        y_hat (iter): predicted labels
    """
    fig = plt.figure()
    plt.scatter(y, y_hat)
    mlflow.log_figure(fig, "regression_predictions.png")
    plt.close()
