import cli
import reader
import report

args = cli.main()

orders = reader.read_orders(args.input)
report_data = report.analyse_orders(orders)

print(report_data)
