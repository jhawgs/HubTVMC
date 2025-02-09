from time import sleep
import uinput

device = uinput.Device([uinput.KEY_FN, uinput.KEY_F11])

sleep(2)

device.emit(uinput.KEY_FN, 1)
sleep(.01)
device.emit(uinput.KEY_F11, 1)
sleep(.01)
device.emit(uinput.KEY_FN, 0)
device.emit(uinput.KEY_F11, 0)