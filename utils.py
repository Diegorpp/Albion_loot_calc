from decimal import Decimal

TAXA_MERCADO = 0.94

class Player:
    def __init__(self, name: str, return_cost: Decimal = 0,
                 repair_cost: Decimal = 0, silver: int = 0,
                 loot: Decimal = 0, loot_com_desconto: Decimal = 0):
        self.name = name
        self.return_cost = return_cost
        self.repair_cost = repair_cost
        self.silver = silver
        self.loot = loot
        self.loot_com_desconto = loot_com_desconto
        self.proportional_profit = 0

    def __repr__(self):
        return f"Player(name={self.name}, return_cost={self.return_cost}, " \
               f"repair_cost={self.repair_cost}, silver={self.silver}, loot={self.loot}), " \
               f"loot_com_desconto={self.loot_com_desconto}), proportional_profit={self.proportional_profit})"


class HuntingParty:
    def __init__(self):
        self.players = []
        self.liquid_profit = 0
        self.total_cost = 0
        self.total_loot = 0
        self.profit_per_player = 0
        self.loot_with_discount = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def __repr__(self):
        return f"HuntingParty(players={self.players}, liquid_profit={self.liquid_profit}, " \
               f"total_cost={self.total_cost}, total_loot={self.total_loot}, " \
               f"profit_per_player={self.profit_per_player}, loot_with_discount={self.loot_with_discount})"
        

class LootResponse:
    def __init__(self, name: str, liquid_profit: Decimal,
                 proportional_profit: Decimal, loot_with_discount: Decimal):
        self.name = name
        self.liquid_profit = liquid_profit
        self.proportional_profit = proportional_profit
        self.loot_with_discount = loot_with_discount

    def __repr__(self):
        return f"LootResponse(name={self.name}, liquid_profit={self.liquid_profit}, " \
               f"proportional_profit={self.proportional_profit}, loot_with_discount={self.loot_with_discount})"

if "__name__" == "__main__":
    player1 = Player("Player1", 100, 50, 200, 500)
    player2 = Player("Player2", 150, 75, 300, 600)
    breakpoint()
