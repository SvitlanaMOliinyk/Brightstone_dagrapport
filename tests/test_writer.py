import pytest
from decimal import Decimal
from rapport.writer import write_report
from rapport.json_writer import convert_to_str

def test_write_report(tmp_path):
    output = tmp_path / "mock_report.md"
    report_data = {'date': '18-09-2026', 'total_orders': 1, 'total_revenue': Decimal('150.40'),
                   'top_5_clients': [{'name': 'Maria', 'prijs': Decimal('150.40')}],
                   'top_5_products': [{'name': 'banana', 'prijs': Decimal('150.40')}],
                   'revenue_category': [{'name': 'Accessoires', 'prijs': Decimal('150.40')}]}
    write_report(report_data, output, "markdown")

    assert output.exists()


def test_write_report_markdown(tmp_path):
    output = tmp_path / "mock_report.md"
    report_data = {'date': '18-09-2026', 'total_orders': 1, 'total_revenue': Decimal('150.40'),
                   'top_5_clients': [{'name': 'Maria', 'prijs': Decimal('150.40')}],
                   'top_5_products': [{'name': 'banana', 'prijs': Decimal('150.40')}],
                   'revenue_category': [{'name': 'Accessoires', 'prijs': Decimal('150.40')}]}
    write_report(report_data, output, "markdown")
    report = output.read_text()
    assert 'Omzet per categorie' in report


def test_write_report_json(tmp_path):
    output = tmp_path / "mock_report.json"
    report_data = {'date': '18-09-2026', 'total_orders': 1, 'total_revenue': Decimal('150.40'),
                   'top_5_clients': [{'name': 'Maria', 'prijs': Decimal('150.40')}],
                   'top_5_products': [{'name': 'banana', 'prijs': Decimal('150.40')}],
                   'revenue_category': [{'name': 'Accessoires', 'prijs': Decimal('150.40')}]}
    write_report(report_data, output, "json")
    report = output.read_text()
    assert '"total_orders": 1' in report


def test_convert_to_str_with_invalid_type():
    with pytest.raises(TypeError):
        convert_to_str('banana')

def test_write_report_default(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    report_data = {'date': '18-09-2026', 'total_orders': 1, 'total_revenue': Decimal('150.40'),
                   'top_5_clients': [{'name': 'Maria', 'prijs': Decimal('150.40')}],
                   'top_5_products': [{'name': 'banana', 'prijs': Decimal('150.40')}],
                   'revenue_category': [{'name': 'Accessoires', 'prijs': Decimal('150.40')}]}
    write_report(report_data, 'rapport_<datum>.md' , "markdown")
    assert (tmp_path/'rapport_18-09-2026.md').exists()

def test_write_report_default_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    report_data = {'date': '18-09-2026', 'total_orders': 1, 'total_revenue': Decimal('150.40'),
                       'top_5_clients': [{'name': 'Maria', 'prijs': Decimal('150.40')}],
                       'top_5_products': [{'name': 'banana', 'prijs': Decimal('150.40')}],
                       'revenue_category': [{'name': 'Accessoires', 'prijs': Decimal('150.40')}]}
    write_report(report_data, 'rapport_<datum>.md', "json")
    assert (tmp_path / 'rapport_18-09-2026.json').exists()
