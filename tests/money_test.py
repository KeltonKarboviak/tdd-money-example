from unittest import TestCase

from money.dollar import Dollar


class MoneyTest(TestCase):

    def test_multiplication(self):
        # act
        five = Dollar(5)

        # assert
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        # assert
        self.assertTrue(Dollar(5) == Dollar(5))
