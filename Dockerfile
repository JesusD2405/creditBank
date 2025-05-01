FROM python:3.13

ENV PYTHONUNBUFFERED 1

RUN apt-get update  && \
    apt-get -y install python3-pip && \
    apt-get install -y bash apt-utils netcat-traditional

WORKDIR /appdata/wwwroot

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /appdata/wwwroot/