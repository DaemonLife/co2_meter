# co2_meter
## What is it?
This is for air analysis. My program use mh_z19 library and reads carbon dioxide levels and plays sound signals at a certain value. Read constants in code.

## For which device (100% works)
- Raspberry Pi 5 (Debian)
- Z19B

## How to run code
### Preparation
1. Make it beep! Create beep directory: ``mkdir beep``
2. Add audio file/files to beep directory.
3. Create python virtual environment: ``python -m venv env``
4. Open python virtual environment: ``source env/bin/activate``
5. And install mh_z19 library: ``pip3 install mh_z19 --upgrade``
6. Grant permission to run the file: `chmod +x start_meter.sh`

### Using
1. Finally run meter: ``bash start_meter.sh``

## Tips
1. [Read about mh-z19](https://github.com/UedaTakeyuki/mh-z19)
2. Create a systemd service for program
