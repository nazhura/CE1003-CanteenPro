import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, font
import datetime, calendar
from tkcalendar import DateEntry
from datetime import date
from menuInput import menuPageInput

#-------------------------------------siti nazhura's part-------------------------------------------
class otherDatesPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        image2 = Image.open('img\datev2.png')
        image1 = ImageTk.PhotoImage(image2)
        background_label = tk.Label(self, image=image1)
        background_label.image1 = image1
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Button(self, text="❮", font=("Carviar Dreams Bold", 25), fg="#FAE7D7", bg="#944332",
                  activebackground="#944332", activeforeground="#FAE7D7", border=0,
                  command=lambda: master.switch_frame('StartPage')).place(x=1, y=1)

        tk.Label(self, text="hi").pack(side="top", pady=(100, 20), padx=550)


        #-------------------------------------------------royce tan's part--------------------------------------
        def variableRetrieve():
            global dropdownHour, dropdownMinute, dayOfWeekSaved
            dropdownHour = str(variable1.get())
            dropdownMinute = str(variable2.get())
            print("Time =", dropdownHour, ":", dropdownMinute)
            dateRetrieve = str(cal.get_date())
            yearRetrieve = int(dateRetrieve[0:4])
            monthRetrieve = int(dateRetrieve[5:7])
            dayRetrieve = int(dateRetrieve[8:10])
            dayOfWeekChecker = datetime.date(yearRetrieve, monthRetrieve, dayRetrieve)
            dayOfWeekSaved = calendar.day_name[dayOfWeekChecker.weekday()]
            print(dayOfWeekSaved)
            params = [dropdownHour, dropdownMinute, dayOfWeekSaved] #siti nazhura's part
            master.switch_frame_params('menuPageInput', params) #siti nazhura's part
            return dropdownHour, dropdownMinute, dayOfWeekSaved
            # Make an exit here

        def setToNow():
            dayOfWeekChecker = date.today()
            dayOfWeekSaved = calendar.day_name[dayOfWeekChecker.weekday()]
            timeReset = str(datetime.datetime.now().time())
            cal.set_date(date.today())
            variable1.set(defaultTime[0:2])
            variable2.set(defaultTime[3:5])
            dropdownHour = int(defaultTime[0:2])
            dropdownMinute = int(defaultTime[3:5])


        #----------------------------------------------------royce tan's part-----------------------------------------------------
        HourOption = []
        MinuteOption = ["00", "05"]
        for HourLoop in range(0, 24):
            HourOption.append(HourLoop)
        for MinuteLoop in range(10, 56, 5):
            MinuteOption.append(MinuteLoop)
        variable1 = StringVar(self)
        variable2 = StringVar(self)

        # take the user's date and time
        defaultTime = str(datetime.datetime.now().time())
        variable1.set(defaultTime[0:2])
        variable2.set(defaultTime[3:5])

        #----------------------------------------------------siti nazhura's part--------------------------------------------------------
        newCanvas = Canvas(self, width=500, height=300, bg="#483c32", borderwidth=0).pack(pady=50)

        leftFrame = Frame(newCanvas, bg="#483c32")
        leftFrame.place(x=240, y=240)

        rightFrame = Frame(newCanvas, bg="#483c32")
        rightFrame.place(x=480, y=240)

        bottomFrame = Frame(newCanvas, bg="#483c32")
        bottomFrame.place(x=280, y=400)

        cFont = font.Font(family='Caviar Dreams Bold', size=12)
        mFont = font.Font(family='Caviar Dreams Bold', size=10)

        tk.Label(leftFrame, text=f"Select your \n desired date: ", font=("Caviar Dreams Bold", 20), bg="#483c32",
                 fg="#fae7d7").pack()
        cal = DateEntry(leftFrame, width=14, height=4, borderwidth=2, font=("Caviar Dreams Bold", 14), selectbackground="#944332",
                        bordercolor="#944332", background="#fae7d7", foreground="#483c32", weekendbackground="#fae7d7",
                        normalbackground="#fae7d7",othermonthwebackground="#fae7d7",othermonthbackground="#fae7d7",
                        headersbackground="#483c32", headersforeground="#fae7d7", date_pattern="d/m/yyyy")
        cal.pack(padx=10, pady=10)

        tk.Label(rightFrame, text=f"Select your \n desired time: ", font=("Caviar Dreams Bold", 20), bg="#483c32",
                 fg="#fae7d7").pack()


        #---------------------------------------------royce tan's part---------------------------------------------------------------
        hour = OptionMenu(rightFrame, variable1, *HourOption)
        hour.config(font=cFont, width=4, bg="white", activebackground="white")
        hour.pack(side=LEFT, pady=(10, 0), padx=(5, 0))

        menu = self.nametowidget(hour.menuname)
        menu.config(font=mFont)  # set the drop down menu font

        tk.Label(rightFrame, text=f":", fg="black", bg="white", font=("Caviar Dreams Bold", 14), pady=4, padx=5).pack(
            side=LEFT, pady=(10, 2))

        min = OptionMenu(rightFrame, variable2, *MinuteOption)
        min.config(font=cFont, width=4, bg="white", activebackground="white")
        min.pack(side=LEFT, pady=(10, 0))

        menu = self.nametowidget(min.menuname)
        menu.config(font=mFont)  # set the drop down menu font

        tk.Button(bottomFrame, text="Set", font=("Caviar Dreams Bold", 16), fg="#483c32", bg="#fae7d7",
                  command=variableRetrieve, width=14, border=0, activeforeground="#483c32",
                  activebackground="#fae7d7").pack(side=LEFT, padx=(0, 20))

        tk.Button(bottomFrame, text="Reset", fg="#483c32", bg="#fae7d7", font=("Caviar Dreams Bold", 16),
                  command=setToNow, width=14, border=0, activeforeground="#483c32", activebackground="#fae7d7").pack(
            side=LEFT)
