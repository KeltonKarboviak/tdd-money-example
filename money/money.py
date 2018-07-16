

class Money(object):

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and self.__class__ == other.__class__)

    def times(self, multiplier):
        raise NotImplementedError('Need to implement in concrete class.')

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollar(Money):

    def __init__(self, amount):
        super(Dollar, self).__init__(amount)

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):

    def __init__(self, amount):
        super(Franc, self).__init__(amount)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
