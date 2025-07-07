import time
import keyboard
import mouse
import tkinter as tk
from threading import Thread, Event

print("✅ Modules chargés avec succès !")

# Test Tkinter : fenêtre qui se ferme après 2 secondes
root = tk.Tk()
root.title("Test Tkinter")
tk.Label(root, text="Tkinter fonctionne !").pack(padx=20, pady=20)
def fermer():
    time.sleep(2)
    root.quit()
Thread(target=fermer, daemon=True).start()
root.mainloop()
