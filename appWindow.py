import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from spread import Spread

class Display():
    "User-interface for the app using Tkinter"

    def __init__(self, app):
        self.win = tk.Tk()
        self.win.title("Spread.io")
        self.win.geometry("500x400")
        self.win.resizable(0,0)
        self.app = app


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
                         command=lambda:[self.login_window(plug), plug.log_in()])
        plat.pack(pady=5)
        if plug.is_linked:
            plat['state'] = 'disabled'

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
                              command=lambda:[self.send_pin(plug), popwin.destroy()])
        login_btn.pack()


    def send_pin(self, plug):
        "Sends authentication verifier to respective platforms"
        add_pin = self.checkpoint.get()
        self.checkpoint.destroy()
        plug.write_user_keys(add_pin)
        plug.load()
        plug.check_link()
        self.update_platforms()

    def show_platforms(self, linked):
        "Shows the available platforms"
        self.vars = []
        self.linked_platforms = []
        for plug in linked:
            var = tk.IntVar()
            plat = tk.Checkbutton(self.win,
                                  text=plug.name,
                                  variable=var)
            plat.pack(anchor='w')
            
            d_button = self.delink_button(plug)
            var.trace("w", lambda *args:self.callback())
            self.vars.append(var)
            self.linked_platforms.append(plat)         
            self.linked_platforms.append(d_button)

    def callback(self):
        list_vars = [i.get() for i in self.vars]
        if max(list_vars) == 1:
            self.button['state'] = 'normal'
        else:
            self.button['state'] = 'disabled'

    def delink_button(self, plug):
        delink_btn = tk.Button(self.win,
                               text="LOG OUT",
                               command=lambda:[plug.delink(), self.update_platforms()])
        delink_btn.pack(anchor='e', padx=20)
        return delink_btn

    def update_platforms(self):
        for obj in self.linked_platforms:
            obj.destroy()
        linked = self.app.check_linked()
        self.show_platforms(linked)

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
        self.button = tk.Button(self.win,
                           text="SEND",
                           command=lambda:[self.send(linked), self.text_frame.delete('1.0', tk.END)])
        self.button['state'] = 'disabled'
        self.button.pack(anchor='e', padx=20, pady=20)
        
    def send(self,linked):
        "Sends the content inside message-box"
        send_text = self.text_frame.get('1.0', tk.END)
        if len(send_text) == 1:
            mb.showinfo("Warning", "Box is empty!")
        else:
            self.put_post(linked, send_text)
        

    def put_post(self, linked, send_text):
        "Posts message to respective linked platforms"
        for n, platform in enumerate(linked):
            if self.vars[n].get() == 1:
                post_status = platform.post(send_text)
                if post_status:
                    mb.showinfo("Message status", " Successfully posted in {}".format(platform.name))
                else:
                    mb.showerror("Warning", "{}:Sorry!!Please check your connection".format(platform.name))

    def show_screen(self):
        "Opens the 'Spread.io' window"
        self.win.mainloop()


def main():
    app = Spread()
    appwin = Display(app)

    plugins = app.get_plugins()
    appwin.add_button(plugins)

    linked = app.check_linked()
    appwin.message_box()
    appwin.send_button(linked)

    appwin.show_platforms(linked)

    appwin.show_screen()


if __name__ == '__main__':
    main()
