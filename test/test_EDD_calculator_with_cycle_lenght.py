from unittest import TestCase
import datetime

from calculator import EDD_calculator_with_cycle_lenght


class TestEDD_calculator_with_cycle_lenght(TestCase):
    def test_EDD_calculator_with_cycle_lenght_shorter(self):
        result= EDD_calculator_with_cycle_lenght.EDD_calculator_with_cycle_lenght('4/2/19', 27)
        self.assertEqual(result, datetime.datetime.strptime('1/6/20', "%m/%d/%y"))

    def test_EDD_calculator_with_cycle_lenght_longer(self):
        result= EDD_calculator_with_cycle_lenght.EDD_calculator_with_cycle_lenght('4/2/19', 30)
        self.assertEqual(result, datetime.datetime.strptime('1/9/20', "%m/%d/%y"))