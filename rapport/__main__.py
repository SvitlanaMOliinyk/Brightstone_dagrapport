import logging
import sys

from . import cli, reader, report, writer
from .errors import InvalidCsvError, MissingColumnError

logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main() -> int:
    """Run the application"""

    try:
        args = cli.main()

    except ValueError as e:
        logger.error(e)
        return 2

    try:
        orders = reader.read_orders(args.input)

        logger.info(
            f"Inlezen data/orders_{orders[0]['datum']} ({len(orders)} rows, 0 fouten)"
        )
    except FileNotFoundError:
        logger.error("Bestand is niet gevonden")
        return 1
    except InvalidCsvError as e:
        logger.error(e)
        return 1
    except MissingColumnError as e:
        logger.error(f"Ontbrekende kolom: {e}")
        return 1

    report_data = report.analyse_orders(orders)
    logger.info("Aggregeren: producten, klanten, categorieën")

    try:
        writer.write_report(report_data, args.output, args.format)
        logger.info(f"Geschreven naar {args.output}")
        print("[OK] Klaar — exit 0")
    except OSError as e:
        logger.error(f"Kan het rapport niet schrijven: {e}")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
