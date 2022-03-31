#!/bin/bash

# a) Copy this file into ~ wget https://raw.githubusercontent.com/derekchased/se.uu.de1.project/master/startup.sh
# b) Change permissions of this file chmod u+x startup.sh
# c) Run this script ./startup.sh

# 1. Update VM

sudo apt update;

sudo apt -y upgrade;

 # 2. Install Docker

sudo apt install apt-transport-https ca-certificates curl software-properties-common -y;

curl -fsSL https://download.docker.com/linux/ubuntu/gpg |sudo apt-key add -;

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable";

sudo apt-get update;

sudo apt install docker-ce -y;

sudo apt install docker-compose -y;

# 3. Config docker launch on reboot

sudo systemctl enable docker.service;

sudo systemctl enable containerd.service;

# ===== Lab Instructions Start Here

# 1. Switch to sudo in shell mode

sudo -s

# 2. Install Java

apt install default-jre;
apt install default-jdk;

# 2. Download pulsar, Unzip it

wget https://archive.apache.org/dist/pulsar/pulsar-2.7.0/apache-pulsar-2.7.0-bin.tar.gz;

tar xvfz apache-pulsar-2.7.0-bin.tar.gz;

cd apache-pulsar-2.7.0;

# 3. Run tmux window

tmux new -s pulsar;

# 4. Start local cluster

# bin/pulsar standalone;

# Stop
# Cntrl c

# 5. Start pulsar with docker 

docker run -it -p 6650:6650 -p 8080:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:2.7.0 bin/pulsar standalone;

# Stop
# Cntrl c


# ====  Task 2 ==============

# 1. Install pip
sudo apt install python3-pip -y;

# 2. Setup python client
pip install pulsar-client==2.7.1;



