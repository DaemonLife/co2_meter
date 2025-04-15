# co2_meter

## What is it?
This is for air analysis. My program use mh_z19 library and reads carbon dioxide levels and plays sound signals at a certain value. Read constants in code.

## For which device (100% works)
- Raspberry Pi 5 (Debian)
- Z19B

## How to run code
If you don't need beep sounds you need remove or comment audio function in code. Next go to step 3.
1. Make it beep! Create beep directory: ``mkdir beep``
2. Add audio file/files to beep directory.
3. Running: ``sudo python main.py``

## Tips
1. [Read this, install mh_z19](https://github.com/UedaTakeyuki/mh-z19)
2. Create a systemd service
