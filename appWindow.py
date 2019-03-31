import sys
import tkinter as tk
from tkinter import scrolledtext as st


plugins = ["Facebook","Twitter", "Instagram","Google +"]
n = len(plugins)


class Display():
    """Create a Display class for the app,setup window, title and geometry"""
    def __init__(self, window):
        self.window = window
        self.window.title("SPREAD")
        self.window.geometry("500x500")
    def screen(self):
        """setup mainloop"""    
        self.window.mainloop()

    def button(self):
        """Send button and checkbutton created in this function"""
        if len(self.window.text_frame.index("end")) == 0:
            btn = tk.Button(self.window, text="SEND", state='disabled')
            btn.grid(row=300, column=2)
        btn = tk.Button(self.window, text="SEND", state='normal', command=self.send)
        btn.grid(row=300, column=2)
            #btn['state'] = 'normal'
        row = 0
        for names in plugins:
            var = tk.IntVar()
            plat = tk.Checkbutton(self.window, text=names, variable=var, width=40)
            plat.grid(row=row, column=2)
            row += 8

    def message_box(self):
        """To print message box"""
        message = tk.Label(self.window, text="Message box", width=40)
        message.grid(column=2, row=90)

    def scrolled_text(self):
        """Now let's create scrolled text to type message"""
        self.window.text_frame = st.ScrolledText(self.window, width=40, height=10)
        self.window.text_frame.grid(column=2, row=200)
            
    def send(self):
        """send function used to return the inside content of scrolltext"""
        send_text = self.window.text_frame.get('1.0', tk.END)
        print(send_text)


def main():
    window= tk.Tk()
    app = Display(window)
    app.button()
    app.message_box()
    app.scrolled_text()
    app.screen()


if __name__ == '__main__':
    main()
