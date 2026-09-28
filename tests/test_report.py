from decimal import Decimal

from rapport.report import ReportData, analyse_orders


def test_report_total_orders():
    report_data = ReportData([{}, {}])

    assert report_data.total_orders() == 2


def test_report_total_revenue():
    report_data = ReportData(
        [
            {"prijs": Decimal("100.50"), "aantal": "2"},
            {"prijs": Decimal("200.80"), "aantal": "3"},
        ]
    )

    assert report_data.total_revenue() == Decimal("803.40")


def test_report_calculate_price_per_column_item():
    report_data = ReportData(
        [
            {"product": "banana", "prijs": Decimal("100.50"), "aantal": "2"},
            {"product": "banana", "prijs": Decimal("200.50"), "aantal": "1"},
            {"product": "apple", "prijs": Decimal("101.50"), "aantal": "3"},
        ]
    )

    assert report_data.calculate_price_per_column_item("product") == {
        "banana": {"name": "banana", "prijs": Decimal("401.50")},
        "apple": {"name": "apple", "prijs": Decimal("304.50")},
    }


def test_report_calculate_top():
    report_data = ReportData(
        [
            {"klant": "Maria", "prijs": Decimal("150.40"), "aantal": "1"},
            {"klant": "Anna", "prijs": Decimal("301.00"), "aantal": "1"},
            {"klant": "John", "prijs": Decimal("50.70"), "aantal": "2"},
        ]
    )
    expected = [
        {"name": "Anna", "prijs": Decimal("301.00")},
        {"name": "Maria", "prijs": Decimal("150.40")},
        {"name": "John", "prijs": Decimal("101.40")},
    ]

    assert report_data.calculate_top("klant", None) == expected


def test_report_calculate_top_limit():
    report_data = ReportData(
        [
            {"klant": "Maria", "prijs": Decimal("150.40"), "aantal": "1"},
            {"klant": "Anna", "prijs": Decimal("301.00"), "aantal": "1"},
            {"klant": "John", "prijs": Decimal("50.70"), "aantal": "2"},
        ]
    )
    expected = [
        {"name": "Anna", "prijs": Decimal("301.00")},
        {"name": "Maria", "prijs": Decimal("150.40")},
    ]

    assert report_data.calculate_top("klant", 2) == expected


def test_report_analyse_orders():
    orders = [
        {
            "datum": "18-09-2026",
            "klant": "Maria",
            "product": "banana",
            "prijs": Decimal("150.40"),
            "categorie": "Accessoires",
            "aantal": "2",
        }
    ]
    expected = {
        "total_revenue": Decimal("300.80"),
        "total_orders": 1,
        "top_5_clients": [{"name": "Maria", "prijs": Decimal("300.80")}],
        "top_5_products": [{"name": "banana", "prijs": Decimal("300.80")}],
        "revenue_category": [{"name": "Accessoires", "prijs": Decimal("300.80")}],
        "date": "18-09-2026",
    }
    assert analyse_orders(orders) == expected
