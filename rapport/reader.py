import csv
from collections.abc import Sequence
from decimal import Decimal, InvalidOperation
from typing import Any

from .errors import InvalidCsvError, MissingColumnError

REQUIRED_COLUMNS = [
    "order_id",
    "datum",
    "klant",
    "product",
    "categorie",
    "aantal",
    "prijs",
]


def check_column(columns: Sequence[str]) -> str | None:
    """Check whether required column is missing

    Args:
        columns: CSV column names

    Returns:
        Missing column name or None
    """
    for column in REQUIRED_COLUMNS:
        if column not in columns:
            return column

    return None


def read_orders(path: str) -> list[dict[str, Any]]:
    """Read a CSV file and return its rows as dictionaries.

    Args:
        path: Path to CSV file

    Returns:
        List of orders
    """
    with open(path, newline="") as csvfile:
        orders_data = []
        reader = csv.DictReader(csvfile, delimiter=";")
        columns = reader.fieldnames
        if columns is None:
            raise InvalidCsvError("Ongeldig csv-bestand")
        missing_column = check_column(columns)
        if missing_column:
            raise MissingColumnError(missing_column)
        for row in reader:
            try:
                row["prijs"] = Decimal(row["prijs"].replace(",", "."))
            except (InvalidOperation, AttributeError):
                raise InvalidCsvError("Ongeldig csv-bestand")
            orders_data.append(row)
        if len(orders_data) == 0:
            raise InvalidCsvError("Ongeldig csv-bestand")
    return orders_data
