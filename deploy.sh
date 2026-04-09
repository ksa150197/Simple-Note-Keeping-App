#!/bin/bash

cd /home/ec2-user/project2/Simple-Note-Keeping-App #add your ec2 full working directopry path

git pull origin master

pkill -f Final_app.py

nohup python3 Final_app.py > Final_app.log 2>&1 &