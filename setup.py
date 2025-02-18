import os
from setuptools import setup, find_packages

def read_readme():
    if os.path.exists("README.md"):
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    return ""

setup(
    name="UcDataImputer",
    version="0.1.0",
    author="Goktug Onal",
    author_email="goktug.onal@ucsf.edu",
    description="Data Imputer for Ulcerative Colitis Studies",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/rwelab/UCDataImputer.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "pandas",
        "joblib",
        "argparse"
    ],
)
