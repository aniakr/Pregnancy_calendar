from datetime import datetime
from datetime import timedelta

class PregnancyCalendar:
    "You can count important dates during your pregnancy thanks to this calendar"

    def __init__(self, lmp):
        self.lmp = datetime.strptime(lmp, "%m/%d/%y")

    def get_now(self):
        return datetime.now()

    def given_week_calculator(self,required_week):
        first_day_of_week = self.lmp + timedelta(weeks=required_week)
        return first_day_of_week

    def current_week(self):
        delta = self.get_now() - self.lmp
        current_week = int(delta.days / 7)
        days = delta.days % 7
        return current_week, days

    def edd_calculator(self):
        date_1 = self.lmp
        edd = date_1 + timedelta(days=280)
        return edd

    def edd_calculator_with_cycle_lenght(self,cycle_lenght):
        date_1 = self.lmp
        edd=date_1+timedelta(days=280-(28-cycle_lenght))
        return edd

    def week_at_given_date(self, given_date):
        days_between=datetime.strptime(given_date, "%m/%d/%y")-self.lmp
        week=int(days_between.days/7)
        days = days_between.days % 7
        return week, days


