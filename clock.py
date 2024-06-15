import time
from time import strftime
from tkinter import Tk, Label,Frame
import threading

class Clock:
    def __init__(self):
        self.app = Tk()
        self.frame = Frame(self.app)
        self.time = strftime("%H %M %S")
        self.label = Label(self.frame,text=self.time)
        self.font = ("Comic Sans MS", 20, "bold")
        self.label.configure(background="red", foreground="white",width=300,height=100,font=self.font)
        self.label.pack()
        self.frame.pack()
        self.app.geometry("500x100")


    def time_change(self):
        while True:
            time.sleep(1)
            self.label.configure(text=strftime("%H %M %S"))

    def start(self):
        clock_thread = threading.Thread(target=self.time_change)
        clock_thread.start()
        self.app.mainloop()

clock = Clock()
clock.start()










