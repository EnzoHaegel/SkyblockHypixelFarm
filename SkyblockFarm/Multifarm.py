import time
import keyboard
import mouse
import tkinter as tk
from threading import Thread, Event

ONE_PLOT_TIME = 24.25


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Script Controller")
        self.master.geometry("350x250")

        # Control variable for the script execution thread
        self.run_event = Event()
        self.pause_event = Event()
        self.current_key = None
        self.start_time = None
        # Time the program has been running (excluding pause time)
        self.elapsed_time = 0
        self.NB_PLOT = tk.IntVar(value=2)
        self.script_thread = None

        tk.Label(master, text="Nombre de plots:").pack(pady=10)

        self.plot_selector = tk.Spinbox(
            master, from_=1, to=5, textvariable=self.NB_PLOT)
        self.plot_selector.pack(pady=10)

        self.timer_label = tk.Label(
            master, text="Time remaining for the line: --")
        self.timer_label.pack(pady=10)

        self.elapsed_label = tk.Label(
            master, text="Elapsed time (excluding pause): --")
        self.elapsed_label.pack(pady=10)

        self.start_button = tk.Button(
            master, text="Start", command=self.start_script)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(
            master, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(
            master, text="Stop", command=self.stop_script)
        self.stop_button.pack(pady=10)

        self.master.after(500, self.check_keys)
        self.mouse_pressed = False  # To track the state of the mouse click

        # Binding the destroy event
        self.master.protocol("WM_DELETE_WINDOW", self.close_app)

    def press_key(self, key, delay):
        end_time = time.time() + delay
        elapsed_time = 0  # Track how much time has passed

        keyboard.press(key)
        self.current_key = key

        while time.time() < end_time:
            if self.pause_event.is_set():
                # Calculate how much time has already passed
                elapsed_time = time.time() - (end_time - delay)
                keyboard.release(self.current_key)
                if mouse.is_pressed():
                    mouse.release()
                while self.pause_event.is_set():
                    time.sleep(0.1)
                keyboard.press(self.current_key)
                # Adjust the end time based on elapsed time
                end_time = time.time() + (delay - elapsed_time)

            time.sleep(0.1)

        keyboard.release(key)
        self.current_key = None

    def tp(self):
        time.sleep(0.2)
        self.press_key('t', 0.5)
        time.sleep(0.2)
        keyboard.write('/warp garden')
        time.sleep(0.2)
        self.press_key('enter', 0.5)
        time.sleep(0.2)

    def check_keys(self):
        if keyboard.is_pressed('9'):
            if self.script_thread and self.script_thread.is_alive():
                self.stop_script()
                time.sleep(0.5)  # Allow some time for the script to stop
            self.start_script()
        elif keyboard.is_pressed('8'):
            self.toggle_pause()
            time.sleep(0.2) # Avoid to press it twice
        # Checking more frequently for responsiveness
        self.master.after(100, self.check_keys)

    def update_labels(self):
        while not self.run_event.is_set():
            if not self.pause_event.is_set() and self.start_time:
                elapsed = int(time.time() - self.start_time +
                              self.elapsed_time)
                mins, secs = divmod(elapsed, 60)
                time_str = f"{mins}m {secs}s"
                remaining_time = int(
                    ONE_PLOT_TIME * self.NB_PLOT.get() - (secs % int(ONE_PLOT_TIME * self.NB_PLOT.get())))
                self.elapsed_label.config(
                    text=f"Elapsed time (excluding pause): {time_str}")
                self.timer_label.config(
                    text=f"Time remaining for the line: {remaining_time}s")
            time.sleep(1)

    def close_app(self):
        self.stop_script()
        self.master.destroy()

    def simulate_key_presses(self):
        LINE_TIME = ONE_PLOT_TIME * self.NB_PLOT.get()

        while not self.run_event.is_set():
            if not self.pause_event.is_set():
                self.tp()
                mouse.press()
                self.mouse_pressed = True  # Enregistre l'état du clic de la souris
                time.sleep(0.1)
                self.press_key('q', LINE_TIME)
                self.press_key('d', LINE_TIME)
                self.press_key('q', LINE_TIME)
                self.press_key('d', LINE_TIME)
                self.press_key('q', LINE_TIME)
                mouse.release()
                self.mouse_pressed = False  # Met à jour l'état du clic de la souris
                time.sleep(0.2)

                # Waiting before next loop iteration
                wait_start = time.time()
                while time.time() - wait_start < (5 - self.NB_PLOT.get()) * ONE_PLOT_TIME * 5 and not self.pause_event.is_set():
                    time.sleep(0.5)

    def start_script(self):
        if self.script_thread is None or not self.script_thread.is_alive():
            self.run_event.clear()
            self.start_time = time.time()
            self.script_thread = Thread(target=self.simulate_key_presses)
            self.script_thread.start()

            # Start the label update thread
            label_update_thread = Thread(target=self.update_labels)
            label_update_thread.start()

    def toggle_pause(self):
        if self.pause_event.is_set():
            self.elapsed_time += time.time() - self.start_time
            self.start_time = time.time()
            self.pause_event.clear()
            if self.mouse_pressed:  # Si la souris était pressée avant la pause
                mouse.press()  # Réactive le clic de la souris
            self.pause_button.config(text="Pause")
        else:
            self.pause_event.set()
            if self.current_key:
                keyboard.release(self.current_key)
            if mouse.is_pressed():  # Si la souris est actuellement pressée
                mouse.release()  # Désactive le clic de la souris
            self.pause_button.config(text="Resume")


    def stop_script(self):
        self.run_event.set()
        self.pause_event.clear()
        if self.script_thread:
            self.script_thread.join()
        self.pause_button.config(text="Pause")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
