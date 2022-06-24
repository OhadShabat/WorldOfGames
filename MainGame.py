import Live
import Utils
import Score
import MainScores

# Score.clear_score()
name = input("Please insert name:")
Live.welcome(name)
Utils.Screen_cleaner()
game_score = Live.load_game()
print("1 " + str(game_score))
while (game_score != -1):
    Score.add_score(game_score)
    MainScores.app.run()
    Utils.Screen_cleaner()
    game_score = Live.load_game()
    print("2 " + str(game_score))
