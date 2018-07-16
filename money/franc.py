from .money import Money


class Franc(Money):

    def __init__(self, amount):
        super(Franc, self).__init__(amount)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
