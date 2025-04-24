import random
from project.Game.bot import Bot
from project.Game.strategy_meta import StrategyMeta


class RandomBot(Bot, metaclass=StrategyMeta):
    def bet(self, number):
        bet_number = random.randint(0, 36)
        bet_amount = min(10, self.bank)
        won = bet_number == number
        self.bank += 35 * bet_amount if won else -bet_amount
        return bet_number
