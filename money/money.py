

class Money(object):

    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other: 'Money') -> bool:
        return (
            self.amount == other.amount
            and self.__class__ == other.__class__)

    def times(self, multiplier: int) -> int:
        raise NotImplementedError('Need to implement in concrete class.')

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Franc(amount)


class Dollar(Money):

    def __init__(self, amount: int):
        super(Dollar, self).__init__(amount)

    def times(self, multiplier: int) -> int:
        return Dollar(self.amount * multiplier)


class Franc(Money):

    def __init__(self, amount: int):
        super(Franc, self).__init__(amount)

    def times(self, multiplier: int) -> int:
        return Franc(self.amount * multiplier)
