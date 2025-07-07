import time
import keyboard
import mouse

NB_PLOT = 3
ONE_PLOT_TIME = 11
LINE_TIME = ONE_PLOT_TIME * NB_PLOT


def press_key(key, delay=0.5):
    keyboard.press(key)
    time.sleep(delay)
    keyboard.release(key)


def press_keys_simultaneously(keys, delay):
    for k in keys:
        keyboard.press(k)
    time.sleep(delay)
    for k in keys:
        keyboard.release(k)


def tp():
    time.sleep(0.2)
    press_key('t')
    time.sleep(0.2)
    keyboard.write('/warp garden')
    time.sleep(0.2)
    press_key('enter')
    time.sleep(0.2)


def simulate_key_presses():
    while True:
        if keyboard.is_pressed('9') or keyboard.is_pressed('1'):
            break
    while True:
        tp()
        mouse.press()
        time.sleep(0.1)
        press_key('q', LINE_TIME)
        time.sleep(0.1)
        press_keys_simultaneously(['z', 'd'], LINE_TIME)
        time.sleep(0.1)
        press_key('q', LINE_TIME)
        time.sleep(0.1)
        press_keys_simultaneously(['z', 'd'], LINE_TIME)
        mouse.release()
        time.sleep(0.2)
        # time.sleep((4 - NB_PLOT) * ONE_PLOT_TIME * 5)


simulate_key_presses()
