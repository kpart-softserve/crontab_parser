def cron_printer(cron_dict):
    for key,value in cron_dict.items():
        if key == "command":
            print (f"{key} {value}")
        else:
            list_value = list(value)
            print(f"{key} {' '.join(str(x) for x in list_value)}")
