from cron_parser.argparse import argument_parser
from cron_parser.cron_parse import cron_parse, no_dependency_cron_parse
from cron_parser.cron_printer import cron_printer


def main_function():
    cron_line = argument_parser()

    # Version with celery dependency
    # cron_dict = cron_parse(cron_line)

    # Version with no dependency
    cron_dict = no_dependency_cron_parse(cron_line)

    cron_printer(cron_dict)
