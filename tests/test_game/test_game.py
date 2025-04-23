import pytest
from project.Game.game import Game
from project.Game.strategies.random_bot import RandomBot
from project.Game.strategies.aggressive_bot import AggressiveBot
from project.Game.strategies.martingale_bot import MartingaleBot
from project.Game.bot_manager import BotManager
from project.Game.rules_meta import GameRuleMeta


def test_bot_betting():
    bot = RandomBot("TestBot")
    bet_number = bot.bet(17)
    assert (
        bet_number >= 0 and bet_number <= 36
    ), "Bot should bet on a number between 0 and 36"
    assert bot.bank != 100, "Bot's bank should change after a bet"

    bot = AggressiveBot("AggressiveBot")
    bet_number = bot.bet(17)
    assert (
        bet_number >= 30 and bet_number <= 36
    ), "AggressiveBot should bet on numbers between 30 and 36"

    bot = MartingaleBot("MartingaleBot")
    bet_number = bot.bet(17)
    assert bet_number == 17, "MartingaleBot should always bet on number 17"


def test_game_over_after_max_rounds():
    GameRuleMeta.update_rules(roulette_size=20, win_multiplier=50)
    bots = [
        RandomBot("Random_bot"),
        AggressiveBot("Aggressive_bot"),
        MartingaleBot("Martingale_bot"),
    ]
    game = Game(bots, max_rounds=5)
    game.play()

    assert (
        game.current_round == 5
    ), "Game should stop after the maximum number of rounds"
    assert len(game.bots.get_bots()) > 0, "Game should have at least one bot remaining"


def test_winner_detection():
    GameRuleMeta.update_rules(roulette_size=20, win_multiplier=50)
    bots = [
        RandomBot("Random_bot"),
        AggressiveBot("Aggressive_bot"),
        MartingaleBot("Martingale_bot"),
    ]
    game = Game(bots, max_rounds=50)
    game.play()

    winners = game.bots.get_winners()
    assert len(winners) > 0, "There should be at least one winner"

    for winner in winners:
        assert winner.bank > 0, "Winner's bank should be greater than 0"


def test_remove_bankrupts():
    bot1 = RandomBot("Bot1", 0)
    bot2 = RandomBot("Bot2", 100)
    bot_manager = BotManager([bot1, bot2])

    bot_manager.remove_bankrupts()

    assert (
        len(bot_manager.bots) == 1
    ), "BotManager should have only one non-bankrupt bot"
    assert bot_manager.bots[0].name == "Bot2", "The remaining bot should be Bot2"


def test_has_winner():
    bot1 = RandomBot("Bot1", 0)
    bot2 = RandomBot("Bot2", 100)
    bot_manager = BotManager([bot1, bot2])

    assert not bot_manager.has_winner(), "BotManager should not have a winner yet"

    bot_manager.remove_bankrupts()
    assert bot_manager.has_winner(), "BotManager should have a winner now"


def test_get_winners():
    bot1 = RandomBot("Bot1", 0)
    bot2 = RandomBot("Bot2", 100)
    bot_manager = BotManager([bot1, bot2])

    bot_manager.remove_bankrupts()
    winners = bot_manager.get_winners()
    assert len(winners) == 1, "There should be exactly one winner"
    assert winners[0].name == "Bot2", "The winner should be Bot2"


def test_update_rules():
    GameRuleMeta.update_rules(roulette_size=10, win_multiplier=20)

    assert (
        GameRuleMeta.config["roulette_size"] == 10
    ), "Roulette size should be updated to 10"
    assert (
        GameRuleMeta.config["win_multiplier"] == 20
    ), "Win multiplier should be updated to 20"


def test_game_start():
    GameRuleMeta.update_rules(roulette_size=10, win_multiplier=10)
    bots = [
        RandomBot("Random_bot"),
        AggressiveBot("Aggressive_bot"),
        MartingaleBot("Martingale_bot"),
    ]
    game = Game(bots, max_rounds=10)

    game.play()
    assert game.current_round <= 10, "Game should not exceed the max number of rounds"
    assert len(game.bots.get_bots()) > 0, "There should be at least one bot remaining"


if __name__ == "__main__":
    pytest.main()
