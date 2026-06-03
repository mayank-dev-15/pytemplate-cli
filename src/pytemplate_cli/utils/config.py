"""YAML config file handling."""

import os
from pathlib import Path

import yaml

DEFAULT_CONFIG = {
    "app_name": "pytemplate-cli",
    "version": "0.1.0",
    "log_level": "INFO",
    "output_dir": "output",
    "max_workers": 4,
}

CONFIG_DIR = Path.home() / ".config" / "pytemplate-cli"
CONFIG_FILE = CONFIG_DIR / "config.yaml"


def load_config() -> dict:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            data = yaml.safe_load(f) or {}
        return {**DEFAULT_CONFIG, **data}
    return DEFAULT_CONFIG.copy()


def save_config(config: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
