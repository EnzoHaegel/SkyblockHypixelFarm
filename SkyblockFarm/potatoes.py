import time
import keyboard
import mouse

NB_PLOT = 4                     # Nombre de plot collé
ONE_PLOT_TIME = 24.25
LINE_TIME = ONE_PLOT_TIME * NB_PLOT


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


def simulate_key_presses():
    # Wait for the user to press '9' to start the program
    while True:
        if keyboard.is_pressed('9') or keyboard.is_pressed('1'):
            break

    while True:
        tp()
        mouse.press()
        time.sleep(0.1)
        press_key('q', LINE_TIME)
        press_key('d', LINE_TIME)
        press_key('q', LINE_TIME)
        press_key('d', LINE_TIME)
        press_key('q', LINE_TIME)
        mouse.release()
        time.sleep(0.2)

        # Temps d'attente de repousse
        time.sleep((4 - NB_PLOT) * ONE_PLOT_TIME * 5)


# Start the program
simulate_key_presses()
