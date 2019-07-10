from datetime import datetime
from datetime import timedelta

class PregnancyCalendar:
    "You can count important dates during your pregnancy thanks to this calendar"

    def __init__(self, lmp):
        self.lmp = lmp

    def given_week_calculator(self,required_week):
        first_day_of_week = datetime.strptime(self.lmp, "%m/%d/%y") + timedelta(weeks=required_week)
        return first_day_of_week

    def current_week(self):
        delta = datetime.now() - datetime.strptime(self.lmp, "%m/%d/%y")
        current_week = int(delta.days / 7)
        days = delta.days % 7
        return current_week, days

    def edd_calculator(self):
        date_1 = datetime.strptime(self.lmp, "%m/%d/%y")
        edd = date_1 + timedelta(days=280)
        return edd

    def edd_calculator_with_cycle_lenght(self,cycle_lenght):
        date_1 = datetime.strptime(self.lmp, "%m/%d/%y")
        edd=date_1+timedelta(days=280-(28-cycle_lenght))
        return edd