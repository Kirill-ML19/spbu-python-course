import random
from project.Game.rules_meta import GameRuleMeta


class Roulette(metaclass=GameRuleMeta):
    def spin(self):
        """
        Spins the roulette and returns a random number
        """
        return random.randint(0, self.config["roulette_size"] - 1)
