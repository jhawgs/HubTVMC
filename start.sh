cd /home/HubTVMC
source ./virtualenv/bin/activate

sudo modprobe uinput

sudo ./virtualenv/bin/python3 banner.py & sudo ./virtualenv/bin/python3 app.py