
class Money(object):

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and self.__class__ == other.__class__)
