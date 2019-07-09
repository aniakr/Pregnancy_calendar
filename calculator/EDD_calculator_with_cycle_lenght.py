from datetime import datetime
from datetime import timedelta


def EDD_calculator_with_cycle_lenght(LMP,cycle_lenght):
    date_1 = datetime.strptime(LMP, "%m/%d/%y")
    EDD=date_1+timedelta(days=280-(28-cycle_lenght))
    return EDD
