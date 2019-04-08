import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from spread import Spread

class Display():
    "User-interface for the app using Tkinter"

    def __init__(self, app):
        self.app = app
        self.plugins = self.app.get_plugins()
        self.load_window()

        self.win = tk.Tk()
        self.win.title("Spread.io")
        self.win.geometry("500x400")
        self.win.resizable(0, 0)

        self.add_button()
        linked = app.check_linked()
        self.text_box()
        self.send_button(linked)
        self.show_platform_list(linked)
        self.show_screen()



    def load_window(self):
        "Loading window, shows which platform is loading before opening"
        loadwin = tk.Tk()
        loadwin.title("Spread.io")
        loadwin.geometry("200x100")
        loadwin.resizable(0, 0)

        current_load = tk.Label(loadwin,
                                text="Loading")
        current_load.pack(expand='yes')
        loadbar = ttk.Progressbar(loadwin, length=100, mode="determinate")
        loadbar.pack(expand='yes')

        for plug in self.plugins:
            loadbar['value'] += 100/len(self.plugins)
            current_load.config(text="Loading {}...".format(plug.name))
            current_load.update_idletasks()
            plug.load()
        loadwin.destroy()


    def add_button(self):
        "Button to open add_window"
        tk.Button(self.win,
                  text="+",
                  width=20,
                  command=self.add_window).pack()

    def add_window(self):
        "Window to link more platforms"
        addwin = tk.Tk()
        addwin.title("Add platforms")
        addwin.geometry("300x{}".format(50*len(self.plugins)))
        addwin.resizable(0, 0)
        for plug in self.plugins:
            self.create_button(addwin, plug)

    def create_button(self, addwin, plug):
        "Creates platform_buttons"
        platform_button = tk.Button(addwin,
                                    text=plug.name,
                                    width=40,
                                    command=lambda: [self.login_window(plug),
                                                     plug.log_in(),
                                                     addwin.destroy()])
        platform_button.pack(pady=5)
        if plug.is_linked:
            platform_button['state'] = 'disabled'


    def login_window(self, plug):
        "Window to link respective platform"
        logwin = tk.Tk()
        logwin.title("Login to {}".format(plug.name))
        logwin.geometry("300x100")
        logwin.resizable(0, 0)

        tk.Label(logwin,
                 text="Enter the verifier",
                 width=15).pack()

        self.verifier = tk.Entry(logwin, width=25)
        self.verifier.pack()

        tk.Button(logwin,
                  text="ADD",
                  command=lambda: [self.authentication(plug),
                                   logwin.destroy()]).pack()


    def authentication(self, plug):
        "Sends the verifier to respective platforms to authenticate"
        string = self.verifier.get()
        self.verifier.destroy()
        plug.write_user_keys(string)
        plug.load()
        self.update_platform_list()


    def update_platform_list(self):
        "Updates the list of logged-in platforms"
        for obj in self.list_bar:
            obj.destroy()
        linked = self.app.check_linked()
        self.show_platform_list(linked)


    def show_platform_list(self, linked):
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
        var.trace("w", lambda *args: self.callback())
        self.check_vars.append(var)

    def delink_button(self, platform_bar, plug):
        "Logout button for logged-in platform"
        tk.Button(platform_bar,
                  text="LOG OUT",
                  command=lambda: [plug.delink(),
                                   self.update_platform_list()]).pack(side='right',
                                                                      padx=20)

    def callback(self):
        "Disables send-button if none of platforms are selected"
        list_vars = [i.get() for i in self.check_vars]
        if max(list_vars) == 1:
            self.button['state'] = 'normal'
        else:
            self.button['state'] = 'disabled'


    def text_box(self):
        "Creates a text-box to type the message/content"
        tk.Label(self.win,
                 text="Message box").pack(anchor='center')

        self.text_frame = st.ScrolledText(self.win,
                                          width=55,
                                          height=10)
        self.text_frame.pack(anchor='center')


    def send_button(self, linked):
        "Button for sending content"
        self.button = tk.Button(self.win,
                                text="SEND",
                                command=lambda: self.send(linked))
        self.button.pack(anchor='e', padx=20, pady=20)
        self.button['state'] = 'disabled'

    def send(self, linked):
        "Sends the content inside text-box"
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
        "Shows message box as post response"
        string = []
        clear_text = True
        for item in post_status:
            response, platform = item
            if response:
                string.append("Posted in {}\n".format(platform.name))
            else:
                clear_text = False
                string.append("Posting failed in {}\n".format(platform.name))

        if clear_text:
            mb.showinfo("Post Status", "".join(string))
            self.text_frame.delete('1.0', tk.END)
        else:
            mb.showerror("Post Status", "".join(string))

    def show_screen(self):
        "Opens the 'Spread.io' window""successful "
        self.win.mainloop()



if __name__ == '__main__':
    app = Spread()
    appwin = Display(app)
