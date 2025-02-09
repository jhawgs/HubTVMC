import tkinter as tk
import subprocess
import time

# === Create the Banner Window ===
root = tk.Tk()
root.overrideredirect(True)  # Removes window decorations (no close, minimize, etc.)
root.attributes('-topmost', True)  # Always on top
root.attributes('-alpha', 0.85)    # Slight transparency

# === Banner Size & Position ===
screen_width = root.winfo_screenwidth()
banner_height = 50  # Banner height in pixels

root.geometry(f"{screen_width}x{banner_height}+0+0")  # Full width, top of the screen

# === Banner Content ===
label = tk.Label(root, text="🚀 SYSTEM BANNER - Raspberry Pi", font=("Arial", 18, "bold"),
                 bg="black", fg="white", padx=20, pady=10)
label.pack(fill=tk.BOTH, expand=True)

root.update_idletasks()

"""
# === Make the Window Non-Interactive (Click-Through) ===
def make_click_through():
    # Get the window ID using wmctrl
    win_id = subprocess.check_output(["wmctrl", "-lp"]).decode()
    pid = str(root.winfo_id())

    # Find the window ID that matches our Tkinter window
    for line in win_id.splitlines():
        if pid in line:
            window_id = line.split()[0]
            break
    else:
        print("Window ID not found.")
        return

    # Set the window to be click-through using xprop
    subprocess.run(["xprop", "-id", window_id, "-f", "_NET_WM_WINDOW_TYPE", "32a",
                    "-set", "_NET_WM_WINDOW_TYPE", "_NET_WM_WINDOW_TYPE_DOCK"])

    # Disable input events (makes it non-interactive)
    subprocess.run(["xprop", "-id", window_id, "-f", "_NET_WM_STATE", "32a",
                    "-set", "_NET_WM_STATE", "_NET_WM_STATE_ABOVE, _NET_WM_STATE_SKIP_TASKBAR"])

# Wait a moment for the window to initialize, then apply properties
root.after(500, make_click_through)
"""

# === Run the Banner ===
root.mainloop()
