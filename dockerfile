FROM python:3

COPY ./ /

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000

CMD ["MainGame.py"]
