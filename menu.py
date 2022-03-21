import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime as dt
import calendar

import pickle


#-------------------------------------siti nazhura's part-------------------------------------------


# importing dictionary from pickle file
with open('monday.pickle', 'rb') as handle:
    mon = pickle.load(handle)

with open('tuesday.pickle', 'rb') as handle:
    tues = pickle.load(handle)

with open('wednesday.pickle', 'rb') as handle:
    wed = pickle.load(handle)

with open('thursday.pickle', 'rb') as handle:
    thu = pickle.load(handle)

with open('friday.pickle', 'rb') as handle:
    fri = pickle.load(handle)

with open('saturday.pickle', 'rb') as handle:
    sat = pickle.load(handle)

with open('sunday.pickle', 'rb') as handle:
    sun = pickle.load(handle)

#-------------------------------------siti nazhura's part-------------------------------------------
class menuPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        try:
            image2 = Image.open('img\menuv6.png')
            image1 = ImageTk.PhotoImage(image2)
        except tk.TclError:
            self.image1 = Label(text="Sorry, no such image in the file directory")
        else:
            background_label = tk.Label(self, image=image1)
            background_label.image1 = image1
            background_label.place(x=0, y=0, relwidth=1, relheight=1)  # using image as the window's background





        tk.Button(self, text="❮", font=("Carviar Dreams Bold", 25), fg="#FAE7D7", bg="#944332",
                            activebackground="#944332", activeforeground="#FAE7D7",border=0,command=lambda: master.switch_frame('StartPage')).place(x=1,y=1)


        tk.Label(self,text="hi").pack(side="top", pady=(20, 50), padx=550)

        def retrieve_input(textBox):
            inputValue = textBox.get("1.0", "end-1c")
            print(inputValue)


        my_date = dt.datetime.now()
        userInDay = calendar.day_name[my_date.weekday()] #get system's date, convert to day
        userInTime = my_date.hour #get system time, only the hour (24 hour based)



        #siti nazhura's part: (display different stalls and menu, dependent on the day and hour
        if userInDay == "Monday":


            if 7 <= userInTime <= 11:
                self.menuList(mon['AM'], userInDay, userInTime)

            elif 12 <= (userInTime) <= 22:
                self.menuList(mon['PM'], userInDay, userInTime)

            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Tuesday":

            if 7 <= userInTime <= 11:
                self.menuList(tues['AM'], userInDay, userInTime)

            elif 12 <= userInTime <= 22:
                self.menuList(tues['PM'],userInDay,userInTime)

            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Wednesday":


            if 7 <= userInTime <= 11:
                self.menuList(wed['AM'],userInDay,userInTime)



            elif 12 <= userInTime <= 22:
                self.menuList(wed['PM'], userInDay, userInTime)

            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Thursday":


            if 7 <= userInTime <= 11:
                self.menuList(thu['AM'], userInDay, userInTime)
            elif 12 <= userInTime <= 22:
                self.menuList(thu['PM'], userInDay, userInTime)
            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Friday":


            if 7 <= userInTime <= 11:
                self.menuList(fri['AM'], userInDay, userInTime)
            elif 12 <= userInTime <= 22:
                self.menuList(fri['PM'], userInDay, userInTime)
            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))

        elif userInDay == "Saturday":

            if 7 <= userInTime <= 11:
                self.menuList(sat['AM'],userInDay,userInTime)

            elif 12 <= userInTime <= 15:
                self.menuList(sat['PM'],userInDay,userInTime)

            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170,180))



        elif userInDay == "Sunday":
            if 7 <= userInTime <= 11:

                self.menuList(sun['AM'],userInDay,userInTime)

            elif 12 <= userInTime <= 15:

                self.menuList(sun['PM'],userInDay,userInTime)

            else:
                Label(self, text="All stalls are closed! \n Please come back tomorrow!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))



    #siti nazhura's part: (user input for waiting time
    def retrieve_input(self,textBox,shopName,day,time):
        shopWaiting = {
            "Clay Pot":0.2,
            "Beverages":0.5,
            "MunChee":0.1,
            "Salad":0.3,
            "Xin Mei Ban Mian":0.3,
            "YT Duck":0,
            "Indian":0,
            "Vinford Western":5,
            "Yong Tau Foo":0.2,
            "Xian Mei Shi":0.2
        }

        try:
            print(shopName)
            print(day)
            print(time)
            approxWait = shopWaiting[shopName]
            inputValue = int(textBox.get("1.0", "end-1c"))


            waitTimewin = Toplevel(self)
            waitTimewin.title(shopName + "'s waiting time")
            waitTimewin.geometry("440x200")
            waitTimewin.configure(background="white")
            waitTimewin.resizable(False, False)

            if day == "Saturday" or day == "Sunday": #weekends -> lesser waiting time
                print("Weekend")
                approxWait = approxWait/2
                print("end"+str(approxWait))


            if 11<=time<=14: #peak period
                print("Peak")
                approxWait = approxWait+5
                print("pk"+str(approxWait))


            print(approxWait)
            print(inputValue)
            totalWaiting = round(approxWait*inputValue, 1)

            print(totalWaiting)

            Label(waitTimewin, text=shopName,font=("Dominique", 40), pady=20,bg="white",fg="#483c32").pack()
            Label(waitTimewin, text="Number of people waiting in line: " + str(inputValue),bg="white",fg="#483c32", font=("Caviar Dreams Bold", 16)).pack()
            Label(waitTimewin, text="Approximate waiting time: " + str(totalWaiting) + " minute(s)",bg="white",fg="#483c32",font=("Caviar Dreams Bold", 16)).pack()


        except:

            messagebox.showerror("User input error", "ERROR! Only integers allowed! Please try again!")
            #error message will pop up if user enter non-integer values



    #siti nazhura's part: (function for the day and hour if statements above
    def menuList(self,list,day,time):

        k = [k for k in list.keys()]
        print(k) #stall names(dictionary version)

        def goto(i):
            newwin = Toplevel(self)
            menu_list = k[i] #stall names

            newwin.title(menu_list + " store menu")


            newwin.geometry("600x580")
            newwin.configure(background="#FAE7D7")
            newwin.resizable(False, False)

            imagebg = Image.open('img\_woodv4.png')
            imgg = ImageTk.PhotoImage(imagebg)
            background_label = tk.Label(newwin, image=imgg)
            background_label.image1 = imgg
            background_label.place(x=0, y=0, relwidth=1, relheight=1)  # using image as the window's background


            Label(newwin, text="~" + menu_list + "~", font=("Dominique", 50), fg="#FAE7D7", bg="#944332").pack(
                pady=(40, 20), ipadx=40)
            # print(menu_list)

            newCanvas = Canvas(newwin, width=500, height=340, bg="#FAE7D7")
            newCanvas.pack()

            leftFrame = Frame(newCanvas, bg="#FAE7D7")
            leftFrame.place(x=10, y=40)

            rightFrame = Frame(newCanvas, bg="#FAE7D7")
            rightFrame.place(x=400, y=40)

            calCanvas = Canvas(newwin, bg="#944332", width=500, height=50)
            calCanvas.place(x=72, y=490)

            calFrame = Frame(calCanvas, bg="#944332", width=500, height=20)
            calFrame.pack()

            g = [g for g in list[k[i]]] #get the number of items in the store from the dictionary

            for h in range(1, len(g) + 1):
                menu = str(list[k[i]][h]['Menu']) #display the menu (food) for selected store from the dictionary
                price = str(list[k[i]][h]['Price'])#display the price for selected store from the dictionary
                print(menu)

                Label(leftFrame, text=menu,
                      font=("Caviar Dreams Bold", 18), fg="#944332", bg="#FAE7D7", pady=2, anchor='w').pack(fill='both')
                Label(rightFrame, text="$" + price + "0", font=("Caviar Dreams Bold", 18), fg="#944332", bg="#FAE7D7", pady=2).pack(
                    padx=(0, 20))


            Label(calFrame, text="Enter the number \n of people queuing: ", font=("Caviar Dreams Bold", 14),padx=10, fg="#FAE7D7", bg="#944332").pack(side=LEFT)
            textBox = Text(calFrame, height=1, width=8,font=("Caviar Dreams Bold", 14),pady=4, fg="#944332", bg="#FAE7D7")
            textBox.pack(side=LEFT)
            buttonCommit = Button(calFrame, height=1, width=10, text="Calculate",
                                  command=lambda: self.retrieve_input(textBox,k[i],day,time), font=("Caviar Dreams Bold", 14),
                                  fg="#944332", bg="#FAE7D7",activebackground="#FAE7D7",activeforeground="#944332", border=0)
            buttonCommit.pack(side=RIGHT,padx=10)

        forCount = 0
        for i in range(len(k)):
            if forCount < 4:
                btn = Button(self, text=k[i], command=lambda i=i: goto(i), font=("Caviar Dreams Bold", 16),
                             fg="#944332", bg="#FAE7D7", width=15, height=1,
                             activebackgroun="#FAE7D7", activeforeground="#944332", border=0).pack(side=LEFT,
                                                                                                   padx=(38, 0),
                                                                                                   pady=(
                                                                                                       160, 250))
                forCount = forCount + 1
            else:
                btn = Button(self, text=k[i], command=lambda i=i: goto(i), font=("Caviar Dreams Bold", 16),
                             fg="#944332", bg="#FAE7D7", width=20, height=1,
                             activebackgroun="#FAE7D7", activeforeground="#944332", border=0).place(x=360,
                                                                                                    y=350)
