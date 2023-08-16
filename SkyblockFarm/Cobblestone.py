import time
import keyboard
import mouse

def simulate_key_presses():
    # Wait for the user to press '9' to start the program
    activate = False
    while True:
        if keyboard.is_pressed('9'):
            activate = not activate
            if activate:
                mouse.press()
            else:
                mouse.release()
            time.sleep(0.5)
        if keyboard.is_pressed('0'):
            break

# Start the program
simulate_key_presses()