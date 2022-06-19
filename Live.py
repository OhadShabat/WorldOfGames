import MemoryGame, GuessGame, CurrencyRouletteGame
import Score


def welcome(name):
    print("Hello {print_name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play\n".format(
    print_name=name))
    input()

def menu():
    print("Please choose a game to play or -1 to stop")
    print("   1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("   2.Guess Game - guess a number and see if you chose like the computer")
    print("   3.Currency Roulette - try and guess the value of a random amount of USD in ILS")


def load_game():
    games = [MemoryGame.MemoryGame, GuessGame.GuessGame, CurrencyRouletteGame.CurrencyRouletteGame]

    chooseGame=0

    while (chooseGame != -1) and (chooseGame != 1) and (chooseGame != 2) and (chooseGame != 3):
        menu()
        chooseGame=int(input(""))
        if (chooseGame == -1):
            return -1

    gameDifficulty = int(input("Please choose game difficulty from 1 to 5: "))
    while (gameDifficulty < 1) or (gameDifficulty > 5):
        gameDifficulty = int(input("Please choose game difficulty from 1 to 5: "))


    game = games[chooseGame-1](gameDifficulty)
    return game.play()

if __name__ == '__main__':
    load_game()