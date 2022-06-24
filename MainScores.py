from flask import Flask, render_template
import Score
import os

app = Flask(__name__)
 
@app.route('/')

def score_server():
    score = Score.get_score()
    print("score : " + str(score))
    f = open("templates/result.html", "w")
    lines = ["<!DOCTYPE html>\n", "<html lang='en'>\n", "<head>\n", "<meta charset='UTF-8'>\n",
             "<title>Scores game</title>\n", "</head>\n", "<body>\n"]
    if (score == -1):
        lines.append("<h1><div id='score' style='color:red'>Failed to read score !!!</div> </h1>\n")
    else:
        lines.append("<h1>The score is <div id='score'>" + str(score) + "</div></h1>\n")

    lines.append("</body>\n")
    lines.append("</html>")

    f.writelines(lines)
    f.close()

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

