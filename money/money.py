

class Expression(object):
    """Interface"""

    def plus(self, addend: 'Expression') -> 'Expression':
        raise NotImplementedError('Need to implement in concrete class')

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        raise NotImplementedError('Need to implement in concrete class')


class Sum(Expression):

    def __init__(self, augend: 'Expression', addend: 'Expression'):
        self.augend = augend
        self.addend = addend

    def times(self, multiplier: int) -> 'Expression':
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def plus(self, addend: 'Expression') -> 'Expression':
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        amount = self.augend.reduce(bank, to).amount \
            + self.addend.reduce(bank, to).amount
        return Money(amount, to)


class Money(Expression):

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f'<Money(amount={self.amount}, ' \
            f'currency={self.currency})>'

    def __repr__(self):
        return str(self)

    def __eq__(self, other: 'Money') -> bool:
        return (
            self.amount == other.amount
            and self.currency == other.currency)

    def times(self, multiplier: int) -> 'Expression':
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend: 'Expression') -> 'Expression':
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')


class Pair(object):

    def __init__(self, _from: str, to: str):
        self._from = _from
        self.to = to

    def __eq__(self, other: 'Pair') -> bool:
        return self._from == other._from and self.to == other.to

    def __hash__(self):
        return hash((self._from, self.to))


class Bank(object):

    def __init__(self):
        self.rates = {}

    def add_rate(self, _from: str, to: str, rate: int):
        self.rates[Pair(_from, to)] = rate
        return int(rate)

    def rate(self, _from: str, to: str) -> int:
        if _from == to:
            return 1

        rate = self.rates.get(Pair(_from, to))
        return int(rate)

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)
