import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb

class Display():
    "User-interface for the app using Tkinter"

    def __init__(self, plugins):
        self.win = tk.Tk()
        self.win.title("Spread.io")
        self.win.geometry("500x400")
        self.win.resizable(0,0)
        self.plugins = plugins

        self.add_button()
        self.show_platforms()
        self.message_box()
        self.send_button()
        self.show_screen()


    def show_screen(self):
        "Opens the 'Spread.io' window"
        self.win.mainloop()

    def add_button(self):
        plus = tk.Button(self.win,
                         text="+",
                         width=20,
                         command=self.add_window)
        plus.pack()

    def show_platforms(self):
        "Shows the available platforms"
        self.vars = []
        for names in self.plugins:
            var = tk.IntVar()
            plat = tk.Checkbutton(self.win,
                                  text=names,
                                  variable=var)
            self.vars.append(var)  ###
            plat.pack(anchor='w')

    def message_box(self):
        "Creates a message-box to type the message/content"
        message = tk.Label(self.win,
                           text="Message box")
        message.pack(anchor='center')
        self.text_frame = st.ScrolledText(self.win,
                                          width=55,
                                          height=10)
        self.text_frame.pack(anchor='center')


    def send_button(self):
        "Button for sending content"
        send_text = self.text_frame.get('1.0', tk.END)
        button = tk.Button(self.win,
                           text="SEND",
                           command=self.send)
        button.pack(anchor='e', padx=20, pady=20)
        
    def send(self):
        "Sends the content inside message-box"
        send_text = self.text_frame.get('1.0', tk.END)
        if len(send_text) == 1:
            mb.showinfo("Warning", "Box is empty!")
        print(send_text)

    def add_window(self):
        subwin = tk.Tk()
        self.subwin = subwin
        self.subwin.title("Add platforms")
        self.subwin.geometry("300x200")
        for names in self.plugins:
            plat = tk.Button(self.subwin,
                            text=names,
                            width=40,
                            command=self.login_win)
            plat.pack()

    def login_win(self):
        self.subwin.destroy()
        popwin = tk.Tk()
        popwin.title("Entry Level")
        popwin.geometry("300x200")
        lbl = tk.Label(popwin,
                    text="Enter Pin",
                    width=15)
        lbl.pack()
        self.checkpoint = tk.Entry(popwin, width=25)
        self.checkpoint.pack()
        login_btn = tk.Button(popwin,
                              text="ADD",
                              command=self.send_pin)
        login_btn.pack()

    def send_pin(self):
        "Sends the content inside message-box"
        add_pin = self.checkpoint.get()
        print(add_pin)
