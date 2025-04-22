class GameRuleMeta(type):
    config = {
        "roulette_size": 37,
        "win_multiplier": 35,
    }

    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        cls.config = GameRuleMeta.config
        return cls

    @classmethod
    def update_rules(cls, **kwargs):
        cls.config.update(kwargs)
