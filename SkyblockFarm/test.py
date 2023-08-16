import keyboard
import time

def press_key(key, delay=0.05):
    keyboard.press(key)
    time.sleep(delay)
    keyboard.release(key)

while True:
        if keyboard.is_pressed('9'):
            break
press_key('s')