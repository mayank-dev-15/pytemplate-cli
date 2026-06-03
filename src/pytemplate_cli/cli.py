"""CLI argument parsing with argparse."""

import argparse
import sys

from pytemplate_cli.commands.init import InitCommand
from pytemplate_cli.commands.run import RunCommand
from pytemplate_cli.commands.config import ConfigCommand
from pytemplate_cli.utils.logging import setup_logging


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pytemplate-cli",
        description="Professional Python CLI tool template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--config", type=str, default="config.yaml", help="Config file path")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init
    init_parser = subparsers.add_parser("init", help="Initialize a new project")
    init_parser.add_argument("name", type=str, help="Project name")
    init_parser.add_argument("--path", type=str, default=".", help="Target directory")

    # run
    run_parser = subparsers.add_parser("run", help="Run the main process")
    run_parser.add_argument("--input", type=str, required=True, help="Input file or directory")
    run_parser.add_argument("--output", type=str, default="output", help="Output directory")
    run_parser.add_argument("--dry-run", action="store_true", help="Simulate without changes")

    # config
    config_parser = subparsers.add_parser("config", help="Manage configuration")
    config_sub = config_parser.add_subparsers(dest="config_action")
    config_sub.add_parser("show", help="Show current config")
    config_sub.add_parser("reset", help="Reset to defaults")
    set_parser = config_sub.add_parser("set", help="Set a config value")
    set_parser.add_argument("key", type=str, help="Config key")
    set_parser.add_argument("value", type=str, help="Config value")

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    setup_logging(verbose=args.verbose)

    if args.command == "init":
        cmd = InitCommand(args)
    elif args.command == "run":
        cmd = RunCommand(args)
    elif args.command == "config":
        cmd = ConfigCommand(args)
    else:
        parser.print_help()
        sys.exit(0)

    cmd.execute()
