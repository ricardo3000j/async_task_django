FROM python:3

#Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED 1

#Set env variables for working dir
ENV APP_PROJ=/djangoapp

# create Django directory inside docker container & install django
COPY . $APP_PROJ

# create limited user and assign ownership to working directory
RUN useradd polls && chown polls:polls -R $APP_PROJ

# change to working directory
WORKDIR $APP_PROJ

# install dependencies
RUN pip install -r requirements.txt
COPY compose/django/start.sh /start.sh

# set permission for our bash file
RUN chmod +x /start.sh && chown polls:polls /start.sh

USER polls
