research-tables
==============================

Application to aid researchers by extracting common ects from research tables

Patrick Bray


## Prerequisites
- Python 3.9
- poetry 
  - `pip install poetry`

## Installation
1. Create your environment
`poetry install`
`poetry shell`
2. Test the precommit script
`inv precommit`
3. Test the package
`pytest .`

This repo uses [poetry](https://python-poetry.org/docs/)
Add dependencies using `poetry add`

Project Organization
------------

    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── mlruns             <- Trained and serialized models, model predictions, or model summaries in mlflow
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    ├── scripts            <- Scripts and configs for training and inference, using [hydra](https://hydra.cc/docs/intro/#introduction).
    |                         Put code here that is not easily reused and put details in your config files. Mature code should be moved
    |                         into the package for reuse from other scripts
    ├── tests              <- project tests
    ├── table_extract       <- Source code for use in this project.
    │   ├── data           <- Functions to download, edit, or generate data
    │   │
    │   ├── model          <- Functions to train models and then use trained models to make
    │   │                     predictions
    │   └── ui  <- Scripts to create exploratory and results oriented visualizations
    │       └── streamlit.py
    ├── tasks.py <- command line workflows using [invoke](https://www.pyinvoke.org/)
    └── pyproject.toml <- holds settings for the project, including linting and dependencies


--------


## Invoke Commands
This repository uses [invoke](https://www.pyinvoke.org/) to manage its command-line workflows.
Enter `inv -l` to see the list of commands

## Example Usage
See the example usage in `config/pdm` and `config/time-series` for tutorials on how to use this repository.