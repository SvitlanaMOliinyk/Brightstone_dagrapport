from typing import Any
from decimal import Decimal

class ReportData:
    def __init__(self, orders: list[dict[str, Any]]):
        self.orders = orders

    def total_orders(self) -> int:
        return len(self.orders)

    def total_revenue(self) -> Decimal:
        total_revenue = Decimal('0')
        for order in self.orders:
            total_revenue += order['prijs']
        return total_revenue

    def calculate_price_per_column_item(self, column_name: str) -> dict[str, Any]:
        column_items = {}

        for order in self.orders:
            column = order[column_name]
            price = order['prijs']
            if column in column_items:
                column_items[column]['prijs'] += price
            else:
                column_items[column] = {'name': column, 'prijs': price}

        return column_items


    def calculate_top(self, column_name: str, limit: int|None = None) -> list[dict[str, Any]]:
        unsorted_list = self.calculate_price_per_column_item(column_name).values()
        sorted_list = sorted(unsorted_list, key=lambda item: item['prijs'], reverse=True)
        if limit is None:
            return sorted_list
        else:
            return sorted_list[:limit]

def analyse_orders(orders: list[dict[str, Any]]) -> dict[str, Any]:
    report = ReportData(orders)
    return {
        'total_revenue': report.total_revenue(),
        'total_orders': report.total_orders(),
        'top_5_clients': report.calculate_top('klant', 5),
        'top_5_products': report.calculate_top('product', 5),
        'revenue_category': report.calculate_top('categorie'),
        'date': report.orders[0]['datum']
    }




