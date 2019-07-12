from unittest import TestCase
from calculator import pregnancy_calendar
import datetime


class TestPregnancyCalculator(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.calc=pregnancy_calendar.PregnancyCalendar('4/2/19')

    def test_incorrectInitialDate(self):
        with self.assertRaises(ValueError):
            pregnancy_calendar.PregnancyCalendar('dupa')

    def test_edd_calculator_with_cycle_lenght_shorter(self):
        result= self.calc.edd_calculator_with_cycle_lenght(27)
        self.assertEqual(result, datetime.datetime.strptime('1/6/20', "%m/%d/%y"))

    def test_edd_calculator_with_cycle_lenght_longer(self):
        result=  self.calc.edd_calculator_with_cycle_lenght(30)
        self.assertEqual(result, datetime.datetime.strptime('1/9/20', "%m/%d/%y"))

    def test_edd_dot_format(self):
        result = self.calc.edd_calculator()
        self.assertEqual(result, datetime.datetime.strptime('1/7/20', "%m/%d/%y"))

    def test_given_week_calculator_standard(self):
        result=self.calc.given_week_calculator(14)
        self.assertEqual(result,datetime.datetime.strptime('7/9/19', "%m/%d/%y"))

    def test_current_week(self):
        result = self.calc.current_week()
        self.assertEqual(result, (14, 3))

    def test_week_at_given_date(self):
        result=self.calc.week_at_given_date('8/20/19')
        self.assertEqual(result,(20,0))



