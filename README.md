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
~~~
~~~
sudo echo -e "[Unit]\nDescription=Start Co2 meter\nAfter=multi-user.target\n\n[Service]\nType=simple\nExecStart=/usr/bin/bash /home/user/co2_meter/start_meter.sh\nRestart=always\n\n[Install]\nWantedBy=multi-user.target" > /lib/systemd/system/co2meter.service
~~~
~~~
sudo systemctl daemon-reload && sudo systemctl enable co2meter && sudo systemctl start co2meter && sudo systemctl status co2meter
~~~
3. Using `screen` program for run my script:
~~~
# Run
screen -S co2 # create and enter to screen session with name "co2".
bash ./start_meter.sh & # run my script as job background (symbol "&" do it).
jobs # to see all jobs status, it must be running.

# Optional. Some tips for jobs:
fg [JOB_ID] # if you want to look your job as foreground, after all use ^Z to exit back (it make stop status for your job also!). And if you want you can totally kill job with ^C.
bg [JOB_ID] # since the job has stopped run jos as background again.
# You can kill job with "kill [JOB_ID]" command if you need it.

# Save all
screen -d # detach session. Be careful "exit" command is kill you session.
screen -ls # list of all detached sessions.
screen -r co2 # open session "co2".
~~~
