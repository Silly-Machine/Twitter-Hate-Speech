## Twitter Sentiment Analysis

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/FelipeRamosOliveira/Portfolio/pulls)
[![GitHub issues](https://img.shields.io/github/issues/FelipeRamosOliveira/Portfolio.svg)](https://img.shields.io/github/issues/FelipeRamosOliveira/Portfolio.svg)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-000000.svg)](https://www.python.org/downloads/release/python-360/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Scope

This project is a simple sentiment analysis project that uses the Twitter API to analyze the sentiment of tweets.

## Directory Structure

The project is organized in the following directory structure:

```sh
.
├── notebooks       --> contains the notebooks used to train the model
│   └── data        --> contains the data used to train the model
├── pyproject.toml  --> contains the project configuration
└── src             --> contains the maincode
    └── main.py
```

## Setup

Clone the project:

```sh
git clone git@github.com:Silly-Machine/Twitter-Hate-Speech.git
```

Is highly recommended to create the following [`conda`](https://docs.conda.io/en/latest/miniconda.html) virtual environment before installing the dependencies.

```sh
conda create -n twitter_analysis python=3.8
```

Activate the virtual environment:

```sh
conda activate twitter_analysis
```

In the virtual environment, install [`poetry`](https://python-poetry.org/) as the package manager :

```sh
conda install poetry
```

Install project dependencies:

```sh
poetry install
```

To ensure coding patterns and also do preliminary security check before we push code commits to this repository,is necessary to install [`pre-commit`](https://pre-commit.com/) hooks with following command:

```sh
poetry run pre-commit install
```

**_Obs :_** In development phase, is highly recommended creat a local [`MongoDB`](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04-pt) server.
