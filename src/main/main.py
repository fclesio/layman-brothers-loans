#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append(".")

import pandas as pd
import joblib
from typing import Union
from sklearn.ensemble import RandomForestClassifier
from typing import Optional
from fastapi import FastAPI, Request, Body
from data_models.loans_data_model import Loans
from src.logger.loggerfactory import LoggerFactory

logger = LoggerFactory.get_logger(log_level="info")

app = FastAPI()

serialized_model = joblib.load("/app/models/model.joblib")

Model = Union[RandomForestClassifier]


def get_default_probability(model_artifact: Model, record: list) -> float:
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
        model_artifact : Model
            Scikit-Learn model that predicts
            according to an array
        record : array
            Values relative with the loan according
            to the columns in the training.

    Returns
    -------
        default_proba: float
            Percentage of a probability of a default
            according to the values passed.
    """

    prediction = model_artifact.predict_proba(record)
    default_proba = prediction[0][0]
    return default_proba


@app.get("/ping")
def pong():
    return {"ping": "OK"}


@app.post("/prediction/v1")
async def get_body(request: Request):
    result = await request.json()

    loan_data = Loans(
        limit_bal=result["limit_bal"],
        education=result["education"],
        marriage=result["marriage"],
        age=result["age"],
        bill_amt1=result["bill_amt1"],
        bill_amt2=result["bill_amt2"],
        pay_amt1=result["pay_amt1"],
        pay_amt2=result["pay_amt2"],
    )

    limit_bal: int = loan_data.limit_bal
    education: int = loan_data.education
    marriage: int = loan_data.marriage
    age: int = loan_data.age
    bill_amt1: int = loan_data.bill_amt1
    bill_amt2: int = loan_data.bill_amt2
    pay_amt1: int = loan_data.pay_amt1
    pay_amt2: int = loan_data.pay_amt2

    record = [
        [limit_bal, education, marriage, age, bill_amt1, bill_amt2, pay_amt1, pay_amt2]
    ]

    result = get_default_probability(model_artifact=serialized_model, record=record)

    result_dict = {"default_probability": result}

    logger.info(f"API Input: {result} - Prediction Output: {result_dict}")

    return result_dict
