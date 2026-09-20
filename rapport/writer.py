from typing import Any

from .json_writer import write_json
from .markdown_writer import write_markdown


def write_report(report_data: dict[str, Any], output: str, format: str) -> None:
    """Select the output format and file name, then write a report.

    Args:
        report_data: Data to be written to file.
        output: Output file name.
        format: Format of output file, either markdown or json.
    """
    if format == "markdown":
        report_text = write_markdown(report_data)
    elif format == "json":
        report_text = write_json(report_data)

    if output == "rapport_<datum>.md":
        if format == "markdown":
            output = f"rapport_{report_data['date']}.md"

        elif format == "json":
            output = f"rapport_{report_data['date']}.json"

    with open(output, "w", encoding="utf_8") as file:
        file.write(report_text)
