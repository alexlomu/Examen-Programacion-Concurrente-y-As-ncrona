from clases import *
if __name__ == "__main__":
    
    player1 = Player("Flecha", 10000)
    player2 = Player("Alex", 10000)
    player3 = Player("Carlos", 10000)
    player4 = Player("German", 10000)

    Game([player1, player2, player3, player4], 50000)
    Game.play_even_odd(player1)
    