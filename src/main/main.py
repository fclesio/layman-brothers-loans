#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append(".")

import pandas as pd
from typing import Optional
from fastapi import FastAPI, Request, Body
from data_models.loans_data_model import Loans
from src.logger.loggerfactory import LoggerFactory

logger = LoggerFactory.get_logger(log_level="info")

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "OK"}


"""

@app.post("/prediction/v1")
async def get_body(request: Request):
    result = await request.json()

    order_data = Orders(
        order_id=result["order_id"],
        customer_id=result["customer_id"],
        timestamp=result["timestamp"],
        sku_code=result["sku_code"],
        zip_code=result["zip_code"],
    )

    order_id = order_data.order_id
    customer_id = order_data.customer_id

    features_calculated = features_processed[
        (features_processed["order_id"] == order_id)
        & (features_processed["customer_id"] == customer_id)
    ].head(
        1
    )  # TODO: Check with the Wayfair team cases about duplications in data

    order_hour_of_day: int = features_calculated["order_hour_of_day"].values

    inventory: int = features_calculated["inventory"].values

    payment_status: str = features_calculated["payment_status"].values

    zip_code_available: bool = features_calculated["zip_code_available"].values

    features = Features(
        order_hour_of_day, inventory, payment_status, zip_code_available
    )

    recommendation = predict(model_v1, features)

    result_dict = {}
    result_dict["order_id"] = order_id
    result_dict["recommendation"] = str(recommendation.value).upper()

    logger.info(f"API Input: {result} - Prediction Output: {result_dict}")

    return result_dict
"""
