import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb

class Display():
    "User-interface for the app using Tkinter"

    def __init__(self, window):
        self.win = window
        self.win.title("Spread.io")
        self.win.geometry("500x500")

        self.show_platforms(plugins)
        self.message_box()
        self.send_button()
        self.show_screen()

    def show_screen(self):
        "Opens the 'Spread.io' window"
        self.win.mainloop()

    def show_platforms(self, plugins):
        "Shows the available platforms"
        row = 0
        for names in plugins:
            var = tk.IntVar()
            plat = tk.Checkbutton(self.win,
                                  text=names,
                                  variable=var,
                                  width=40)
            plat.grid(column=2, row=row)
            row += 7

    def message_box(self):
        "Creates a message-box to type the message/content"
        message = tk.Label(self.win,
                           text="Message box",
                           width=40)
        message.grid(column=2, row=90)
        self.scrolled_text()

    def scrolled_text(self):
        "Creates scrolled text to type message"
        self.text_frame = st.ScrolledText(self.win,
                                          width=40,
                                          height=10)
        self.text_frame.grid(column=2,
                             row=200)

    def send_button(self):
        "Button for sending content"
        send_text = self.text_frame.get('1.0', tk.END)
        button = tk.Button(self.win,
                           text="SEND",
                           command=self.send)
        button.grid(row=300, column=2)
        
    def send(self):
        "Sends the content inside message-box"
        send_text = self.text_frame.get('1.0', tk.END)
        if len(send_text) == 1:
            mb.showinfo("Warning", "Box is empty!")
        # print(send_text)


plugins = ["Facebook", "Twitter", "Instagram", "Google +"]
def main():
    window = tk.Tk()
    Display(window)
    # app = Display(window)

if __name__ == '__main__':
    main()
