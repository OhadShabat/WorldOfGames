import random

class GuessGame:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.SecretNumber = 0

    def generate_number(self):
        self.SecretNumber = random.randint(1, self.Difficulty)

    def get_guess_from_user(self):
        return(int(input("please enter a number between 1 to " + str(self.Difficulty) + " ")))

    def compare_results(self, Number):
        return (self.SecretNumber == Number)

    def play(self):
        self.generate_number()
        MyNumber = self.get_guess_from_user()
        if (self.compare_results(MyNumber)):
            #  Win
            return (self.Difficulty * 3 + 5)
        else: # Lost
            return 0

def main():
    game1 = GuessGame(10)
    game1.play()
    print("Difficuly : " + str(game1.Difficulty))
    print("Secret number : " + str(game1.SecretNumber))

    game2 = GuessGame(100)
    game2.play()
    print("Difficuly : " + str(game2.Difficulty))
    print("Secret number : " + str(game2.SecretNumber))

if __name__ == '__main__':
    main()
