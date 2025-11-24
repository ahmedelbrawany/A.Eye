#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back 

cd /home/pi/Desktop/Organized/Main
PYTHONPATH=/home/pi/.local/lib/python3.7/site-packages/
HOME=/home/pi
python3 Main.py
