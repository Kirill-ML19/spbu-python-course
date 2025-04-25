class Bot:
    def __init__(self, name, bank=100):
        """
        Bot base class

        param name: bot name
        param bank: starting amount
        """
        self.name = name
        self.bank = bank

    def bet(self, number):
        """
        Rate method - defined in subclasses
        """
        raise NotImplementedError

    def update(self, result):
        """
        Updates the bank depending on the result
        """
        raise NotImplementedError
