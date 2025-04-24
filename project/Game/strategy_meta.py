from typing import List, Type


class StrategyMeta(type):
    """
    Metaclass for registering bot strategies.
    Keeps track of all strategy classes created based on this metaclass.

    Attributes:
        registry (list): A list containing all registered strategies.

    Methods:
        get_strategies(cls): Returns all registered strategies.
    """

    registry: List[Type] = []

    def __new__(cls, name, bases, dct):
        """
        Creates a new class based on the StrategyMeta metaclass.
        Registers the strategy if the class name is not "Bot".

        Arguments:
            cls: The metaclass used to create the new class.
            name: The name of the class to create.
            bases: A tuple of base classes.
            dct: A dictionary containing the attributes of the class.

        Returns:
            A new class with the registered strategy class.
        """
        new_cls = super().__new__(cls, name, bases, dct)
        if name != "Bot":
            StrategyMeta.registry.append(new_cls)
        return new_cls

    @classmethod
    def get_strategies(cls):
        """
        Returns a list of all registered strategies.

        Returns:
            list: A list of all strategies registered in registry.
        """
        return cls.registry
