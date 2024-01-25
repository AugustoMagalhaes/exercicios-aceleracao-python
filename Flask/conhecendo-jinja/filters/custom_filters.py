from datetime import datetime


def convert_date(date):
    data_obj = datetime.strptime(date, "%Y-%m-%d")
    return data_obj.strftime("%d/%m/%Y")
