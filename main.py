#!/usr/bin/python3

import mh_z19
from time import sleep
from datetime import datetime, time
import json
import os
import traceback
import random
import subprocess

# ---------
# CONSTANTS
# ---------

# root directory
DIR_ROOT = "/home/user/co2_meter"

# loging settings
LOG_FILE = os.path.join(DIR_ROOT, 'meter.log')
LOG_MAX_SIZE = 128 * 1024 * 1024

# silent hours
TIME_SILENT_START = time(23, 15)
TIME_SILENT_END = time(9, 15)

# waiting in seconds
SLEEP = 60

# co2 sound trigger value
CO2_TRIGGER = 1000

# sound volume fix. 1 is standart
BEEP_VOLUME = "1.3"

# audio folder
DIR_AUDIO = os.path.join(DIR_ROOT, 'beep')

# ---------
# FUNCTIONS
# ---------

def remove_spaces_in_dir(dir_path):
    # file search
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        # is it file?
        if os.path.isfile(file_path):
            # try ' ' -> '-'
            new_filename = filename.replace(' ', '-')
            new_file_path = os.path.join(dir_path, new_filename)

            # apply
            if new_file_path != file_path:
                os.rename(file_path, new_file_path)
                print(f"Removed file name spaces: '{filename}' -> '{new_filename}'")

def pick_random_file(dir_path):
    # make files list
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

    # check files
    if files:
        # pick one
        random_file = random.choice(files)
        print(f"Random beep: {random_file}")
    else:
        print(f"No audio files in {dir_path} directory.")

    return dir_path + "/" + random_file

def trim_file(file_path, max_size):
    """Remove top lines if file size > max_size/2."""
    while os.path.getsize(file_path) > max_size/2:
        with open(file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            # remove first line
            file.seek(0)
            file.writelines(lines[1:])
            file.truncate()  # cut file to new lenght

def main():
    while True:

        # log size check
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > LOG_MAX_SIZE:
                trim_file(LOG_FILE, LOG_MAX_SIZE)

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        json_meter_data = str(mh_z19.read_all())
        json_meter_data = json_meter_data.replace("'", '"')
        dict_meter = json.loads(json_meter_data)

        line  = f"{current_time}\tCO2: {dict_meter['co2']}\ttC: {dict_meter['temperature']}\n"

        with open(LOG_FILE, 'a', encoding='utf-8') as file:
            file.write(line)

        time_now = datetime.now().time()
        if (int(dict_meter['co2']) >= CO2_TRIGGER) and (TIME_SILENT_START > time_now > TIME_SILENT_END):
            print(f"High CO2 level - {dict_meter['co2']}!")
            audio_file = pick_random_file(DIR_AUDIO)
            subprocess.run(['play', '-v', BEEP_VOLUME, '-q', audio_file])

        sleep(SLEEP)

# ---------
# RUN MAIN!
# ---------

if __name__ == "__main__":
    try:
        remove_spaces_in_dir(DIR_AUDIO)
        main()
    except:
        print(traceback.format_exc())
