"""Run command: main processing logic."""

import os
from argparse import Namespace
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from pytemplate_cli.core.processor import Processor
from pytemplate_cli.core.validator import Validator

console = Console()


class RunCommand:
    def __init__(self, args: Namespace):
        self.input_path = Path(args.input)
        self.output_path = Path(args.output)
        self.dry_run = args.dry_run

    def execute(self):
        if not self.input_path.exists():
            console.print(f"[red]Error: Input path '{self.input_path}' not found.[/red]")
            return

        validator = Validator()
        if not validator.validate_input(self.input_path):
            console.print("[red]Validation failed.[/red]")
            return

        if self.dry_run:
            console.print("[yellow]Dry run mode — no changes will be made.[/yellow]")

        processor = Processor(dry_run=self.dry_run)

        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("Processing...", total=None)
            result = processor.process(self.input_path, self.output_path)
            progress.update(task, completed=True)

        console.print(f"[bold green]Done.[/bold green] Processed {result['count']} items.")
        if result.get("errors"):
            console.print(f"[yellow]Warnings: {len(result['errors'])}[/yellow]")
