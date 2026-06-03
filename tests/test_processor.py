"""Tests for processor module."""

from pathlib import Path

from pytemplate_cli.core.processor import Processor


def test_process_file(tmp_path):
    processor = Processor(dry_run=True)
    input_file = tmp_path / "test.txt"
    input_file.write_text("hello")
    result = processor.process(input_file, tmp_path / "out")
    assert result["count"] == 1


def test_process_dir(tmp_path):
    processor = Processor(dry_run=True)
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "b.txt").write_text("b")
    result = processor.process(tmp_path, tmp_path / "out")
    assert result["count"] == 2
