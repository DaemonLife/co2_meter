# co2_meter
## What is it?
This is for air analysis. My program use mh_z19 library and reads carbon dioxide levels and plays sound signals at a certain value. Read constants in code.

## For which device (100% works)
- Raspberry Pi 5 (Debian)
- Z19B

## How to run code
### Preparation
1. Create python virtual environment: ``python -m venv env``
2. Open python virtual environment: ``source env/bin/activate``
3. And install mh_z19 library: ``pip3 install mh_z19 --upgrade``
4. Grant permission to run the file: `chmod +x start_meter.sh`

### Using
1. Finally run meter: ``bash start_meter.sh``

## Tips
1. [Read about mh-z19](https://github.com/UedaTakeyuki/mh-z19)
2. ~~Create a systemd service for program (use your path in ExecStart!):~~
~~~
sudo touch /lib/systemd/system/co2meter.service

sudo echo -e "[Unit]\nDescription=Start Co2 meter\nAfter=multi-user.target\n\n[Service]\nType=simple\nExecStart=/usr/bin/bash /home/user/co2_meter/start_meter.sh\nRestart=always\n\n[Install]\nWantedBy=multi-user.target" > /lib/systemd/system/co2meter.service

sudo systemctl daemon-reload && sudo systemctl enable co2meter && sudo systemctl start co2meter && sudo systemctl status co2meter
~~~
3. Using `screen` program for run my script:
~~~
screen -S co2 # create and enter to screen session with name "co2"
bash ./start_meter.sh & # run my script as job background
jobs # to see running background jobs, it must be running 
fg [JOB_ID] # open job as foreground
# Use ^Z to stop job and close it. Now it has stopped status
bg [JOB_ID] # run job as background again
screen -d # detach session
screen -ls # list of all detached sessions
screen -r co2 # open session "co2"
~~~
