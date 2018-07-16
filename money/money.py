

class Money(object):

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (
            self.amount == other.amount
            and self.currency == other.currency)

    def times(self, multiplier: int) -> 'Money':
        return Money(self.amount * multiplier, self.currency)

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Money(amount, 'CHF')
