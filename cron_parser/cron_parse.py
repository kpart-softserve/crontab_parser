from celery.schedules import crontab_parser

def expression_parse(expression, max, min=0):
    result_list = []
    special_characters = ['*', '/', ',', '-']

    if not any(char in expression for char in special_characters):
        result_list.append(expression)
        return result_list
    
    if '/' in expression:
        if '*/' not in expression:
            raise ValueError
        if expression.count('*/') != 1:
            raise ValueError

        # */15 in months (12) is possible - no check
        
        step = expression.split('*/', 1)[1]
        for x in range(min, max, int(step)):
            result_list.append(x)
        return result_list
    
    if '*' in expression:
        if expression.count('*') != 1:
            raise ValueError
        
        for x in range(min, max):
            result_list.append(x)
        return result_list
    
    if ',' in expression:
        result_list = expression.split(',')
        if int(sorted(result_list)[len(result_list) - 1]) > max:
            raise ValueError
        if int(sorted(result_list)[0]) < min:
            raise ValueError
        return result_list
    
    if '-' in expression:
        if expression.count('-') != 1:
            raise ValueError
        
        temp_range = expression.split('-')

        for x in range(int(temp_range[0]), int(temp_range[1]) + 1):
            result_list.append(x)

        if int(sorted(result_list)[len(result_list) - 1]) > max:
            raise ValueError
        if int(sorted(result_list)[0]) < min:
            raise ValueError
        return result_list


def no_dependency_cron_parse(cron_line):
    try:
        if (len(cron_line.split()) > 6):
            raise IndexError
        
        cron_dict = {}
        cron_dict["minute"] = sorted(
            expression_parse(cron_line.split()[0], 60))
        cron_dict["hour"] = sorted(
            expression_parse(cron_line.split()[1], 24))
        cron_dict["day of month"] = sorted(
            expression_parse(cron_line.split()[2], 60, 1))
        cron_dict["month"] = sorted(
            expression_parse(cron_line.split()[3], 13, 1))
        cron_dict["day of week"] = sorted(
            expression_parse(cron_line.split()[4], 8, 1))
        cron_dict["command"] = cron_line.split()[5]

        return cron_dict

    except ValueError:
        print("Wrong crontab entry")
        exit(1)
    except IndexError:
        print("Wrong crontab entry")
        exit(1)

def cron_parse(cron_line):
    try:
        if (len(cron_line.split()) > 6):
            raise IndexError
        
        cron_dict = {}
        cron_dict["minute"] = sorted(
            crontab_parser(60).parse(cron_line.split()[0]))
        cron_dict["hour"] = sorted(
            crontab_parser(24).parse(cron_line.split()[1]))
        cron_dict["day of month"] = sorted(
            crontab_parser(30, 1).parse(cron_line.split()[2]))
        cron_dict["month"] = sorted(crontab_parser(
            12, 1).parse(cron_line.split()[3]))
        cron_dict["day of week"] = sorted(
            crontab_parser(7, 1).parse(cron_line.split()[4]))
        cron_dict["command"] = cron_line.split()[5]

        return cron_dict

    except ValueError:
        print("Wrong crontab entry")
        exit(1)
    except IndexError:
        print("Wrong crontab entry")
        exit(1)
