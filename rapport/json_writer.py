import json
from decimal import Decimal
from typing import Any

def convert_to_str(value: Any) -> str:
    """Convert the value to a string.

    Args:
        value: Value to be converted to string.

    Returns:
        String value.

    Raises:
        TypeError: If the value is not a Decimal.
    """
    if isinstance(value, Decimal):
        return str(value)
    else:
        raise TypeError(f"Unsupported type: {type(value).__name__}")


def write_json(report_data: dict[str, Any]) -> str:
    """Convert the report data into a JSON string.

    Args:
        report_data: Data to be written to file.

    Returns:
        JSON string.
       """
    return json.dumps(report_data, default=convert_to_str, indent=4)


