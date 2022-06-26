import random, time, os
import tkinter as tk
import Utils

class MemoryGame:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.GeneratedNumbers = []
        self.UserNumbers = []

    def generate_sequence(self):
        for i in range(0, self.Difficulty):
            self.GeneratedNumbers.append(random.randint(0,10))

    def get_list_from_user(self):
        print("Enter " + str(self.Difficulty) + " numbers: ")
        for i in range(0, self.Difficulty):
            self.UserNumbers.append(int(input("")))

    def is_list_equal(self):
        X = sorted(self.UserNumbers)
        Y = sorted(self.GeneratedNumbers)
        return X == Y

    def ClearConsole(self):
        return lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    def play(self):
        self.generate_sequence()
        '''
        print(self.GeneratedNumbers)
        time.sleep(1)
        self.ClearConsole()
        
        root = tk.Tk()
        w = 280 # width for the Tk root
        h = 50  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title("Generated Numbers")
        tk.Label(root, text=str(self.GeneratedNumbers)).pack()
        root.after(1000, lambda: root.destroy())  # time in ms
        root.mainloop()
        '''
        print(str(self.GeneratedNumbers))
        time.sleep(1)
        Utils.Screen_cleaner()
        self.get_list_from_user()
        if self.is_list_equal():
            #  Win
            return (self.Difficulty * 3 + 5)
        else:  # Lost
            return 0

def main():
    game1 = MemoryGame(5)
    game1.play()

if __name__ == '__main__':
    main()
