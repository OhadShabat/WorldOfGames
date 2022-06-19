FROM python:3

WORKDIR /WorldOfGames

COPY MainScores.py Score.py Utils.py Scores.txt requirements.txt ./

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["MainScores.py"]
