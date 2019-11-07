import time
import datetime;
import os
import threading
import ctypes
import contextlib
import enum
import six
import threading
import unicodedata
import tkinter as tk
from pynput._util import AbstractListener
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key, Listener

#Changeables
delay = 0.250
button = Button.left
start_stop_key = Key.f6
welcome = 'Welcome to the BFG Auto Clicker!'
directions = 'Put your mouse over the start button when you are out of leads and then press the F6 key on the top of your keyboard. \n Once you get a lead press F6 again to stop clicking. \n \n While you are auto clicking your mouse is locked from movement. \n'
copyright =  '\n Created by Kyle Janulis'

#Set base var
loc = 300
ts = datetime.datetime.now()
click = 0

#Menu Functions
def okclicked():
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    print ('Ready for clicking')
    menu.destroy()

#Menu
menu = tk.Tk()
menu.title("BFG Auto Click")
lbl = tk.Label(menu, text=welcome, font=("Arial Bold", 30))
lbl.grid(column=0, row=0)
lbl2 = tk.Label(menu, text=directions)
lbl2.grid(column=0, row=1)
btn = tk.Button(menu, text="   OK   ", bg="green", fg="white", command=okclicked)
btn.grid(column=0, row=2)
lbl3 = tk.Label(menu, text=copyright, font=("Arial", 6))
lbl3.grid(column=0, row=3)

#Display the welcome msg and minimize the console window
os.system('mode con: cols=50 lines=5')
menu.mainloop()

#Actual code for functions
class ClickMouse(threading.Thread):
    def __init__(self, delay, button, loc, click):
        super(ClickMouse, self).__init__()
        self.loc = mouse.position
        self.delay = delay
        self.click = click
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.loc = mouse.position
        self.running = True
        self.click = 0
        print("Start Clicking at", ts)

    def stop_clicking(self):
        self.running = False
        print("Stop Clicking at", ts)

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                print("Auto Click #", self.click)
                self.click = (self.click + 1)
                mouse.position = (self.loc)
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button, loc, click)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()


with Listener(on_press=on_press) as listener:
    listener.join()