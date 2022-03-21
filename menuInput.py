import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pickle


#-------------------------------------siti nazhura's part-------------------------------------------


#list the stores that are avalilable on the user selected date and time

#importing dictionary from pickle file
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


class menuPageInput(tk.Frame):
    def __init__(self, master, params):
        print(params)
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
                            activebackground="#944332", activeforeground="#FAE7D7",border=0,command=lambda: master.switch_frame('otherDatesPage')).place(x=1,y=1)


        tk.Label(self,text="hi").pack(side="top", pady=(20, 50), padx=550)



        userInDay = params[2]
        userInTime = int(params[0])

        # siti nazhura's part: (display different stalls and menu, dependent on the day and hour, provided by the user
        if userInDay == "Monday":

            if 7 <= userInTime <= 11:
                self.menuList(mon['AM'])

            elif 12 <= (userInTime) <= 22:
                self.menuList(mon['PM'])

            else:
                Label(self, text="All stalls are closed \n  at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Tuesday":

            if 7 <= userInTime <= 11:
                self.menuList(tues['AM'])

            elif 12 <= userInTime <= 22:
                self.menuList(tues['PM'])

            else:
                Label(self, text="All stalls are closed \n  at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Wednesday":

            if 7 <= userInTime <= 11:
                self.menuList(wed['AM'])



            elif 12 <= userInTime <= 22:
                self.menuList(wed['PM'])

            else:
                Label(self, text="All stalls are closed \n  at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Thursday":

            if 7 <= userInTime <= 11:
                self.menuList(thu['AM'])
            elif 12 <= userInTime <= 22:
                self.menuList(thu['PM'])
            else:
                Label(self, text="All stalls are closed \n  at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))


        elif userInDay == "Friday":

            if 7 <= userInTime <= 11:
                self.menuList(fri['AM'])
            elif 12 <= userInTime <= 22:
                self.menuList(fri['PM'])
            else:
                Label(self,text="All stalls are closed \n  at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))

        elif userInDay == "Saturday":

            if 7 <= userInTime <= 11:
                self.menuList(sat['AM'])

            elif 12 <= userInTime <= 15:
                self.menuList(sat['PM'])

            else:
                Label(self, text="All stalls are closed \n  at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))



        elif userInDay == "Sunday":
            if 7 <= userInTime <= 11:

                self.menuList(sun['AM'])

            elif 12 <= userInTime <= 15:

                self.menuList(sun['PM'])

            else:
                Label(self, text="All stalls are closed at this timing!",
                      font=("Caviar Dreams Bold", 30),
                      fg="#944332", bg="#FAE7D7", pady=7, padx=10).pack(pady=(170, 180))



    # siti nazhura's part: (function for the day and hour if statements above
    def menuList(self,list):

        k = [k for k in list.keys()]
        print(k)  # stall names(dictionary version)

        def goto(i):
            newwin = Toplevel(self)
            menu_list = k[i]  # stall names

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


            g = [g for g in list[k[i]]]  # get the number of items in the store

            for h in range(1, len(g) + 1):
                menu = str(list[k[i]][h]['Menu'])  # display the menu (food) for selected store
                price = str(list[k[i]][h]['Price'])  # display the price for selected store
                print(menu)

                Label(leftFrame, text=menu,
                      font=("Caviar Dreams Bold", 18), fg="#944332", bg="#FAE7D7", pady=2, anchor='w').pack(fill='both')
                Label(rightFrame, text="$" + price + "0", font=("Caviar Dreams Bold", 18), fg="#944332", bg="#FAE7D7",
                      pady=2).pack(
                    padx=(0, 20))


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
