from unittest import TestCase
from calculator import pregnancy_calendar
x=pregnancy_calendar.PregnancyCalendar('4/2/19')
import datetime

class TestWeek_calculator(TestCase):
    def test_week_calculator_standard(self):
        result= x.given_week_calculator(14)
        self.assertEqual(result,datetime.datetime.strptime('7/9/19', "%m/%d/%y"))
