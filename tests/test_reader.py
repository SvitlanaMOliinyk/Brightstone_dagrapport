from decimal import Decimal

import pytest

from rapport.errors import InvalidCsvError, MissingColumnError
from rapport.reader import check_column, read_orders


def test_read_orders(tmp_path):
    csv_file = tmp_path / "mock_orders.csv"
    csv_file.write_text(
        "order_id;datum;klant;product;categorie;aantal;prijs\n"
        "1;18-9-2026;Louise M. Watterson;Muis;Accessoires;3;25,99",
        encoding="utf-8",
    )

    orders = read_orders(csv_file)
    expected = [
        {
            "order_id": "1",
            "datum": "18-9-2026",
            "klant": "Louise M. Watterson",
            "product": "Muis",
            "categorie": "Accessoires",
            "aantal": "3",
            "prijs": Decimal("25.99"),
        },
    ]

    assert orders == expected


def test_check_column():
    one_missing = ["order_id", "datum", "product", "categorie", "aantal", "prijs"]

    assert check_column(one_missing) == "klant"


def test_read_orders_with_missing_column(tmp_path):
    csv_file = tmp_path / "mock_orders.csv"
    csv_file.write_text(
        "order_id;datum;product;categorie;aantal;prijs\n"
        "1;18-9-2026;Muis;Accessoires;3;25,99",
        encoding="utf-8",
    )
    with pytest.raises(MissingColumnError):
        read_orders(csv_file)


def test_read_orders_with_invalid_price(tmp_path):
    csv_file = tmp_path / "mock_orders.csv"
    csv_file.write_text(
        "order_id;datum;klant;product;categorie;aantal;prijs\n"
        "1;18-9-2026;Louise M. Watterson;Muis;Accessoires;3;banana",
        encoding="utf-8",
    )

    with pytest.raises(InvalidCsvError):
        read_orders(csv_file)


def test_read_orders_with_empty_csv(tmp_path):
    csv_file = tmp_path / "mock_orders.csv"
    csv_file.write_text("", encoding="utf-8")

    with pytest.raises(InvalidCsvError):
        read_orders(csv_file)


def test_read_orders_with_empty_rows(tmp_path):
    csv_file = tmp_path / "mock_orders.csv"
    csv_file.write_text(
        "order_id;datum;klant;product;categorie;aantal;prijs\n", encoding="utf-8"
    )

    with pytest.raises(InvalidCsvError):
        read_orders(csv_file)


def test_read_orders_with_broken_row(tmp_path):
    csv_file = tmp_path / "mock_orders.csv"
    csv_file.write_text(
        "order_id;datum;klant;product;categorie;aantal;prijs\n"
        "1;18-9-2026;Louise M. Watterson;Muis;Accessoires;",
        encoding="utf-8",
    )

    with pytest.raises(InvalidCsvError):
        read_orders(csv_file)
