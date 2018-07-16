

class Money(object):

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (
            self.amount == other.amount
            and self.__class__ == other.__class__)

    def times(self, multiplier: int) -> int:
        raise NotImplementedError('Need to implement in concrete class.')

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Franc(amount, None)


class Dollar(Money):

    def __init__(self, amount: int, currency: str):
        super(Dollar, self).__init__(amount, currency)

    def times(self, multiplier: int) -> int:
        return Money.dollar(self.amount * multiplier)


class Franc(Money):

    def __init__(self, amount: int, currency: str):
        super(Franc, self).__init__(amount, currency)

    def times(self, multiplier: int) -> int:
        return Money.franc(self.amount * multiplier)
