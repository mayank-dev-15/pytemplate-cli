"""Config command: manage YAML configuration."""

from argparse import Namespace

from rich.console import Console
from rich.table import Table

from pytemplate_cli.utils.config import load_config, save_config, DEFAULT_CONFIG

console = Console()


class ConfigCommand:
    def __init__(self, args: Namespace):
        self.action = args.config_action
        self.key = getattr(args, "key", None)
        self.value = getattr(args, "value", None)

    def execute(self):
        if self.action == "show":
            config = load_config()
            table = Table(title="Configuration")
            table.add_column("Key", style="cyan")
            table.add_column("Value", style="green")
            for k, v in config.items():
                table.add_row(k, str(v))
            console.print(table)
        elif self.action == "reset":
            save_config(DEFAULT_CONFIG)
            console.print("[green]Config reset to defaults.[/green]")
        elif self.action == "set":
            config = load_config()
            config[self.key] = self.value
            save_config(config)
            console.print(f"[green]Set {self.key} = {self.value}[/green]")
        else:
            console.print("Use: config show | config reset | config set <key> <value>")
