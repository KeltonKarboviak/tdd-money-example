from unittest import TestCase

from money.dollar import Dollar


class MoneyTest(TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)

        product = five.times(3)
        self.assertEqual(15, product.amount)
