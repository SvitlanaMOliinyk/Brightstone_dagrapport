import sys
import pytest
from rapport.cli import main


def test_cli_main(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["rapport", "--input", "orders.csv"])

    args = main()

    assert args.input == "orders.csv"


def test_cli_default_output(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["rapport", "--input", "orders.csv"])

    args = main()
    assert args.output == "rapport_<datum>.md"


def test_cli_default_format(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["rapport", "--input", "orders.csv", "--output", "rapport.md"])

    args = main()
    assert args.format == "markdown"


def test_cli_format(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["rapport", "--input", "orders.csv", "--format", "json"])

    args = main()
    assert args.format == "json"


def test_cli_json_wrong_extension(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["rapport", "--input", "orders.csv", "--output", "rapport.md", "--format", "json"])

    with pytest.raises(ValueError):
        main()


def test_cli_markdown_wrong_extension(monkeypatch):
    monkeypatch.setattr(sys, "argv",
                        ["rapport", "--input", "orders.csv", "--output", "rapport.json", "--format", "markdown"])

    with pytest.raises(ValueError):
        main()
