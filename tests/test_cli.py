"""Tests for CLI module."""

from pytemplate_cli.cli import create_parser


def test_parser_creation():
    parser = create_parser()
    assert parser is not None


def test_init_command():
    parser = create_parser()
    args = parser.parse_args(["init", "myproject"])
    assert args.command == "init"
    assert args.name == "myproject"


def test_run_command():
    parser = create_parser()
    args = parser.parse_args(["run", "--input", "data.csv"])
    assert args.command == "run"
    assert args.input == "data.csv"


def test_config_show():
    parser = create_parser()
    args = parser.parse_args(["config", "show"])
    assert args.command == "config"
    assert args.config_action == "show"
