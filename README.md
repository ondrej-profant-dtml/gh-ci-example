# Github CI example

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![uv](https://img.shields.io/badge/built%20with-uv-blueviolet)](https://astral.sh/blog/uv)

Example of python package and github CI.


```sh
cd packages/uv-p1
uv run uv-p1
uv run --group dev ruff --config ../../ruff.toml check .
uv run --group dev ruff --config ../../ruff.toml format . --check
uv run --group dev pytest
```

