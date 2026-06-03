"""Core processing logic."""

from pathlib import Path
from typing import Any


class Processor:
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run

    def process(self, input_path: Path, output_path: Path) -> dict[str, Any]:
        results = {"count": 0, "errors": []}

        if input_path.is_dir():
            for item in input_path.iterdir():
                if item.is_file():
                    try:
                        if not self.dry_run:
                            output_path.mkdir(parents=True, exist_ok=True)
                        results["count"] += 1
                    except Exception as e:
                        results["errors"].append(str(e))
        elif input_path.is_file():
            try:
                if not self.dry_run:
                    output_path.mkdir(parents=True, exist_ok=True)
                results["count"] = 1
            except Exception as e:
                results["errors"].append(str(e))

        return results
