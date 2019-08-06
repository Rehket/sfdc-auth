FROM python:3.7.4-alpine3.9

RUN apk update && apk upgrade && apk add alpine-sdk python3-dev libffi-dev libressl-dev
RUN python -m pip install -U pip
WORKDIR /app
COPY . /app
RUN python -m pip install -r dev_req.txt
RUN python -m pip install -e .
RUN pytest --cov=SFJWT tests/
