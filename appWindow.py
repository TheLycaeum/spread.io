import sys
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb

plugins = ["Facebook","Twitter", "Instagram","Google +"]
n = len(plugins)


class Display():
    """User-interface for the app using Tkinter"""
    def __init__(self, window):
        self.window = window
        self.window.title("SPREAD.IO")
        self.window.geometry("500x500")
        self.show_platforms(plugins)
        self.message_box()
        self.send_button()
        self.show_screen()

    def show_screen(self):
        """Open's the SPREAD.IO window"""
        self.window.mainloop()

    def show_platforms(self, plugins):
        """Show's the available platforms"""
        row = 0
        for names in plugins:
            var = tk.IntVar()
            plat = tk.Checkbutton(self.window, text=names, variable=var, width=40)
            plat.grid(row=row, column=2)
            row += 7

    def message_box(self):
        """to print a label: Message box"""
        message = tk.Label(self.window, text="Message box", width=40)
        message.grid(column=2, row=90)
        self.scrolled_text()

    def scrolled_text(self):
        """Now let's create scrolled text to type message/content"""
        self.text_frame = st.ScrolledText(self.window, width=40, height=10)
        self.text_frame.grid(column=2, row=200)

    def send_button(self):
        """Button for sending conent"""
        button = tk.Button(self.window, text="SEND", state='normal', command=self.send_to)
        button.grid(row=300, column=2)

    def send_to(self):
        """send the message/content inside message_box and checks scrolledtext is empty or not"""
        send_text = self.text_frame.get('1.0', tk.END)
        if len(send_text) == 1:
            mb.showinfo("Warning!!!", "Box is empty!")
        print(send_text)


def main():
    window= tk.Tk()
    Display(window)


if __name__ == '__main__':
    main()
