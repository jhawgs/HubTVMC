import uinput
from Xlib import display

r = display.Display().screen().root
qp = r.query_pointer()
x = qp.win_x
y = qp.win_y

Y_CURSOR_LIMIT = (60, 1050)
X_CURSOR_LIMIT = (30, 1875)
REQUERY_INTERVAL = 6
reqint = 0

events = {
    "a": uinput.KEY_A,
    "b": uinput.KEY_B,
    "c": uinput.KEY_C,
    "d": uinput.KEY_D,
    "e": uinput.KEY_E,
    "f": uinput.KEY_F,
    "g": uinput.KEY_G,
    "h": uinput.KEY_H,
    "i": uinput.KEY_I,
    "j": uinput.KEY_J,
    "k": uinput.KEY_K,
    "l": uinput.KEY_L,
    "m": uinput.KEY_M,
    "n": uinput.KEY_N,
    "o": uinput.KEY_O,
    "p": uinput.KEY_P,
    "q": uinput.KEY_Q,
    "r": uinput.KEY_R,
    "s": uinput.KEY_S,
    "t": uinput.KEY_T,
    "u": uinput.KEY_U,
    "v": uinput.KEY_V,
    "w": uinput.KEY_W,
    "x": uinput.KEY_X,
    "y": uinput.KEY_Y,
    "z": uinput.KEY_Z,
    "__RELX__": uinput.REL_X,
    "__RELY__": uinput.REL_Y,
    0: uinput.BTN_LEFT,
    2: uinput.BTN_RIGHT,
    "Enter": uinput.KEY_ENTER,
    "Shift": uinput.KEY_RIGHTSHIFT,
    "Tab": uinput.KEY_TAB,
    "0": uinput.KEY_0,
    "1": uinput.KEY_1,
    "2": uinput.KEY_2,
    "3": uinput.KEY_3,
    "4": uinput.KEY_4,
    "5": uinput.KEY_5,
    "6": uinput.KEY_6,
    "7": uinput.KEY_7,
    "8": uinput.KEY_8,
    "9": uinput.KEY_9,
    "]": uinput.KEY_RIGHTBRACE,
    "[": uinput.KEY_LEFTBRACE,
    " ": uinput.KEY_SPACE,
    "ArrowLeft": uinput.KEY_LEFT,
    "ArrowUp": uinput.KEY_UP,
    "ArrowDown": uinput.KEY_DOWN,
    "ArrowRight": uinput.KEY_RIGHT,
    #"__EVSYN__": uinput.EV_SYN,
    #"__SYNREP__": uinput.SYN_REPORT
}

device = uinput.Device(list(events.values()))

def handle_key(event):
    global x, y, reqint
    if event["type"] in ["keydown", "keyup"]:
        if event["key"] not in events:
            print("Unknown Key: {}".format(event["key"]))
        else:
            device.emit(events[event["key"]], 1 if event["type"] == "keydown" else 0)
    elif event["type"].startswith("mouse"):
        if event["type"] == "mouseup":
            device.emit(uinput.BTN_LEFT if event["button"] == 0 else uinput.BTN_RIGHT, 0)
        elif event["type"] == "mousedown":
            device.emit(uinput.BTN_LEFT if event["button"] == 0 else uinput.BTN_RIGHT, 1)
        elif event["type"] == "mousemove":
            if reqint >= REQUERY_INTERVAL:
                qp = r.query_pointer()
                x = qp.win_x
                y = qp.win_y
                reqint = 0
            if x + event["dx"] * 1.25 > X_CURSOR_LIMIT[0] and x + event["dx"] * 1.25 < X_CURSOR_LIMIT[1]:
                device.emit(uinput.REL_X, int(event["dx"] * 1.25))
                x += int(event["dx"] * 1.25)
            if y + event["dy"] * 1.25 > Y_CURSOR_LIMIT[0] and y + event["dy"] * 1.25 < Y_CURSOR_LIMIT[1]:
                device.emit(uinput.REL_Y, int(event["dy"] * 1.25))
                y += int(event["dy"] * 1.25)
            while x < X_CURSOR_LIMIT[0]:
                x += 1
                device.emit(uinput.REL_X, 1)
            while x > X_CURSOR_LIMIT[1]:
                x -= 1
                device.emit(uinput.REL_X, -1)
            while y < Y_CURSOR_LIMIT[0]:
                y += 1
                device.emit(uinput.REL_Y, 1)
            while y > Y_CURSOR_LIMIT[1]:
                y -= 1
                device.emit(uinput.REL_Y, -1)
            reqint += 1
        print(x, y)
    #device.emit(uinput.EV_SYN, uinput.SYN_REPORT, 0)