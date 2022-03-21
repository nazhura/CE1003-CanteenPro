import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import datetime as dt



#-------------------------------------------siti nazhura's part==============================================


#landing page of the app
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        try:
            image2 = Image.open('img\coffee-1964159_1920_edited.png')
            image1 = ImageTk.PhotoImage(image2)
        except tk.TclError:
            self.image1 = Label(text="Sorry, no such image in the file directory")
        else:
            background_label = tk.Label(self, image=image1)
            background_label.image1 = image1
            background_label.place(x=0, y=0, relwidth=1, relheight=1)




        currentTime = dt.datetime.now()
        currentTime.hour


        tk.Label(self, text="Welcome to CanteenPro", fg="#FAE7D7", bg="#5e462b", font=("Hey August", 50), pady=6, padx=500, borderwidth=1,
                relief="solid").pack(pady=(56,398)) #header


        tk.Label(self, text=f"{dt.datetime.now():%a,\n%d\n%b\n%y}", fg="#050505", bg="#A59787",
                            font=("Kiona Regular", 18), pady=5, padx=(5)).place(x=0,y=200) #display day and date

        tk.Label(self, text=f"{currentTime.strftime('%I')}\n{currentTime.strftime('%M')}\n{currentTime.strftime('%p')}", fg="#050505", bg="#A59787",
                            font=("Kiona Regular", 20),pady=18,padx=6).place(x=885,y=200) #display time


        tk.Button(self, text="View today's \n stores",
                  command=lambda: master.switch_frame('menuPage'), fg="#5e462b", bg="#FAE7D7", activebackgroun="#FAE7D7", activeforeground="#5e462b",
                            font=("Caviar Dreams Bold", 16), pady=5, padx=30, borderwidth=0).place(x=250,y=210)
        tk.Button(self, text="View stores by \n other dates",
                  command=lambda: master.switch_frame('otherDatesPage'), fg="#5e462b", bg="#FAE7D7", activebackgroun="#FAE7D7", activeforeground="#5e462b",
                            font=("Caviar Dreams Bold", 16), pady=5, padx=20, borderwidth=0).place(x=500,y=210)

        tk.Button(self, text="View store information",
                  command=lambda: master.switch_frame('operatingHrs'), fg="#5e462b", bg="#FAE7D7", activebackgroun="#FAE7D7", activeforeground="#5e462b",
                  font=("Caviar Dreams Bold", 16), width=38, height=1, borderwidth=0).place(x=250, y=300)


