# Lib-ML

`lib-ml` is a Python library that provides shared preprocessing logic for machine learning model training and service. It includes utilities for text preprocessing and is designed to be reusable across different machine learning projects.

## 📚 Table of Contents

- [✨ Features](#-features)
- [🚀 Installation and Development](#-installation-and-development)
- [📦 Requirements](#-requirements)
- [💻 Usage](#-usage)
- [🔄 Release Workflow](#-release-workflow)
- [📝 License](#-license)

## ✨ Features

- Text preprocessing: Convert text to lowercase and remove non-alphanumeric characters
- Stemming of words using Porter Stemmer
- Stopwords removal (with 'not' preserved for sentiment analysis)
- Easy integration with machine learning pipelines
- Pandas DataFrame support

## 🚀 Installation and Development

To install the library, use the following command:

```bash
pip install .
```

Alternatively, you can build the package locally and install it:

```bash
pip install build
python -m build
pip install dist/*.whl
```

To set up a development environment, install the optional build tools:

```bash
pip install -r requirements.txt
```

## 📦 Requirements

The library requires Python 3.10 or higher and the following dependencies:

- nltk>=3.6
- pandas>=1.0

## 💻 Usage

Here is an example of how to use the `preprocess_reviews` function:

```python
import pandas as pd
from lib_ml.preprocessing import preprocess_reviews

# Create a sample dataset
data = {'Review': ["This movie was great! I loved it.",
                  "Terrible experience, would not recommend."]}
df = pd.DataFrame(data)

# Preprocess the reviews
processed_corpus = preprocess_reviews(df)
print(processed_corpus)
# Output: ['movi great love', 'terribl experi not recommend']
```

The preprocessing includes:

- Removing non-alphabetic characters
- Converting to lowercase
- Removing stopwords (except 'not')
- Stemming words

## 🔄 Release Workflow

The project uses GitHub Actions to automate the release process with GitVersion. When a new tag is pushed in the format `v<MAJOR>.<MINOR>.<PATCH>`, the workflow will:

1. Parse the version from the tag
2. Inject the version into `pyproject.toml`
3. Build the package

Versioning conventions:

- Use `#major` in commit message for breaking changes
- Use `#minor` in commit message for new features
- Use `#patch` in commit message for bug fixes

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.