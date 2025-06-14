# get base image
FROM ubuntu:latest

# set environment variables
ENV user=ubuntu
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
# set python version
ARG PYTHON_VERSION="3.12"
ENV PYTHON_VERSION=${PYTHON_VERSION}

# install required software and programmes for development environment
RUN apt-get update 
RUN apt-get install -y apt-utils vim curl wget unzip tree htop

# set up home environment
RUN mkdir -p /home/${user} && chown -R ${user}: /home/${user}

# copy littlelemon repo
COPY . /home/ubuntu/LittleLemon

# add deadsnakes ppa
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
# install required python packages
RUN apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv 
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN /opt/venv/bin/python3 -m pip install -v -r /home/ubuntu/LittleLemon/requirements.txt

# set working directory for django app
WORKDIR /home/${user}/LittleLemon/littlelemon
# make migrations and migrate data from csv files
RUN /opt/venv/bin/python3 manage.py makemigrations restaurant
RUN /opt/venv/bin/python3 manage.py migrate
RUN /opt/venv/bin/python3 manage.py runscript restaurant.import_data
# run django app tests
RUN /opt/venv/bin/python3 manage.py test

EXPOSE 8000
CMD  ["/opt/venv/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]