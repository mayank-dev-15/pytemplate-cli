"""Tests for validator module."""

from pytemplate_cli.core.validator import Validator


def test_validate_txt_file(tmp_path):
    v = Validator()
    f = tmp_path / "test.txt"
    f.write_text("hello")
    assert v.validate_input(f) is True


def test_validate_unsupported_file(tmp_path):
    v = Validator()
    f = tmp_path / "test.exe"
    f.write_text("binary")
    assert v.validate_input(f) is False


def test_validate_dir(tmp_path):
    v = Validator()
    assert v.validate_input(tmp_path) is True
