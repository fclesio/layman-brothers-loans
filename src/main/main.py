#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append(".")


import pandas as pd
from typing import Optional
from fastapi import FastAPI, Request, Body
from data_models.loans_data_model import Loans
from src.main.prediction.model_predicton import get_default_probability
from src.logger.loggerfactory import LoggerFactory

logger = LoggerFactory.get_logger(log_level="info")

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "OK"}


@app.post("/prediction/v1")
async def get_body(loan: Loans):
    limit_bal: int = loan.limit_bal
    education: int = loan.education
    marriage: int = loan.marriage
    age: int = loan.age
    bill_amt1: int = loan.bill_amt1
    bill_amt2: int = loan.bill_amt2
    pay_amt1: int = loan.pay_amt1
    pay_amt2: int = loan.pay_amt2

    record = [
        [limit_bal, education, marriage, age, bill_amt1, bill_amt2, pay_amt1, pay_amt2]
    ]

    result = get_default_probability(record=record)

    result_dict = {"default_probability": result}

    logger.info(f"API Input: {result} - Prediction Output: {result_dict}\n")

    return result_dict
