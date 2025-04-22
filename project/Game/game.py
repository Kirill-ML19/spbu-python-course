from project.Game.roulette import Roulette
from project.Game.bot_manager import BotManager


class Game:
    def __init__(self, bots, max_rounds=100):
        """
        The Game class controls the game process

        param bots: list of bot objects
        param max_rounds: maximum number of rounds
        """
        self.roulette = Roulette()
        self.bots = BotManager(bots)
        self.max_rounds = max_rounds
        self.current_round = 0

    def play(self):
        print("\n=== Start of the game ===")
        while not self.bots.has_winner() and self.current_round < self.max_rounds:
            self.current_round += 1
            print(f"\n--- Round {self.current_round} ---")
            number = self.roulette.spin()
            print(f"The number dropped: {number}")

            for bot in self.bots.get_bots():
                bet_number = bot.bet(number)
                print(
                    f"{bot.name} bet on number {bet_number} with remaining bank: {bot.bank}"
                )

            self.bots.remove_bankrupts()

            self.bots.print_statuses()

        print("\n=== Game over ===")
        winners = self.bots.get_winners()
        if winners:
            print("Winner:")
            for bot in winners:
                print(f"- {bot.name} with bank {bot.bank}")
        else:
            print("There are no winners")
