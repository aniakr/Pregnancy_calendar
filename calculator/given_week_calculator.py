from datetime import datetime
from datetime import timedelta

def week_calculator(required_week, LMP):
    first_day_of_week=datetime.strptime(LMP, "%m/%d/%y")+timedelta(weeks=required_week)
    return first_day_of_week

