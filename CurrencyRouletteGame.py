import requests
import random
from forex_python.converter import CurrencyRates

def usd2ils():
    c = CurrencyRates()
    return (1 / c.get_rate('ILS', 'USD'))

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.Difficulty = difficulty

    def get_money_interval(self, t):
        return t-(5-self.Difficulty), t+(5-self.Difficulty)

    def get_guess_from_user(self, dollar_amount):
        return float(input("please enter your guess of the value of " + str(dollar_amount) + "$ to ILS: "))

    def play(self):
        dollar_amount = random.randint(1, 100)
        ils_amount = usd2ils() * dollar_amount
        interval = self.get_money_interval(ils_amount)
        user_guess = self.get_guess_from_user(dollar_amount)
        if (interval[0] <= user_guess) and (interval[1] >= user_guess):
            #  Win
            return (self.Difficulty * 3 + 5)
        else:  # Lost
            return 0

def main():
    print("Dollar rate = " + str(usd2ils()))
    difficulty = int(input("please enter game difficulty (1-5):"))
    game1 = CurrencyRouletteGame(difficulty)
    game1.play()

if __name__ == '__main__':
    main()