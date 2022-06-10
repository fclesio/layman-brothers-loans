#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append(".")

import joblib
from typing import Union
from sklearn.ensemble import RandomForestClassifier

serialized_model = joblib.load("/app/models/model.joblib")

Model = Union[RandomForestClassifier]


def get_default_probability(
    record: list, model_artifact: Model = serialized_model
) -> float:
    """
    According with some features will return
    the probability of a default.

    Columns in the prediction array:
        - LIMIT_BAL    int64
        - EDUCATION    int64
        - MARRIAGE     int64
        - AGE          int64
        - BILL_AMT1    int64
        - BILL_AMT2    int64
        - PAY_AMT1     int64
        - PAY_AMT2     int64

    Parameters
    ----------
        record : array
            Values relative with the loan according
            to the columns in the training.
        model_artifact : Model
            Scikit-Learn model that predicts
            according to an array

    Returns
    -------
        default_proba: float
            Percentage of a probability of a default
            according to the values passed.
    """

    prediction = model_artifact.predict_proba(record)
    default_proba = prediction[0][0]
    return default_proba
