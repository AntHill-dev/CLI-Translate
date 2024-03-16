<div align="center">
  <img src=".github/assets/logo.png" alt="logo" width="200px" height="auto" />
  <h1>CLI Translate</h1>

  <p>CLI-Translate is a text translation console utility developed in Python.</p>

<!-- Badges -->
<p>
  <a href="https://github.com/Qu1nel/CLI-Translate/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Qu1nel/CLI-Translate" alt="contributors" />
  </a>
  <a href="https://github.com/Qu1nel/CLI-Translate/commits/main">
    <img src="https://img.shields.io/github/last-commit/Qu1nel/CLI-Translate" alt="last update" />
  </a>
  <a href="https://github.com/Qu1nel/CLI-Translate/network/members">
    <img src="https://img.shields.io/github/forks/Qu1nel/CLI-Translate" alt="forks" />
  </a>
  <a href="https://github.com/Qu1nel/CLI-Translate/stargazers">
    <img src="https://img.shields.io/github/stars/Qu1nel/CLI-Translate" alt="stars" />
  </a>
  <a href="https://github.com/Qu1nel/CLI-Translate/issues/">
    <img src="https://img.shields.io/github/issues/Qu1nel/CLI-Translate" alt="open issues" />
  </a>
</p>

<p>
  <a href="https://www.python.org/downloads/release/python-3110/" >
    <img src="https://img.shields.io/badge/Python-3.11%2B-blueviolet" alt="python Version" />
  <a>
  <a href="https://github.com/Qu1nel/CLI-Translate/releases/">
    <img src="https://img.shields.io/github/v/release/Qu1nel/CLI-Translate" alt="project version" />
  <a>
  <a href="https://github.com/Qu1nel/CLI-Translate/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Qu1nel/CLI-Translate?color=g" alt="license" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/actions/workflow/status/Qu1nel/CLI-Translate/python_linting.yml?label=Linting" alt="linting" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/actions/workflow/status/Qu1nel/CLI-Translate/python_tests.yml?label=Tests" alt="tests" />
  </a>
</p>

<h4>
  <a href="#view-demo">View Demo</a>
  <span> · </span>
  <a href="#documentation">Documentation</a>
  <span> · </span>
  <a href="https://github.com/Qu1nel/CLI-Translate/issues/">Report Bug</a>
  <span> · </span>
  <a href="https://github.com/Qu1nel/CLI-Translate/issues/">Request Feature</a>
</h4>
</div>

<br />

<!-- Table of Contents -->

# Contents

- [About the Project](#about-cli-translate)
  - [Screenshots](#screenshots)
- [Installation](#installation)
  - [Requirements](#requirements)
- [Getting started](#getting-started)
  - [Windows](#windows)
  - [Linux](#linux)
- [Documentation](#documentation)
- [Flags](#flags)
- [Developers](#developers)
- [License](#license)

## About CLI Translate

CLI-Translate is a powerful multilingual text translation console utility developed in Python. This program provides a fast and reliable way to translate words, phrases, and even whole sentences into different languages.

<details>
  <summary><h3 id="screenshots">Screenshots</h3></summary>
  <div align="center">
    <img src=".github/assets/preview1.png" width=580px>
    <img src=".github/assets/preview2.png" width=580px>
  </div>
</details>

## Installation

Clone the repository, install all requirements and run the file `run.py`.

### Requirements

_The [`Python`](https://www.python.org/downloads/) interpreter version 3.11+ and preferably [`poetry`](https://python-poetry.org/)_

Install requirements with `poetry`:

```bash
poetry install
```

## Getting started

Clone this repository and navigate to it with the command:

```bash
git clone https://github.com/Qu1nel/CLI-Translate.git
cd CLI-Translate/
```

#### Windows

```powershell
python run.py
```

#### Linux

```bash
python3 run.py
```

## Documentation

For full help with make commands, you can use the command:

```bash
make help
```

### Flags

#### --sentence \<text\>

The original application that needs to be translated.

#### --to-lang \<lang\>

Forcibly translate into the selected language.

## Developers

- [Qu1nel](https://github.com/Qu1nel)

## License

[MIT](./LICENSE) © [Ivan Kovach](https://github.com/Qu1nel/)
