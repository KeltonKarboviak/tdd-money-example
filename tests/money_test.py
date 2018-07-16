from unittest import TestCase

from money.money import Expression, Money, Bank


class MoneyTest(TestCase):

    def test_multiplication(self):
        # act
        five = Money.dollar(5)

        # assert
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        # assert
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Money.dollar(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency)
        self.assertEqual('CHF', Money.franc(1).currency)

    def test_simple_addition(self):
        # arrange
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()

        # act
        reduced = bank.reduce(sum, 'USD')

        # assert
        self.assertEqual(Money.dollar(10), reduced)
