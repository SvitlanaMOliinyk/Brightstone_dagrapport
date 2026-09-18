import cli
import reader
import report
import writer

args = cli.main()

orders = reader.read_orders(args.input)
report_data = report.analyse_orders(orders)
writer.write_report(report_data, args.output, args.format)


