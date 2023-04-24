import random

class Player:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.bet = 0

    def place_bet(self, bet_amount):
        if bet_amount > self.balance:
            print(f"{self.name} no tiene suficiente saldo para apostar {bet_amount} euros.")
            return False
        self.bet = bet_amount
        self.balance -= bet_amount
        return True

    def win(self, payout):
        self.balance += payout
        print(f"{self.name} ha ganado {payout} euros.")

    def lose(self):
        self.bet = 0
        print(f"{self.name} ha perdido.")

class Roulette:
    def __init__(self):
        self.numbers = list(range(37))
        self.ball = None

    def spin(self):
        self.ball = random.choice(self.numbers)
        print(f"Ha salido el número {self.ball}.")

    def is_even(self):
        return self.ball % 2 == 0

class FrenchRoulette(Roulette):
    def __init__(self):
        super().__init__()
        self.numbers.remove(0)

class Game:
    def __init__(self, players, casino_balance):
        self.players = players
        self.casino_balance = casino_balance
        self.casino_wins = 0

    def play_french_roulette(self):
        roulette = FrenchRoulette()
        for player in self.players:
            if player.balance == 0:
                print(f"{player.name} no tiene saldo suficiente para jugar.")
                continue
            bet_amount = 10
            if player.place_bet(bet_amount):
                if player.name == "Banco":
                    self.casino_balance += bet_amount
                else:
                    roulette.spin()
                    if roulette.ball == player.bet:
                        payout = 36 * bet_amount
                        player.win(payout)
                        self.casino_balance -= payout
                    else:
                        player.lose()
                        self.casino_balance += bet_amount

    def play_even_odd(self):
        roulette = Roulette()
        for player in self.players:
            if player.balance == 0:
                print(f"{player.name} no tiene saldo suficiente para jugar.")
                continue
            bet_amount = 10
            if player.place_bet(bet_amount):
                if player.name == "Banco":
                    self.casino_balance += bet_amount
                else:
                    roulette.spin()
                    if roulette.is_even() and player.bet == "par":
                        player.win(20)
                        self.casino_balance -= 20
                    elif not roulette.is_even() and player.bet == "impar":
                        player.win(20)
                        self.casino_balance -= 20
                    else:
                        player.lose()
                        self.casino_balance += bet_amount

    def play_martingale(self):
        roulette = FrenchRoulette()
        for player in self.players:
            if player.balance == 0:
                print(f"{player.name} no tiene saldo suficiente para jugar.")
                continue
            bet_amount = 10
            if player.place_bet(bet_amount):
                if player.name == "Banco":
                    self.casino_balance += bet_amount
                else:
                    while True:
                        roulette.spin()
                        if roulette.ball == player.bet:
                            payout = 36 * bet_amount
                            player.win(payout)
                            self.casino_balance -= payout
                            break
                        else:
                            player.lose()
