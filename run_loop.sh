#!/bin/bash
while true
do
  echo "Opening config.ini - customize accordingly then save and close it to continue!"
  if command -v nano &> /dev/null
  then
    nano config.ini
  else
    pico config.ini
  fi
  echo "config.ini closed - starting Easy-Wav2Lip..."
  python run.py
done
