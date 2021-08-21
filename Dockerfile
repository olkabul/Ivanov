FROM python:3.8-alpine
RUN apk update
RUN apk add bash
RUN apk add git
RUN apk add python3-dev
RUN ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /dire
RUN git clone https://github.com/olkabul/Ivanov.git