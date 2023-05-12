
# Project name goes here

This template serves as a starting point for Python projects, including essential utilities, directory structure, and boilerplate code for various tasks.

# To build your own project from this template

1. **Clone it:**

    ```bash
    git clone git@github.com:tollefj/pyplate.git
    ```

2. **Disconnect it:**

     ```bash
     git remote remove origin
     git remote add origin <your_repository_url>
     ```

3. **Make changes:**

     ```bash
     git add .
     git commit -m "Customize the boilerplate for my project"
     ```

4. **Create your own repository:**

5. **Push:**

     ```bash
     git push -u origin master
     ```

## Running stuff

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
