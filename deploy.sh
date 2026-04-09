#!/bin/bash

cd C:\Users\Shubham Anand\Desktop\VS code files and folders\Poject 2

git pull origin master

pkill -f Final_app.py

nohup python3 Final_app.py > Final_app.log 2>&1 &