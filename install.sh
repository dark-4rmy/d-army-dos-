#!/bin/bash

pip install -r requirements.txt --break-system-packages

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root (use sudo)."
    exit 1
else
    echo "You are running this script as root."
fi


echo ' We Are Dark army '

apt install python3
clear

echo python3 d-army.py
