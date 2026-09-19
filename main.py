import logging
from errors import InvalidCsvError, MissingColumnError
import cli
import reader
import report
import writer

logging.basicConfig(format='[%(levelname)s] %(message)s', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    args = cli.main()
except ValueError as e:
    logger.error(e)
    exit(2)

try:
    orders = reader.read_orders(args.input)
    logger.info(f"Inlezen data/orders_{orders[0]['datum']} ({len(orders)} rows, 0 fouten)")
except FileNotFoundError:
    logger.error('Bestand is niet gevonden')
    exit(1)
except InvalidCsvError as e:
    logger.error(e)
    exit(1)
except MissingColumnError as e:
    logger.error(f'Ontbrekende kolom: {e}')
    exit(1)

report_data = report.analyse_orders(orders)
logger.info(f'Aggregeren: producten, klanten, categorieën')

try:
    writer.write_report(report_data, args.output, args.format)
    logger.info(f"Geschreven naar {args.output}")
    print('[OK] Klaar — exit 0')
except PermissionError:
    logger.error('Geen toestemming om het bestand te schrijven.')
    exit(2)
