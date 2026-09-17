import csv
from decimal import Decimal
from typing import Any


def read_orders(path: str) -> list[dict[str, Any]]:
    with open(path, newline='') as csvfile:
        orders_data=[]
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            row['prijs'] = Decimal(row['prijs'].replace(',', '.'))
            orders_data.append(row)
    return orders_data
