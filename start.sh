cd /home/HubTVMC
source ./virtualenv/bin/activate

sudo xset dpms force off

sudo modprobe uinput

sudo ./virtualenv/bin/python3 app.py