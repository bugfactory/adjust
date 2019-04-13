FROM python:3

LABEL name=metrics-search

ADD . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
