FROM python:3.8-slim

RUN mkdir -p /usr/src/face_definition

WORKDIR /usr/src/face_definition

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN apt-get install -y build-essential cmake sqlite3 libsqlite3-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x entrypoint.sh

ENTRYPOINT ["/usr/src/face_definition/entrypoint.sh"]

