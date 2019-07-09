from unittest import TestCase
import datetime
from calculator import EDD_calculator


class TestEDD(TestCase):
    def test_EDD_dot_format(self):
        result = EDD_calculator.EDD_calculator('4/2/19')
        self.assertEqual(result,datetime.datetime.strptime('1/7/20', "%m/%d/%y"))
