FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y git

RUN apt-get install -y vim

RUN apt-get install -y python3.5

RUN apt-get install -y python3-pip

# Install cryptography dependencies:
# Dependecies for Ubuntu found here:
# https://cryptography.io/en/latest/installation/
RUN apt-get install -y libffi-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y build-essential
RUN apt-get install -y python3-dev


# Install python SSH package.
RUN pip3 install paramiko