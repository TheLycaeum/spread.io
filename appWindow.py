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
        "Shows the list of logged-in platforms"
        self.check_vars = []
        self.list_bar = []
        for plug in linked:
            platform_bar = tk.Frame(self.win)
            self.check_box(platform_bar, plug)
            self.delink_button(platform_bar, plug)
            platform_bar.pack(fill='x')
            self.list_bar.append(platform_bar)         

    def check_box(self, platform_bar, plug):
        "Checkbox for logged-in platform"
        var = tk.IntVar()
        tk.Checkbutton(platform_bar,
                       text=plug.name,
                       variable=var).pack(side='left',
                                          padx=10)
        var.trace("w", lambda *args:self.callback())
        self.check_vars.append(var)
            
    def delink_button(self, platform_bar, plug):
        "Logout button for logged-in platform"
        tk.Button(platform_bar,
                  text="LOG OUT",
                  command=lambda:[plug.delink(),
                                  self.update_platforms()]).pack(side='right',
                                                                 padx=20)


    def callback(self):
        list_vars = [i.get() for i in self.check_vars]
        if max(list_vars) == 1:
            self.button['state'] = 'normal'
        else:
            self.button['state'] = 'disabled'


    def update_platforms(self):
        for obj in self.list_bar:
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
                            command=lambda:self.send(linked))
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
        post_status = []
        for n, platform in enumerate(linked):
            if self.check_vars[n].get() == 1:
                response = platform.post(send_text)
                post_status.append((response, platform))
        self.post_response(post_status)

    def post_response(self, post_status):
        string = []
        clear_text = True
        for item in post_status:
            response, platform = item
            if response:
                string.append("Posted in {}\n".format(platform.name))
            else:
                clear_text = False
                string.append("Posting failed in {}\n".format(platform.name))
        mb.showinfo("Post Status", "".join(string))
        if clear_text:
            self.text_frame.delete('1.0', tk.END)

    def show_screen(self):
        "Opens the 'Spread.io' window""successful "
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
