from celery.schedules import crontab_parser


def cron_parse(cron_line):
    try:
        if (len(cron_line.split()) > 6):
            raise IndexError
        cron_dict = {}
        cron_dict["minute"] = sorted(crontab_parser(60).parse(cron_line.split()[0]))
        cron_dict["hour"] = sorted(crontab_parser(24).parse(cron_line.split()[1]))
        cron_dict["day of month"] = sorted(crontab_parser(30, 1).parse(cron_line.split()[2]))
        cron_dict["month"] = sorted(crontab_parser(12, 1).parse(cron_line.split()[3]))
        cron_dict["day of week"] = sorted(crontab_parser(7, 1).parse(cron_line.split()[4]))
        cron_dict["command"] = cron_line.split()[5]
        
        return cron_dict

    except ValueError:
        print("Wrong crontab entry")
        exit(1)
    except IndexError:
        print("Wrong crontab entry")
        exit(1)
