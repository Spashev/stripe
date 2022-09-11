FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install base software
RUN apt-get update && apt-get install -y \
  alien \
  nginx \
  lsof \
  libaio1 \
  vim \
  wget \
  unzip

# install dependencies
RUN pip install --upgrade pip --user
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# copy project
COPY ./stripe /usr/src/app/

EXPOSE 8000