@echo off
:run_loop
echo opening config.ini - customize accordingly then save and close it to continue!
start /wait notepad.exe config.ini
echo config.ini closed - starting Easy-Wav2Lip...
python run.py
goto run_loop
