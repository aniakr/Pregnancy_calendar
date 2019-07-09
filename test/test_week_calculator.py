from unittest import TestCase
import datetime

from calculator import given_week_calculator


class TestWeek_calculator(TestCase):
    def test_week_calculator_standard(self):
        result= given_week_calculator.week_calculator(14, '4/2/19')
        self.assertEqual(result,datetime.datetime.strptime('7/9/19', "%m/%d/%y"))
