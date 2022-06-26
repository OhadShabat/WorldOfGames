from flask import Flask, render_template
import Score
import os

app = Flask(__name__)

@app.route('/')
def score_server():
    score = Score.get_score()
    print("score : " + str(score))

    if (score == -1):
        return render_template('error.html')
    else:
        return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)

