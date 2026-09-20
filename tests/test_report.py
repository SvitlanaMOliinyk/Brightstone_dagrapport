from decimal import Decimal
from rapport.report import ReportData, analyse_orders


def test_report_total_orders():
    report_data = ReportData([{}, {}])

    assert report_data.total_orders() == 2


def test_report_total_revenue():
    report_data = ReportData([{"prijs": Decimal('100.50')}, {"prijs": Decimal('200.80')}])

    assert report_data.total_revenue() == Decimal('301.30')


def test_report_calculate_price_per_column_item():
    report_data = ReportData(
        [{'product': 'banana', 'prijs': Decimal('100.50')}, {'product': 'banana', 'prijs': Decimal('200.50')},
         {'product': 'apple', 'prijs': Decimal('101.50')}])

    assert report_data.calculate_price_per_column_item('product') == {
        'banana': {'name': 'banana', 'prijs': Decimal('301.00')},
        'apple': {'name': 'apple', 'prijs': Decimal('101.50')}}


def test_report_calculate_top():
    report_data = ReportData(
        [{'klant': 'Maria', 'prijs': Decimal('150.40')}, {'klant': 'Anna', 'prijs': Decimal('301.00')},
         {'klant': 'John', 'prijs': Decimal('50.70')}])
    expected = [{'name': 'Anna', 'prijs': Decimal('301.00')}, {'name': 'Maria', 'prijs': Decimal('150.40')},
                {'name': 'John', 'prijs': Decimal('50.70')}]

    assert report_data.calculate_top('klant', None) == expected


def test_report_calculate_top_limit():
    report_data = ReportData(
        [{'klant': 'Maria', 'prijs': Decimal('150.40')}, {'klant': 'Anna', 'prijs': Decimal('301.00')},
         {'klant': 'John', 'prijs': Decimal('50.70')}])
    expected = [{'name': 'Anna', 'prijs': Decimal('301.00')}, {'name': 'Maria', 'prijs': Decimal('150.40')}]

    assert report_data.calculate_top('klant', 2) == expected

def test_report_analyse_orders():
    orders = [{'datum': '18-09-2026', 'klant': 'Maria', 'product': 'banana', 'prijs': Decimal('150.40'), 'categorie': 'Accessoires'}]
    expected = {
        'total_revenue': Decimal('150.40'),
        'total_orders': 1,
        'top_5_clients': [{'name': 'Maria', 'prijs': Decimal('150.40')}] ,
        'top_5_products': [{'name': 'banana', 'prijs': Decimal('150.40')}],
        'revenue_category': [{'name': 'Accessoires', 'prijs': Decimal('150.40')}],
        'date': '18-09-2026'
    }
    assert analyse_orders(orders) == expected
