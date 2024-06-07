#!bin/bash

cd /var/lib/jenkins/workspace/Midtermjob

nohup python3 serve.py > server.log 2>&1 &
