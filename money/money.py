

class Expression(object):
    """Interface"""

    def reduce(self, to: str) -> 'Money':
        raise NotImplementedError('Need to implement in concrete class')


class Sum(Expression):

    def __init__(self, augend: 'Money', addend: 'Money'):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> 'Money':
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)


class Money(Expression):

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (
            self.amount == other.amount
            and self.currency == other.currency)

    def times(self, multiplier: int) -> 'Money':
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend: 'Money') -> 'Expression':
        return Sum(self, addend)

    def reduce(self, to: str) -> 'Money':
        return self

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')


class Bank(object):

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)
