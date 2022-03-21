import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import datetime as dt
import calendar
import pickle
from operatinghoursPage import operatingHrs
from date import otherDatesPage
from mainMenu import StartPage
from menu import menuPage
from menuInput import menuPageInput

#--------------------------siti nazhura's part: (creating the main class for the app)---------------------------
class CanteenProApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame('StartPage')
        self.title("CanteenPro")
        self.geometry("940x580")
        self.configure(background='white')

        #double check with the user if he really wants to quit the application
        def closeWindowPopup():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.destroy()


        Button(self, text="Close window", font="Montserrat 10", fg="#FAE7D7", bg="#944332", activebackground="#944332",
               activeforeground="#FAE7D7",
               command=closeWindowPopup, pady=5, padx=30, borderwidth=0,
               relief="solid").pack(fill=BOTH, side=BOTTOM)

    def switch_frame(self, frame_class_name):
        # Destroys current frame and replaces it with a new one
        frame_class = eval(frame_class_name)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def switch_frame_params(self, frame_class_name, params):
        # Destroys current frame and replaces it with a new one
        print(params)
        frame_class = eval(frame_class_name)
        new_frame = frame_class(self,params)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":

    def closeWindowPopup():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            app.destroy() #this will prompt the user if he really wants to quit the app


    app = CanteenProApp()
    app.protocol("WM_DELETE_WINDOW", closeWindowPopup)
    app.resizable(False, False)  # don't let the user resize the window
    app.mainloop()
