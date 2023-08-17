import time
import keyboard
import mouse

LINE_TIME = 29.5 / 2
WALK_TIME = 1.3

def press_key(key, delay=0.5):
    keyboard.press(key)
    time.sleep(delay)
    keyboard.release(key)

def tp():
    # press 't' then write : './warp garden' then press enter
    time.sleep(0.2)
    press_key('t')
    time.sleep(0.2)
    keyboard.write('/warp garden')
    time.sleep(0.2)
    press_key('enter')
    time.sleep(0.2)

def leftstart():
    time.sleep(0.2)
    mouse.press()
    time.sleep(0.1)
    press_key('d', LINE_TIME)
    press_key('q', LINE_TIME)
    press_key('d', LINE_TIME)
    mouse.release()
    time.sleep(0.2)
    press_key('z', WALK_TIME)
    time.sleep(0.2)

def rightstart():
    time.sleep(0.2)
    mouse.press()
    time.sleep(0.1)
    press_key('q', LINE_TIME)
    press_key('d', LINE_TIME)
    press_key('q', LINE_TIME)
    mouse.release()
    time.sleep(0.2)
    press_key('z', WALK_TIME)
    time.sleep(0.2)

def simulate_key_presses():
    # Wait for the user to press '9' to start the program
    while True:
        if keyboard.is_pressed('9'):
            break
    while True:
        tp()
        leftstart()
        rightstart()
        leftstart()
        rightstart()
        leftstart()
        # rightstart()
        # leftstart()

# Start the program
simulate_key_presses()
