from datetime import datetime
from datetime import timedelta


def EDD_calculator(LMP):
    date_1 = datetime.strptime(LMP, "%m/%d/%y")
    EDD=date_1+timedelta(days=280)
    return EDD


