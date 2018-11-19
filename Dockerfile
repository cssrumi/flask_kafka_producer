FROM python:3.6-alpine

RUN mkdir /code
ADD ./code/ /code/
WORKDIR /code

RUN ls
RUN pip install -r requirements.txt

CMD ["python", "webhook.py"]
