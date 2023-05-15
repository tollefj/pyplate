
# PyPlate - A boilerplate for new Python projects

This template serves as a starting point for Python projects, including essential utilities, directory structure, and example code for various repetitive tasks.

# To build your own project from this template

## 1. Create your own repo

## 2. Clone this repo into a new project folder

```bash
git clone git@github.com:tollefj/pyplate.git MYPROJECT
cd MYPROJECT
```

## 3. Run the setup script `make new`

Or manually:

```bash
git remote remove origin
git remote add origin <your repo url>
git push --set-upstream origin main
```

# Running stuff

```bash
make setup
# optional tasks: {geo/graphs/image/ml/nlp/web}
make install-req TASK=ml
# do code changes :-)
make run
# did you write tests?
make test
```

## Typing, linting and formatting

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
