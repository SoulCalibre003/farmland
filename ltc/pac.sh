#!/bin/bash


clear
pkg install update
pkg install upgrade
apt update
apt upgrade -y
pkg install python -y
pip install --upgrade pip
pip install -r requirements.txt

echo
echo -e "\e[1n Subscribe to Termux Tricks & Tut
Kung merong katanungan mag PM sa aking FB account fb.me/jonabine"
echo
echo -e "\e[1m\e[32m Enter :\e[33m exit"
echo
