import sys
sys.path.append('..')

import pandas as pd
import sqlalchemy
import io
import time
from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, average_precision_score
import scipy.sparse
import matplotlib.pyplot as plt

def plot_PR(y_test, pred):
    from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, average_precision_score
    precision, recall, _ = precision_recall_curve(y_test, pred)
    average_precision = average_precision_score(y_test, pred)

    plt.figure()
    plt.step(recall, precision, color='b', alpha=0.2,
             where='post')
    plt.fill_between(
        recall, precision, alpha=0.2, color='b',
        label='P-R curve (average precision = %0.2f)' % average_precision
    )

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.0])
    plt.xlim([0.0, 1.05])
    plt.legend(loc="upper right")
    plt.title('Precision-Recall curve - EoL Model')
    plt.show()

def plot_ROC(y_test, pred):
    fpr, tpr, _ = roc_curve(y_test, pred)
    plt.figure()
    lw = 2
    plt.fill_between(fpr, tpr, color='b', alpha = 0.2,
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc_score(y_test, pred))
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic - EoL Model')
    plt.legend(loc="lower right")
    plt.show()