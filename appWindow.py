from tkinter import *

def list_of_platforms(plugin_names):
    number_of_plugins = len(plugin_names)
    for number, names in enumerate(plugin_names, 1):
        print(number, names)


def main():
    window = Tk()
    window.geometry('350x250')
    window.title("SPREAD")
    lbl = Label(window, text="Hello")
    lbl.grid(column=3, row=4)
    btn = Button(window, text="Click me",bg="orange",fg="red")
    btn.grid(column=1, row=0)
    window.mainloop()
