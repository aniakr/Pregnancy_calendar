from unittest import TestCase
from calculator import pregnancy_calendar
x=pregnancy_calendar.PregnancyCalendar('4/2/19')
import datetime


class Testedd_calculator_with_cycle_lenght(TestCase):
    def test_edd_calculator_with_cycle_lenght_shorter(self):
        result= x.edd_calculator_with_cycle_lenght(27)
        self.assertEqual(result, datetime.datetime.strptime('1/6/20', "%m/%d/%y"))

    def test_edd_calculator_with_cycle_lenght_longer(self):
        result=  x.edd_calculator_with_cycle_lenght(30)
        self.assertEqual(result, datetime.datetime.strptime('1/9/20', "%m/%d/%y"))