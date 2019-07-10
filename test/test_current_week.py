from unittest import TestCase
from calculator import pregnancy_calendar
x=pregnancy_calendar.PregnancyCalendar('4/2/19')

class TestCurrent_week(TestCase):
    def test_current_week(self):
        result=x.current_week()
        self.assertEqual(result,(14,1))
