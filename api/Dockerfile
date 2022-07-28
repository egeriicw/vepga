# This is a simple Dockerfile to use while developing
# It's not suitable for production
#
# It allows you to run both flask and celery if you enabled it
# for flask: docker run --env-file=.flaskenv image flask run
# for celery: docker run --env-file=.flaskenv image celery worker -A myapi.celery_app:app
#
# note that celery will require a running broker and result backend
# FROM python:3.9
# ENV PYTHONUNBUFFERED 1


# RUN mkdir /app
# WORKDIR /app

# COPY requirements.txt setup.py tox.ini ./
# RUN pip install -U pip
# RUN pip install -r requirements.txt
# RUN pip install -e .

# COPY vepga-api vepga-api/
# COPY migrations migrations/

# EXPOSE 5000




# Base Image
FROM python:3.9.1-slim

# Install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD python manage.py run -h 0.0.0.0