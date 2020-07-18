FROM python:3
RUN apt-get update
ENV PYTHONUNBUFFERED = 1 
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r Pipfile

# RUN sudo apt install python3 mysql-server


