#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("./")

import logging
import shutil
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from joblib import dump, load


def setup_custom_logger(name):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


logger = setup_custom_logger("root")
logger.info("[DATA-CLEANUP] - Start data folder deletion")

logger.info("[DATA-CLEANUP] - Data folder deletion finished")
logger.info("[DATA-EXTRACTION] - Start data extraction")
url = "https://raw.githubusercontent.com/fclesio/learning-space/master/Datasets/02%20-%20Classification/default_credit_card.csv"

logger.info(f"[DATA-EXTRACTION] - Data URL: {url}")
seed = 42

logger.info(f"[DATA-EXTRACTION] - Random seed for data split: {seed}")
dict_data_path = {
    "X_train": "data/train_features.csv",
    "X_test": "data/test_features.csv",
    "y_train": "data/train_labels.csv",
    "y_test": "data/test_labels.csv",
}


def get_raw_from_github(url):
    df = pd.read_csv(url)
    return df


def get_y(df):
    y = df.iloc[:, -1:]
    return y


def get_X(df):
    del df["DEFAULT"]
    del df["ID"]
    del df["SEX"]
    del df["PAY_0"]
    del df["PAY_2"]
    del df["PAY_3"]
    del df["PAY_4"]
    del df["PAY_5"]
    del df["PAY_6"]
    del df["BILL_AMT3"]
    del df["BILL_AMT4"]
    del df["BILL_AMT5"]
    del df["BILL_AMT6"]
    del df["PAY_AMT3"]
    del df["PAY_AMT4"]
    del df["PAY_AMT5"]
    del df["PAY_AMT6"]
    X = df
    return X


def delete_files(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


logger.info(f"[DATA-EXTRACTION] - Get data from Github")
df = get_raw_from_github(url=url)

logger.info(
    f"[DATA-EXTRACTION] - Dataframe with {df.shape[0]} rows and {df.shape[1]} columns"
)

y = get_y(df)
X = get_X(df)

test_size = 0.10
logger.info(
    f"[DATA-EXTRACTION] - Split train and test sets. Test size with {test_size}%"
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=seed, test_size=test_size
)

logger.info(
    f"[DATA-EXTRACTION] - Training set with {X_train.shape[0]} samples - Test set with {X_test.shape[0]} samples"
)

logger.info("[DATA-EXTRACTION] - Create folder")
if not os.path.isdir("data"):
    os.mkdir("data")
for key, value in dict_data_path.items():
    delete_files(filepath=value)

logger.info("[DATA-EXTRACTION]- Saving files in folder")

np.savetxt(dict_data_path["X_train"], X_train)
np.savetxt(dict_data_path["X_test"], X_test)
np.savetxt(dict_data_path["y_train"], y_train)
np.savetxt(dict_data_path["y_test"], y_test)

logger.info("[DATA-EXTRACTION]- Data extraction finished")

dict_cml_objects_path = {
    "confusion_matrix": "meta/confusion_matrix.png",
    "metrics": "meta/metrics.txt",
}

dict_data_path = {
    "X_train": "data/train_features.csv",
    "X_test": "data/test_features.csv",
    "y_train": "data/train_labels.csv",
    "y_test": "data/test_labels.csv",
}


logger.info("[TRAINING] - Load training and test data")
X_train = np.genfromtxt(dict_data_path["X_train"])
y_train = np.genfromtxt(dict_data_path["y_train"])
X_test = np.genfromtxt(dict_data_path["X_test"])
y_test = np.genfromtxt(dict_data_path["y_test"])

logger.info("[TRAINING] - Algo training")
clf = RandomForestClassifier(max_depth=50, verbose=1)
clf.fit(X_train, y_train)

dump(clf, "models/model.joblib")

acc = clf.score(X_test, y_test)
acc = (round(acc, 2)) * 100

logger.info(f"[TRAINING] - Model accuracy: {acc}")

with open(dict_cml_objects_path["metrics"], "w") as outfile:
    outfile.write("Accuracy: " + str(acc) + "\n")

y_pred = clf.predict(X_test)

classes = ["non_default", "default"]

cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm, display_labels=classes).plot(
    values_format=".0f"
)

cm_display.figure_.savefig(dict_cml_objects_path["confusion_matrix"], dpi=300)

logger.info("[TRAINING] - Training finished")
