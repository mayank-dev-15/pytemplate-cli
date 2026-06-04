# PyTemplate-CLI

![Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit-blue?style=for-the-badge)


## 🚀 Live Demo

**[View Demo](https://mayank-dev-15.github.io/pytemplate-cli-demo)** — hosted on GitHub Pages


[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Professional Python CLI tool template with argparse, structured logging, YAML config, and rich output.

## Features

- **argparse** with subcommands (init, run, config)
- **Rich** console output with progress bars
- **YAML** configuration management
- **Structured logging** with configurable levels
- **Input validation** with extensible rules
- **pytest** test suite

## Quick Start

```bash
pip install -e .
pytemplate-cli --help
pytemplate-cli init myproject
pytemplate-cli run --input data/ --output results/
pytemplate-cli config show
```

## Project Structure

```
pytemplate-cli/
├── src/pytemplate_cli/
│   ├── cli.py              # Argument parsing
│   ├── main.py             # Entry point
│   ├── commands/           # Subcommand implementations
│   │   ├── init.py
│   │   ├── run.py
│   │   └── config.py
│   ├── core/               # Core logic
│   │   ├── processor.py
│   │   └── validator.py
│   └── utils/              # Utilities
│       ├── logging.py
│       └── config.py
├── tests/
├── pyproject.toml
└── README.md
```

## License

MIT
