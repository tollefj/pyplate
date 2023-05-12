
# Project name goes here

This template serves as a starting point for Python projects, including essential utilities, directory structure, and boilerplate code for various tasks.

### Getting started

```bash
make setup
# optional tasks: {geo/graphs/image/ml/nlp/web}
make install-req TASK=ml
# do code changes :-)
make run
# did you write tests?
make test
```
### Typing, linting and formatting

```bash
# typing
make mypy
# flake8
make lint
# format the code using `black` and `isort`
make format
# dry run:
make format-check
```

## Directory Structure

```text
├── docs/
│ └── ...
│
├── requirements/
│ ├── requirements.txt
│ ├── requirements_ml.txt
│ ├── requirements_web.txt
│ └── ...
│
├── src/
│ ├── main.py
│ ├── utils/
│ │ └── ...
│
└── tests/
│ └── ...
```
