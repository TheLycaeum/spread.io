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

    def show_screen(self):
        """Open's the SPREAD.IO window"""
        self.window.mainloop()

    def show_platforms(self, plugins):
        """Show's the available platforms"""
        btn = tk.Button(self.window, text="SEND", state='normal', command=self.send)
        btn.grid(row=300, column=2)
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
        self.window.text_frame = st.ScrolledText(self.window, width=40, height=10)
        self.window.text_frame.grid(column=2, row=200)
            
    def send(self):
        """send the message/content inside message_box"""
        send_text = self.window.text_frame.get('1.0', tk.END)
        if len(self.window.text_frame.get('1.0', tk.END)) == 1:
            mb.showinfo("Warning!!!", "Box is empty!")
        print(send_text)
            


def main():
    window= tk.Tk()
    app = Display(window)
    app.show_platforms(plugins)
    app.message_box()
    app.scrolled_text()
    app.show_screen()


if __name__ == '__main__':
    main()
