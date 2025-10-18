# get base image
FROM python:3.12

# set environment variables
ENV user=user
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# install required software and programmes for development environment
RUN apt-get update
RUN apt-get install -y apt-utils vim curl wget unzip tree htop

# set up home environment
RUN mkdir -p /home/${user} && chown -R ${user}: /home/${user}

# copy little lemon repo
COPY . /home/${user}/LittleLemonDjango

# install required python packages
RUN python -m pip install -v -r /home/${user}/LittleLemon/requirements.txt

# set working directory for django app
WORKDIR /home/${user}/LittleLemonDjango/littlelemon
# make migrations and migrate data from csv files
RUN python manage.py makemigrations restaurant
RUN python manage.py migrate
RUN python manage.py runscript restaurant.import_data
# run django app tests
RUN python manage.py test

EXPOSE 8000
CMD  ["python", "manage.py", "runserver", "0.0.0.0:8000"]