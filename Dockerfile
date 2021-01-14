FROM ubuntu:20.04

MAINTAINER Lily "oaguy1@gmail.com"

RUN apt update -y && apt upgrade -y

RUN apt install python3 python3-pip -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

Entrypoint ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0"]
