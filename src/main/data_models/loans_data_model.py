#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import BaseModel


class Loans(BaseModel):
    limit_bal: int
    education: int
    marriage: int
    age: int
    bill_amt1: int
    bill_amt2: int
    pay_amt1: int
    pay_amt2: int
