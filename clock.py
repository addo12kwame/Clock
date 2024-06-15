import time
import tkinter
from time import strftime

from tkinter import *
from tkinter.ttk import *
import threading


class Clock:
    def __init__(self):
        self.app = Tk()
        self.app.resizable(False, False)
        self.frame = Frame(self.app,width=500,height=200)
        self.frame["relief"] = "groove"

        # self.app.protocol("WM_DELETE_WINDOW", lambda: self.app.quit())
        self.time = strftime("%H %M %S")
        self.time_label = Label(self.frame, text=self.time)
        self.font = ("Comic Sans MS", 20, "bold")
        self.time_var = StringVar()
        self.date_var = StringVar()
        self.time_label.configure(background="red", foreground="white", font=self.font, textvariable=self.time_var)
        self.date_label = Label(self.frame,background="red", foreground="white", font=self.font,textvariable=self.date_var)
        self.time_label.grid(row=0, column=0, columnspan=7,sticky = "EW")
        self.date_label.grid(row=3, column=0, columnspan=7)
        self.frame.grid(row=0, column=0)
        self.clock_thread = None
        self.kill_thread = False

    def time_change(self):

        while True:
            try:
                time.sleep(1)
                self.time_var.set("Time : "+ strftime("%H %M %S"))
                self.date_var.set("Date : "+ strftime("%m %d %Y"))
            except RuntimeError:
                break

    def start(self):
        self.clock_thread = threading.Thread(target=self.time_change)
        self.clock_thread.start()

        self.app.mainloop()

    def quit(self):
        if self.clock_thread:
            self.kill_thread = True
        self.app.quit()


if __name__ == '__main__':
    clock = Clock()
    clock.start()










