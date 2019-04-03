import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb

class Display():
    "User-interface for the app using Tkinter"

    def __init__(self, window):
        self.win = window
        self.win.title("Spread.io")
        self.win.geometry("500x370")
        self.win.resizable(0,0)
        self.show_platforms(plugins)
        self.message_box()
        self.send_button()
        self.show_screen()

    def show_screen(self):
        "Opens the 'Spread.io' window"
        self.win.mainloop()

    def show_platforms(self, plugins):
        "Shows the available platforms"
        self.vars = []
        for names in plugins:
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


plugins = ["Facebook", "Twitter", "Instagram", "Google +"]
def main():
    window = tk.Tk()
    Display(window)
    # app = Display(window)

if __name__ == '__main__':
    main()
