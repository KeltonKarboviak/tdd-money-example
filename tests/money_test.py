from unittest import TestCase

from money.money import Money, Bank, Sum


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
        self.assertFalse(Money.dollar(5) == Money.franc(5))

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

    def test_plus_returns_sum(self):
        # arrange
        five = Money.dollar(5)

        # act
        result = five.plus(five)
        sum = result

        # assert
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)

    def test_reduce_sum(self):
        # arrange
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()

        # act
        result = bank.reduce(sum, 'USD')

        # assert
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        # arrange
        bank = Bank()

        # act
        result = bank.reduce(Money.dollar(1), 'USD')

        # assert
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        # arrange
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        # act
        result = bank.reduce(Money.franc(2), 'USD')

        # assert
        self.assertEqual(Money.dollar(1), result)

    def test_identify_rate(self):
        # assert
        self.assertEqual(1, Bank().rate('USD', 'USD'))

    def test_mixed_addition(self):
        # arrange
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        # act
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')

        # assert
        self.assertEqual(Money.dollar(10), result)

    def test_sum_plus_money(self):
        # arrange
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        # act
        sum = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(sum, 'USD')

        # assert
        self.assertEqual(Money.dollar(15), result)

    def test_sum_times(self):
        # arrange
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        # act
        sum = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum, 'USD')

        # assert
        self.assertEqual(Money.dollar(20), result)
