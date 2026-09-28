from argparse import Namespace

from rapport.__main__ import main
from rapport.errors import InvalidCsvError, MissingColumnError


def test_main_success(monkeypatch):
    args = Namespace(
        input="orders.csv",
        output="rapport.md",
        format="markdown",
    )
    orders = [{"datum": "18-09-2026"}]

    def fake_cli():
        return args

    def fake_read_orders(path):
        return orders

    def fake_analyse_orders(orders):
        return {}

    def fake_write_report(report_data, output, format):
        pass
    monkeypatch.setattr("rapport.__main__.cli.main", fake_cli)
    monkeypatch.setattr("rapport.__main__.reader.read_orders", fake_read_orders)
    monkeypatch.setattr("rapport.__main__.report.analyse_orders", fake_analyse_orders)
    monkeypatch.setattr("rapport.__main__.writer.write_report", fake_write_report)

    result = main()
    assert result == 0

def test_main_file_not_found(monkeypatch):
    args = Namespace(
        input="missing.csv",
        output="rapport.md",
        format="markdown")

    def fake_cli():
        return args
    def fake_read_orders(path):
        raise FileNotFoundError

    monkeypatch.setattr("rapport.__main__.cli.main", fake_cli)
    monkeypatch.setattr("rapport.__main__.reader.read_orders", fake_read_orders)

    result = main()
    assert result == 1

def test_main_missing_column(monkeypatch):
    args = Namespace(
        input="orders.csv",
        output="rapport.md",
        format="markdown"
    )

    def fake_cli():
        return args
    def fake_read_orders(path):
        raise MissingColumnError
    monkeypatch.setattr("rapport.__main__.cli.main", fake_cli)
    monkeypatch.setattr("rapport.__main__.reader.read_orders", fake_read_orders)
    result = main()
    assert result == 1

def test_main_invalid_csv(monkeypatch):
    args = Namespace(
        input="orders.csv",
        output="rapport.md",
        format="markdown"
    )
    def fake_cli():
        return args
    def fake_read_orders(path):
        raise InvalidCsvError
    monkeypatch.setattr("rapport.__main__.cli.main", fake_cli)
    monkeypatch.setattr("rapport.__main__.reader.read_orders", fake_read_orders)
    result = main()
    assert result == 1

def test_main_cli_value_error(monkeypatch):
   def fake_cli():
       raise ValueError
   monkeypatch.setattr("rapport.__main__.cli.main", fake_cli)
   result = main()
   assert result == 2

def test_main_os_error(monkeypatch):
    args = Namespace(
        input="orders.csv",
        output="rapport.md",
        format="markdown"
    )
    orders = [{"datum": "18-09-2026"}]
    def fake_cli():
        return args
    def fake_read_orders(path):
        return orders
    def fake_analyse_orders(orders):
        return {}
    def fake_write_report(report_data, output, format):
        raise OSError("Kan bestand niet schrijven")
    monkeypatch.setattr("rapport.__main__.cli.main", fake_cli)
    monkeypatch.setattr("rapport.__main__.reader.read_orders", fake_read_orders)
    monkeypatch.setattr("rapport.__main__.report.analyse_orders", fake_analyse_orders)
    monkeypatch.setattr("rapport.__main__.writer.write_report", fake_write_report)

    result = main()
    assert result == 2
