import time
import keyboard
import mouse

LINE_TIME = 10

def press_key(key, delay=0.5):
    keyboard.press(key)
    time.sleep(delay)
    keyboard.release(key)

def activate_speed():
    press_key("&", 0.1)
    mouse.press("right")
    time.sleep(0.1)
    mouse.release("right")
    press_key("é", 0.1)

def tp():
    # press 't' then write : './warp garden' then press enter
    time.sleep(0.2)
    press_key('t')
    time.sleep(0.2)
    keyboard.write('/warp garden')
    time.sleep(0.2)
    press_key('enter')
    time.sleep(0.2)

def pattern():
    press_key('d', LINE_TIME)
    press_key('s', LINE_TIME)

def simulate_key_presses():
    # Wait for the user to press '9' to start the program
    while True:
        if keyboard.is_pressed('9'):
            break
    while True:
        tp()
        activate_speed()
        time.sleep(0.2)
        mouse.press()
        for _ in range(14):
            pattern()
            mouse.release()
            time.sleep(0.1)
            activate_speed()
            time.sleep(0.1)
            mouse.press()
        press_key('d', LINE_TIME)
        mouse.release()

# Start the program
simulate_key_presses()