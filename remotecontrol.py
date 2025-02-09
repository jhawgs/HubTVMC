import uinput

events = (
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
)

with uinput.Device(events) as device:
    def handle_key(event):
        pass

   # for i in range(20):
   #     # syn=False to emit an "atomic" (5, 5) event.
   #     device.emit(uinput.ABS_X, 5, syn=False)
   #     device.emit(uinput.ABS_Y, 5)
   # device.emit_click(uinput.BTN_JOYSTICK)