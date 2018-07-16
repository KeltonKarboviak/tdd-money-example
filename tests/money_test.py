from unittest import TestCase

from money.money import Money


class MoneyTest(TestCase):

    def test_multiplication(self):
        # act
        five = Money.dollar(5)

        # assert
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_franc_multiplication(self):
        # act
        five = Money.franc(5)

        # assert
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_equality(self):
        # assert
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))

        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))

        self.assertTrue(Money.dollar(5) == Money.franc(5))

