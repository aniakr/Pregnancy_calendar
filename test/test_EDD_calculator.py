from unittest import TestCase
from calculator import pregnancy_calendar
x=pregnancy_calendar.PregnancyCalendar('4/2/19')
import datetime


class Testedd(TestCase):
    def test_edd_dot_format(self):
        result = x.edd_calculator()
        self.assertEqual(result,datetime.datetime.strptime('1/7/20', "%m/%d/%y"))
