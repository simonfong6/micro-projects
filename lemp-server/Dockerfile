FROM ubuntu:16.04
# Instructions from https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-16-04

RUN apt-get update -y
RUN apt-get upgrade -y

# Install git for development
RUN apt-get install -y git

# Install vim for debugging
RUN apt-get install -y vim

# Step 1: Install the Nginx Web Server
RUN apt-get install -y nginx
RUN service nginx restart

#Step 2: Install MySQL to Manage Site Data
RUN apt-get install -y mysql-server

# Step 3: Install PHP for Processing
RUN apt-get install -y php-fpm php-mysql
