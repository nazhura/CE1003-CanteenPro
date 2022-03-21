import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font


#-------------------------------------siti nazhura's part-------------------------------------------
class operatingHrs(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        image2 = Image.open('img\storeinfoV2.png')
        image1 = ImageTk.PhotoImage(image2)
        background_label = tk.Label(self, image=image1)
        background_label.image1 = image1
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Button(self, text="❮", font=("Carviar Dreams Bold", 25), fg="#FAE7D7", bg="#944332",
                  activebackground="#944332", activeforeground="#FAE7D7", border=0,
                  command=lambda: master.switch_frame('StartPage')).place(x=1, y=1)

        tk.Label(self, text="hi").pack(side="top", pady=(100, 500), padx=550)

        cFont = font.Font(family='Caviar Dreams Bold', size=12)



        def on_configure(event):
            # update scrollregion after starting 'mainloop'
            # when all widgets are in canvas
            canvas.configure(scrollregion=canvas.bbox('all'))


        frame = Frame(self)
        frame.place(x=60, y=180)

        last = PhotoImage(file="img\_last.png")
        Label(frame, image=last)



        # --- create canvas with scrollbar ---

        canvas = Canvas(frame, bg="#483c32", width=820, height=340)
        canvas.pack(side=LEFT)

        scrollbar = Scrollbar(frame, command=canvas.yview)
        scrollbar.pack(side=LEFT, fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.bind('<Configure>', on_configure)

        frame2 = Frame(canvas, bg="#483c32",padx=20)
        # frame2.pack()
        canvas.create_window((0,0), window=frame2, anchor='nw')

        # --- add widgets in frame ---

        stores = ["Clay Pot", "Beverages", "Mun Chee", "Salad", "Xin Mei \n Ban Mian",
                  "YT Duck", "Indian", "Vinford\nWestern", "Yong Tau\nFoo", "Xian Mei Shi"]


        operatinghours = ["Monday & Wednesday: 7am to 10pm \n Sunday: 7am - 12pm",  # claypot
                          "Monday - Friday: 7am to 10pm \n Saturday & Sunday: 7am to 3pm",  # bev
                          "Monday & Wednesday: 7am to 10pm",  # munchee
                          "Monday - Friday: 7am to 10pm \n Saturday: 7am to 12pm \n Closed on Wednesdays",  # salad
                          "Monday & Thursday: 7am to 10pm",  # ban mian
                          "Tuesday & Friday: 7am to 10pm \n Saturday: 12pm to 3pm",  # ytduck
                          "Tuesday & Friday: 7am to 10pm \n Saturday: 7am to 3pm",  # indian
                          "Tuesday - Thursdsay: 7am to 10pm \n Sunday: 7am 3pm",  # western
                          "Wednesday - Thursday: 7am to 10pm \n Sunday: 7am to 3pm",  # ytf
                          "Satuday: 7am to 12pm"  # xms
                          ]

        storeInfo = ["Clay Pot serves sizzling dishes in a claypot\nto satisfy your hunger pangs in the morning.",
                     "Looking for a cool drink on a hot day?\nWhat are you waiting for!\nOrder from our stall for premium"
                     "\nbeverages handcrafted to perfection, only for you.",
                     "Authentic oriental soup for the soul\nwhether you are having a bad or good day.\nCome get your hearty soups before they run out",
                     "Who says salads are for those who are dieting?\nOur Salads are healthy yet sinfully good.",
                     "NTU's most famous ban mian store. Need I say more?\nLoved by local and exchange students.",
                     "We specialize in serving hand crafted duck rice.",
                     "Craving for Briyani on campus? Order now!\nWe also sell prata, thosai and\nauthentic Indian dishes.",
                     "Competable with Astons.\nRight here at North Spine food court!",
                     "Heresay ours is better than\nSouth Spine food court.",
                     "We are ONLY opened on Saturday mornings to provide\nbest quality breakfast catered to YOUR taste"]


        imgstring = ["img\_claypotv4.png","img\_bevv4.png","img\_muncheev2.png","img\_saladv3.png","img\_banmianv2.png","img\_ytv2.png","img\_indv4.png","img\_vinfordv3.png","img\_ytf.png","img\_lastv2.png"]



        for i in range(len(stores)):
            image4 = Image.open(imgstring[i])
            image3 = ImageTk.PhotoImage(image4)
            idl = Label(frame2, image=image3, bg="#483c32")
            idl.image3 = image3
            idl.grid(row=i,column=0)


            Label(frame2, text=stores[i], bg="#483c32" , fg="#fae7d7",font=("Caviar Dreams Bold", 10)).grid(row=i, column=1)
            Label(frame2, text="Operating hours: \n" + operatinghours[i], bg="#483c32" , fg="#fae7d7", font=("Caviar Dreams Bold", 10)).grid(row=i, column=2)
            Label(frame2, text=storeInfo[i], bg="#483c32" , fg="#fae7d7", font=("Caviar Dreams Bold", 10)).grid(row=i, column=3)

