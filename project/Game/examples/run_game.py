from project.Game.strategies.random_bot import RandomBot
from project.Game.strategies.aggressive_bot import AggressiveBot
from project.Game.strategies.martingale_bot import MartingaleBot
from project.Game.game import Game
from project.Game.rules_meta import GameRuleMeta

if __name__ == "__main__":
    GameRuleMeta.update_rules(roulette_size=20, win_multiplier=50)
    bots = [
        RandomBot("Random_bot"),
        AggressiveBot("Aggressive_bot"),
        MartingaleBot("Martingale_bot"),
    ]

    game = Game(bots, max_rounds=50)
    game.play()
