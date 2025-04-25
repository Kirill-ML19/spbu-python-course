import random
from project.Game.bot import Bot
from project.Game.strategy_meta import StrategyMeta


class AggressiveBot(Bot, metaclass=StrategyMeta):
    def bet(self, number):
        bet_number = random.choice(range(30, 37))
        bet_amount = min(self.bank, 50)
        won = bet_number == number
        self.bank += 35 * bet_amount if won else -bet_amount
        return bet_number
