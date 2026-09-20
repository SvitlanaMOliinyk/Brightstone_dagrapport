from typing import Any
from decimal import Decimal

class ReportData:
    def __init__(self, orders: list[dict[str, Any]]):
        """Initialize the report data.

        Args:
            orders: List of order dictionaries.
        """
        self.orders = orders

    def total_orders(self) -> int:
        """Return the total number of orders.

        Returns:
            Number of orders.
        """
        return len(self.orders)

    def total_revenue(self) -> Decimal:
        """Return the total revenue.

        Returns:
            Total revenue.
        """
        total_revenue = Decimal('0')
        for order in self.orders:
            total_revenue += order['prijs']
        return total_revenue

    def calculate_price_per_column_item(self, column_name: str) -> dict[str, Any]:
        """Return column items as dictionaries.

        Args:
            column_name: Name of column.

        Returns:
            Dictionary with total price for each column value.
        """
        column_items: dict[str, dict[str, Any]] = {}

        for order in self.orders:
            column = order[column_name]
            price = order['prijs']
            if column in column_items:
                column_items[column]['prijs'] += price
            else:
                column_items[column] = {'name': column, 'prijs': price}

        return column_items


    def calculate_top(self, column_name: str, limit: int | None = None) -> list[dict[str, Any]]:
        """Return column items sorted by price.

        Args:
            column_name: Name of column.
            limit: Maximum number of items to return.

        Returns:
            List of dictionaries sorted by price.
        """
        unsorted_list = self.calculate_price_per_column_item(column_name).values()
        sorted_list = sorted(unsorted_list, key=lambda item: item['prijs'], reverse=True)
        if limit is None:
            return sorted_list
        else:
            return sorted_list[:limit]

def analyse_orders(orders: list[dict[str, Any]]) -> dict[str, Any]:
    """Analyze the orders and return a report data.

    Args:
        orders: List of orders.

    Returns:
        Dictionary of processed report data.
    """
    report = ReportData(orders)
    return {
        'total_revenue': report.total_revenue(),
        'total_orders': report.total_orders(),
        'top_5_clients': report.calculate_top('klant', 5),
        'top_5_products': report.calculate_top('product', 5),
        'revenue_category': report.calculate_top('categorie'),
        'date': report.orders[0]['datum']
    }




