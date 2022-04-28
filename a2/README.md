# Assignment 2

Derek Yadgaroff, Data Engineering 2, Uppsala University

derek_de2_lab2


=====

# Notes

, 130.238.28.102



===========
dev server
ssh -i /home/ubuntu/cluster-keys/cluster-key appuser@192.168.2.17

===========
prod server
ssh -i /home/ubuntu/cluster-keys/cluster-key appuser@130.238.28.129


======
#!/bin/bash
while read oldrev newrev ref
do
    if [[ $ref =~ .*/master$ ]];
    then
        echo "Master ref received.  Deploying master branch to production..."
        sudo git --work-tree=/model_serving/ci_cd/production_server --git-dir=/home/appuser/my_project checkout -f
    else
        echo "Ref $ref successfully received.  Doing nothing: only the master branch may be deployed on this server."
    fi
done


======

git remote add production appuser@130.238.28.129:/home/appuser/my_project