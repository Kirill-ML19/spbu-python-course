class BotManager:
    def __init__(self, bots):
        self.bots = bots

    def make_bets(self, number):
        for bot in self.bots:
            if bot.bank > 0:
                result = bot.bet(number)
                print(f"{bot.name} {'win' if result else 'lost'} | Bank: {bot.bank}")

    def remove_bankrupts(self):
        self.bots = [b for b in self.bots if b.bank > 0]

    def has_winner(self):
        return len(self.bots) == 1

    def get_winners(self):
        if len(self.bots) == 1 and self.bots[0].bank > 0:
            return self.bots
        return []

    def print_statuses(self):
        print("\nPlayers status:")
        for bot in self.bots:
            print(f"{bot.name}: {bot.bank}")

    def get_bots(self):
        return self.bots
