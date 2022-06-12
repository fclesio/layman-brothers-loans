#!/usr/bin/env python
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
from src.main.prediction.model_predicton import get_default_probability


st.title("Layman Brothers Loan")
st.subheader("Personal Information")

st.subheader("Education")
st.caption("1: No education - 2: College - 3: Graduation - 4: Masters")
education = st.slider("Education", 1, 4, 1)
st.write("Education: ", education)

st.subheader("Marriage")
st.caption("1: Married - 2: Not Married")
marriage = st.slider("marriage", 1, 2, 1)
st.write("Marriage: ", marriage)

st.subheader("Age")
age = st.slider("age", 18, 120, 18)
st.write("Age: ", age)


st.subheader("Financial Information")

limit_bal = st.slider("Balance Limit", 0, 500000, 0)
st.write("Balance Limit: ", limit_bal)

bill_amt1 = st.slider("Bill Amount - Installment #1", 0, 500000, 0)
st.write("Bill Amount - Installment #1: ", bill_amt1)

bill_amt2 = st.slider("Bill Amount - Installment #2", 0, 500000, 0)
st.write("Bill Amount - Installment #2: ", bill_amt2)

pay_amt1 = st.slider("Payment Amount - Installment #1", 0, 500000, 0)
st.write("Payment Amount - Installment #1: ", pay_amt1)

pay_amt2 = st.slider("Payment Amount - Installment #2", 0, 500000, 0)
st.write("Payment Amount - Installment #1: ", pay_amt2)


record = [
    [limit_bal, education, marriage, age, bill_amt1, bill_amt2, pay_amt1, pay_amt2]
]


print(record)

result = get_default_probability(record=record)

st.metric(label="Default Probability", value=f"{result}")
