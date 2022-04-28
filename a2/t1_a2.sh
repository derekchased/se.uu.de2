#!/bin/bash

# a) Copy this file into ~ wget https://raw.githubusercontent.com/derekchased/se.uu.de1.project/master/startup.sh
# b) Change permissions of this file chmod u+x startup.sh
# c) Run this script ./startup.sh

# Update VM

sudo apt update;

sudo apt -y upgrade;


# Add Openstack

sudo apt install python3-openstackclient -y;

sudo apt install python3-novaclient -y;

sudo apt install python3-keystoneclient -y;


# Add Ansible

sudo apt update;

sudo apt upgrade -y;

sudo apt-add-repository ppa:ansible/ansible;

sudo apt update;

sudo apt install ansible -y;


####

