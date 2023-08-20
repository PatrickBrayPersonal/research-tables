# DSMS Machine Learning Template

_Create standardized repositories that facilitate reproducible and organized experiments._

## Usage
-----------
### Prerequisites
 - Python 3.9+
 - Git
### Getting Started
1. Click "Use this template"
2. Clone your new repository
3. Run `rename_project.py`
- make sure programs (including vscode) are not accessing the `your_project` folder
4. Follow the installation instructions in your new project's README 

## Why should I use this?
------------
To understand the motivation behind this project read the stated principles of [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/#links-to-related-projects-and-references)
- This project builds upon the principles of that template with more recent tooling targeted at machine learning applications (hydra, mlflow, poetry)
- we simplify some aspects of this repository and add other opinionated capabilities
## Principles
- Experimentation with reproducibility
	- If you run an experiment, you should be able to rerun the experiment at any time in the future and produce the same results.
	- Experiment adjustment should be painless to maximize exploration
	- All steps taken in an experiment should be displayed and obvious
- Dependency inversion principle
	- *High-level implementations should depend on abstractions*
	- Key to building loosely coupled applications
	- This template encourages the development of interchangeable readers, transformers, components, and writers (high-level abstractions). Swapping out components and transformers during experimentation frees the user to write reliable code quickly. Swapping out readers and writers enables easy switching between local and cloud environments.

## Integrations
------
This template is a Frankenstein monster of open-source ML and Python tooling. Swap out these libraries with other tools more suited to your use case.
### Machine Learning
- [hydra](https://hydra.cc/docs/intro/#introduction)
	- Config and experimentation orchestration
	- Lightweight alternative: [Python Fire](https://google.github.io/python-fire/guide/)
- [mlflow](https://mlflow.org/docs/latest/what-is-mlflow.html)
	- Experiment tracking and model versioning
	- Subscription-based alternative:  [Weights & Biases](https://wandb.ai/site)
### Documentation
- [pdoc](https://pdoc.dev/docs/pdoc.html#customizing-pdoc)
	- Automatically builds API documentation
	- More configurable alternative: [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
- [ghp-import](https://pypi.org/project/ghp-import/)
	- Lightweight GitHub pages for documentation automation
	- Heavier and more automated alternative: [Github Actions](https://github.com/features/actions)
### Formatting (PEP8)
- [black](https://pypi.org/project/black/)
	- automatically format code
- [isort](https://pycqa.github.io/isort/)
	- automatically sort imports
- [flake8](https://flake8.pycqa.org/en/2.5.5/config.html)
	- find linting issues not fixed by black
### Other
- [invoke](https://www.pyinvoke.org/)
	- manage command line workflows using python
	- OS agnostic, unlike Makefile
- [pytest](https://docs.pytest.org/en/7.3.x/)
	- python test management framework
	- More configurable alternative: [unittest](https://docs.python.org/3/library/unittest.html)
- [poetry](https://python-poetry.org/)
	- Dependency and environment management
	- Classic alternative: [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [theskumar/python-dotenv](https://github.com/theskumar/python-dotenv)
	- automatically read and access environment variables
- [loguru](https://loguru.readthedocs.io/en/stable/overview.html#)
	- easy logging, better api
## Inspiration
----------
- [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)
	- Cookiecutter template that espouses data analysis as a DAG concept.
	- Packages used are outdated
	- No integration with experiment tracking.
- [khuyentran1401/data-science-template](https://github.com/khuyentran1401/data-science-template)
	- A similar template but without the experiment tracking and opinionated package structure.
- [fmind/MLOps Template](https://github.com/fmind/mlops-python-package)
- [Sematic](https://www.sematic.dev/)
	- This package allows the user to orchestrate different aspects of the pipeline with different hardware.
	- It also can cache pipeline outputs (development accelerator)
	- The type checking had issues with iterables that made development using sematic difficult.
- [MLflow Recipes](https://mlflow.org/docs/latest/recipes.html)
	- This framework has some bugs that I was unable to address and is still experimental

