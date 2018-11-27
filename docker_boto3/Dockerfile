FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y python3.5 \
                       python3-pip
RUN apt-get install -y git

RUN pip3 install awscli

RUN pip3 install boto3
