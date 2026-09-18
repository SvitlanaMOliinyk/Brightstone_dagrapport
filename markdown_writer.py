from typing import Any
from _datetime import datetime

def write_markdown(report_data: dict[str, Any]) -> str:
    date = datetime.strptime(report_data['date'], '%d-%m-%Y').strftime('%Y-%m-%d')
    markdown = f"# Dagrapport Brightstone — {date}\n"

    markdown += f"## Totaal aantal orders: \t {report_data['total_orders']}\n"
    markdown += f"## Totale omzet: \t €{report_data['total_revenue']}\n"

    markdown += f"# Top 5 producten (op omzet):\n"
    for number, item in enumerate(report_data['top_5_products'], 1):
        markdown += f"{number}. {item['name']} \t €{item['prijs']}\n"

    markdown += f"# Top 5 klanten (op besteed bedrag):\n"
    for number, item in enumerate(report_data['top_5_clients'], 1):
        markdown += f"{number}. {item['name']} \t €{item['prijs']}\n"

    markdown += f"# Omzet per categorie:\n"
    for item in report_data['revenue_category']:
        markdown += f"{item['name']} \t €{item['prijs']}\n"

    return markdown
