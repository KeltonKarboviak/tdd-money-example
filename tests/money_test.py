from unittest import TestCase

from money.dollar import Dollar
from money.franc import Franc


class MoneyTest(TestCase):

    def test_multiplication(self):
        # act
        five = Dollar(5)

        # assert
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_franc_multiplication(self):
        # act
        five = Franc(5)

        # assert
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equality(self):
        # assert
        self.assertTrue(Dollar(5) == Dollar(5))
