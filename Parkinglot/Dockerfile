FROM python:3
RUN apt-get update
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SERCRET_KEY='_w@(2%qahsb4*(r7$jw3^yba9zqqm*2y9b^#7&yzn-lmm9&%x0'
ENV JWT_SECRET_KEY='secret'
ENV HOST='web:8000'
ENV LOCALHOST='web'
ENV REDIS_HOST='127.0.0.1'
ENV PORT='8000'
ENV REDIS_PORT=6379
ENV DATABASE_NAME="parkinglot"
ENV DATABASE_USER="root"
ENV DATABASE_PASSWORD="1234"
ENV DATABASE_PORT="3306"
RUN pip install pipenv mysqlclient
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip3.8 install -r ParkingLot/requirements.txt
RUN apt install -y rabbitmq-server
RUN apt install -y redis-server
RUN service rabbitmq-server start
RUN service redis-server start

