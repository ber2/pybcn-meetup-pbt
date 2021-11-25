# pybcn-meetup-pbt

Code examples for my talk, _Property-based testing with Hypothesis_, at the [PyBCN Meetup](https://www.meetup.com/python-barcelona/events/282194482/) on 2021-11-25.

Property-based testing is introduced and discussed in the context of Test-Driven Development, and [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is introduced as one of the leading packages for property-based testing in python.

Then we discuss an exercise about writing a program using TDD and testing it using Hypothesis. The code for that exercise is contained here.

## Running the code

You will need to install both hypothesis and pytest. I originally wrote the code in Python 3.9, but I reckon anything newer than 3.6 should most probably work (lemme know by opening an issue if that is the case).

```bash
pip install pytest hypothesis
pytest -v
```

## Using poetry

If you use poetry, I have provided my `pyproject.toml` and `poetry.lock`. On an environment with Python 3.9:

```bash
poetry install
pytest -v
```
