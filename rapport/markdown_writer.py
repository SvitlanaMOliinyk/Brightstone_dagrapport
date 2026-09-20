from datetime import date
from typing import Any


def write_markdown(report_data: dict[str, Any]) -> str:
    """Convert the report data into Markdown.

    Args:
        report_data: Data to be written to file.

    Returns:
        Markdown string.
    """
    report_date = date.strptime(report_data["date"], "%d-%m-%Y").strftime("%Y-%m-%d")
    markdown = f"# {'Dagrapport Brightstone':<25} {'—':<3} {report_date:<10}\n\n"

    markdown += "```text\n"
    markdown += f"### {'Totaal aantal orders:':<25} {report_data['total_orders']:<10}\n"
    markdown += (
        f"### {'Totale omzet:':<25} {'€' + str(report_data['total_revenue']):<10}\n\n"
    )
    markdown += "```\n"

    markdown += "## Top 5 producten (op omzet):\n"
    markdown += "```text\n"
    markdown += f"{'Nr':<4} {'Product':<25} {'Omzet':<10}\n"
    markdown += "-" * 41 + "\n"
    for number, item in enumerate(report_data["top_5_products"], 1):
        markdown += f"{str(number) + '.':<4} {item['name']:<25} {'€' + str(item['prijs']):<10}\n"
    markdown += "```\n"

    markdown += "## Top 5 klanten (op besteed bedrag):\n"
    markdown += "```text\n"
    markdown += f"{'Nr':<4} {'Klant':<25} {'Besteed bedrag':<10}\n"
    markdown += "-" * 41 + "\n"
    for number, item in enumerate(report_data["top_5_clients"], 1):
        markdown += f"{str(number) + '.':<4} {item['name']:<25} {'€' + str(item['prijs']):<10}\n"
    markdown += "```\n"

    markdown += "## Omzet per categorie:\n"
    markdown += "```text\n"
    markdown += f"{'Categorie':<25} {'Omzet':<10}\n"
    markdown += "-" * 36 + "\n"
    for item in report_data["revenue_category"]:
        markdown += f"{item['name']:<25} {'€' + str(item['prijs']):<10}\n"
    markdown += "```\n"
    return markdown
