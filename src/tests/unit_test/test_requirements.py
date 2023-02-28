#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_requirements():
    import pkg_resources

    dependencies = [
        "setuptools==57.5.0",
        "numpy==1.22.2",
        "pandas==1.4.1",
        "scipy==1.8.0",
        "boto3==1.21.4",
        "black==22.3.0",
        "scikit-learn==1.2.1",
        "jupyter==1.0.0",
        "matplotlib==3.5.1",
        "fastapi==0.69.0",
        "pydantic==1.8.0",
        "uvicorn==0.15.0",
        "pytest==7.1.0",
        "locust==2.8.4",
        "streamlit==1.10.0",
    ]

    pkg_resources.require(dependencies)
