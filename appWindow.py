import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from spread import Spread

class Display():
    "User-interface for the app using Tkinter"

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Spread.io")
        self.win.geometry("500x400")
        self.win.resizable(0,0)


    def add_button(self, plug_ins):
        plus = tk.Button(self.win,
                         text="+",
                         width=20,
                         command=lambda:self.add_window(plug_ins))
        plus.pack()

    def add_window(self, plug_ins):
        subwin = tk.Tk()
        self.subwin = subwin
        self.subwin.title("Add platforms")
        self.subwin.geometry("300x{}".format(50*len(plug_ins)))
        self.subwin.resizable(0,0)
        for plug in plug_ins:
            self.create_button(plug)

    def create_button(self, plug):
            plat = tk.Button(self.subwin,
                            text=plug.name,
                            width=40,
                            command=lambda:[plug.log_in(), self.login_window(plug)])
            plat.pack(pady=5)

    def login_window(self, plug):
        self.subwin.destroy()
        popwin = tk.Tk()
        popwin.title("Login to {}".format(plug.name))
        popwin.geometry("300x100")
        popwin.resizable(0,0)

        tk.Label(popwin,
                 text="Enter Pin",
                 width=15).pack()
        self.checkpoint = tk.Entry(popwin, width=25)
        self.checkpoint.pack()
        login_btn = tk.Button(popwin,
                              text="ADD",
                              command=lambda:self.send_pin(plug))
        login_btn.pack()


    def send_pin(self, plug):
        "Sends authentication verifier to respective platforms"
        add_pin = self.checkpoint.get()
        self.checkpoint.destroy()
        plug.write_user_keys(add_pin)
        
    def show_platforms(self, linked):
        "Shows the available platforms"
        self.vars = []
        for plug in linked:
            var = tk.IntVar()
            plat = tk.Checkbutton(self.win,
                                  text=plug.name,
                                  variable=var)
            self.vars.append(var)  ###
            plat.pack(anchor='w')
            self.delink_button(plug)


    def delink_button(self, plug):
            delink_btn = tk.Button(self.win,
                                   text="LOG OUT",
                                   command=plug.delink)
            delink_btn.pack(anchor='e', pady=1)


    def message_box(self):
        "Creates a message-box to type the message/content"
        message = tk.Label(self.win,
                           text="Message box")
        message.pack(anchor='center')
        self.text_frame = st.ScrolledText(self.win,
                                          width=55,
                                          height=10)
        self.text_frame.pack(anchor='center')


    def send_button(self,linked):
        "Button for sending content"
        send_text = self.text_frame.get('1.0', tk.END)
        button = tk.Button(self.win,
                           text="SEND",
                           command=lambda:[self.send(linked)])
        button.pack(anchor='e', padx=20, pady=20)
        
    def send(self,linked):
        "Sends the content inside message-box"
        send_text = self.text_frame.get('1.0', tk.END)
        if len(send_text) == 1:
            mb.showinfo("Warning", "Box is empty!")
        else:
            self.put_post(linked, send_text,self.vars)
        

    def put_post(self, linked,send_text,vars):
        "Posts message to respective linked platforms"
        for i in range(len(linked)):
            if vars[i].get() == 1:
                linked[i].post(send_text)

    def show_screen(self):
        "Opens the 'Spread.io' window"
        self.win.mainloop()



def main():
    app = Spread()    
    appwin = Display()

    plugins = app.get_plugins()
    appwin.add_button(plugins)

    linked = app.check_linked()
    appwin.show_platforms(linked)

    appwin.message_box()
    appwin.send_button(linked)
    appwin.show_screen()


if __name__ == '__main__':
    main()
