        
import time
import threading

import tkinter as tk
from tkinter import Canvas
from pynput.mouse import Button, Controller
import keybo
#----Created by Brandt_dzeri----

class AutoClicker:
    def __init__(self, delay=0.02, button=Button.left):
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.mouse = Controller()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def click(self):
        self.mouse.click(self.button)

    def run(self):
        while self.program_running:
            while self.running:
                self.click()
                time.sleep(self.delay)
            time.sleep(0.1)

def start_click():
    auto_clicker.start_clicking()

def stop_click():
    auto_clicker.stop_clicking()

def exit_program():
    auto_clicker.program_running = False
    auto_clicker.stop_clicking()
    root.destroy()

def create_rounded_button(canvas, x, y, radius, color, text, command):
    button = tk.Button(canvas, text=text, command=command, bg=color, fg="white", borderwidth=0, highlightthickness=0)
    button.config(font=("Helvetica", 12, "bold"))

    # Create rounded rectangle on canvas
    canvas.create_arc(x, y, x + radius, y + radius, start=90, extent=90, fill=color, outline=color)
    canvas.create_arc(x + 50 - radius, y, x + 50, y + radius, start=0, extent=90, fill=color, outline=color)
    canvas.create_arc(x, y + 20 - radius, x + radius, y + 20, start=180, extent=90, fill=color, outline=color)
    canvas.create_arc(x + 50 - radius, y + 20 - radius, x + 50, y + 20, start=270, extent=90, fill=color, outline=color)
    canvas.create_rectangle(x + radius / 2, y, x + 50 - radius / 2, y + 20, fill=color, outline=color)
    canvas.create_rectangle(x, y + radius / 2, x + 50, y + 20 - radius / 2, fill=color, outline=color)

    # Place button on top of the canvas' rounded rectangle
    button_window = canvas.create_window(x + 25, y + 10, window=button)
    return button

if __name__ == "__main__":
    auto_clicker = AutoClicker(delay=0.02)  # Set the delay to 0.02 seconds for 50 clicks per second

    root = tk.Tk()
    root.title("AutoClicker")
    root.geometry("200x200")

    canvas = tk.Canvas(root, width=200, height=200, bg="white")
    canvas.pack()

    start_button = create_rounded_button(canvas, 50, 30, 10, "green", "Start (S)", start_click)
    stop_button = create_rounded_button(canvas, 50, 80, 10, "red", "Stop (E)", stop_click)
    exit_button = create_rounded_button(canvas, 50, 130, 10, "purple", "Exit (F)", exit_program)

    click_thread = threading.Thread(target=auto_clicker.run, daemon=True)

    click_thread.start()

    def check_hotkeys():
        while True:
            if keyboard.is_pressed('s'):
                start_click()
            if keyboard.is_pressed('e'):
                stop_click()
            if keyboard.is_pressed('f'):
                exit_program()
            time.sleep(0.1)

    hotkey_thread = threading.Thread(target=check_hotkeys, daemon=True)
    hotkey_thread.start()

    root.mainloop()
