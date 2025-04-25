from project.Game.bot import Bot
from project.Game.strategy_meta import StrategyMeta


class MartingaleBot(Bot, metaclass=StrategyMeta):
    def __init__(self, name, bank=100):
        super().__init__(name, bank)
        self.last_bet = 1

    def bet(self, number):
        bet_number = 17
        bet_amount = min(self.bank, self.last_bet)
        won = bet_number == number
        if won:
            self.bank += 35 * bet_amount
            self.last_bet = 1
        else:
            self.bank -= bet_amount
            self.last_bet *= 2
        return bet_number
