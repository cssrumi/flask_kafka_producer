FROM python:3.6-alpine

ADD ./code /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "webhook.py"]
