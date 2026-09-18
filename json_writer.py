import json
from decimal import Decimal
from typing import Any

def convert_to_str(value):
        if isinstance(value, Decimal):
            return str(value)
        else:
            raise TypeError(f"Unsupported type: {type(value).__name__}")


def write_json(report_data: dict[str, Any]) -> str:
    return json.dumps(report_data, default=convert_to_str, indent=4)


