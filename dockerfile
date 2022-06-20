FROM python:3

WORKDIR /WorldOfGames

COPY MainGame.py requirements.txt ./

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["MainGame.py"]
