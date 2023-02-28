#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_requirements():
    import pkg_resources

    dependencies = [
        "setuptools==57.5.0",
        "numpy==1.22.2",
        "pandas==1.4.1",
        "scipy==1.8.0",
        "black==22.3.0",
        "scikit-learn==1.2.1",
        "jupyter==1.0.0",
        "matplotlib==3.5.1",
        "pydantic==1.9.0",
        "fastapi==0.75.0",
        "uvicorn==0.17.6",
        "pytest==7.0.1",
        "streamlit==1.10.0",
    ]

    pkg_resources.require(dependencies)
