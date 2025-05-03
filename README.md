# lib-ml

## Overview

`lib-ml` is a Python library that provides shared preprocessing logic for machine learning model training and service. It includes utilities for text preprocessing and is designed to be reusable across different machine learning projects.

## Features

- Text preprocessing: Convert text to lowercase and remove non-alphanumeric characters.
- Easy integration with machine learning pipelines.

## Installation

To install the library, use the following command:

```bash
pip install .
```

## Requirements

The library requires Python 3.10 or higher and the following dependencies:

- pandas>=2.2.0
- scikit-learn>=1.4.0
- numpy>=1.26.0

## Usage

Here is an example of how to use the `preprocessing` function:

```python
from lib_ml.preprocessing import preprocessing

text = "Hello, World!"
cleaned_text = preprocessing(text)
print(cleaned_text)  # Output: "hello world"
```

## Development

To set up a development environment, install the optional build tools:

```bash
pip install -r requirements.txt
```

## License

TODO

## Contributing

TODO

## Release Workflow

The project uses GitHub Actions to automate the release process. When a new tag is pushed in the format `v<MAJOR>.<MINOR>.<PATCH>`, the workflow will:

1. Parse the version from the tag.
2. Inject the version into `pyproject.toml`.
3. Build the package.
4. Optionally upload the artifacts.

## Contact

For any questions or issues, please contact the maintainers of the repository.
