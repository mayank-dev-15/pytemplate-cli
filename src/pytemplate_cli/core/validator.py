"""Input validation utilities."""

from pathlib import Path


class Validator:
    SUPPORTED_EXTENSIONS = {".txt", ".csv", ".json", ".yaml", ".yml", ".md"}

    def validate_input(self, path: Path) -> bool:
        if path.is_dir():
            return True
        if path.is_file():
            return path.suffix.lower() in self.SUPPORTED_EXTENSIONS
        return False

    def validate_output(self, path: Path) -> bool:
        return True
