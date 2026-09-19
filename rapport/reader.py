import csv
from decimal import Decimal, InvalidOperation
from typing import Any
from .errors import InvalidCsvError, MissingColumnError

REQUIRED_COLUMNS = ['order_id', 'datum', 'klant', 'product', 'categorie', 'aantal', 'prijs']

def check_column(columns: list[str]) -> str|None:
    for column in REQUIRED_COLUMNS:
        if column not in columns:
            return column


def read_orders(path: str) -> list[dict[str, Any]]:
    with open(path, newline='') as csvfile:
        orders_data=[]
        reader = csv.DictReader(csvfile, delimiter=';')
        columns = reader.fieldnames
        if columns is None:
            raise InvalidCsvError('Ongeldig csv-bestand')
        missing_column = check_column(columns)
        if missing_column:
            raise MissingColumnError(missing_column)
        for row in reader:
            try:
                row['prijs'] = Decimal(row['prijs'].replace(',', '.'))
            except InvalidOperation:
                raise InvalidCsvError('Ongeldig csv-bestand')
            orders_data.append(row)
        if len(orders_data) == 0:
            raise InvalidCsvError('Ongeldig csv-bestand')
    return orders_data
