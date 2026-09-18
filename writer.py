from typing import Any
from markdown_writer import write_markdown
from json_writer import write_json

def write_report(report_data: dict[str, Any], output: str, format: str) -> None:
    if format == "markdown":
        report_text = write_markdown(report_data)
    elif format == "json":
        report_text = write_json(report_data)

    with open(output, "w", encoding="utf_8") as file:
        file.write(report_text)
