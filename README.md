# Basics
Dominiks Basics

## Developing

To get started, you must install the Python dependencies:

```shell
pipenv install --dev
```

## Running Tests

In-order to ensure your code works, you should write tests. If you wish to run these tests, you need a shell with a modified `PATH` that allows us to execute the binaries from our dependencies. Pipenv provides a helper for this:

```shell
pipenv shell
pytest
```
