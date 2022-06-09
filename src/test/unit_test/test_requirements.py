#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_requirements():
    import pkg_resources

    dependencies = [
        "setuptools==57.5.0",
        "numpy==1.22.2",
        "pandas==1.4.1",
        "psycopg2-binary==2.9.3",
        "scipy==1.8.0",
        "boto3==1.21.4",
        "s3fs==0.4.2",
        "sagemaker==2.77.0",
        "black==22.1.0",
        "awscli==1.22.60",
        "sklearn==0.0",
        "jupyter==1.0.0",
        "matplotlib==3.5.1",
        "pytest==7.0.1",
    ]

    pkg_resources.require(dependencies)
