from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import scrolledtext


plugins = ["Facebook","Twitter"]
n = len(plugins)


def button(window):
    row = 0
    for names in plugins:
        var = IntVar()
        c = Checkbutton(window, text=names, variable=var, width=40)
        c.grid(column=2, row=row, sticky=W)
        row += 7


def user_id(window):
    row = 1
    for i in range(n):
        lbl = Label(window, text="Email Address:", width=15)
        lbl.grid_rowconfigure(0, row=row)
        row += 5


def passwd(window):
    row = 2
    for i in range(n):
        lbl1 = Label(window, text="Password", width=50)
        lbl1.grid(column=0, row=row)
        row += 6


#def entry_text(window):
 #   row = 1
  #  for i in range(n):
   #     ent = Entry(window, width=25)
    #    ent.grid(column=1, row=row)
     #   row += 5

#def entry_text1(window):
 #   row = 2
  #  for i in range(n):
   #     ent = Entry(window, width=25)
    #    ent.grid(column=1, row=row)
     #   row += 5

#def l_button(window):
 #   row = 3
  #  for i in range(n):
   #     lb = Button(window, text="Login", width=5)
    #    lb.grid(column=3, row=row)
     #   row += 4

def message_box(window):
    message = Label(window, text="Message box", width=40)
    message.grid(column=2, row=90)
    xt = scrolledtext.ScrolledText(window, width=40, height=10)
    xt.grid(column=2, row=200)

def send_message(window, message_box):
    value = event.widget.get("1.0", "end-1c")
    print("CONTENT:") + value
def clicked():
    messagebox.showinfo('Message title', 'Message sent!!')

def send_button(window,clicked):
    btn = Button(window, text="SEND", command=clicked)
    btn.grid(column=2, row=300)


def main():
    window = Tk()
    window.title("SPREAD")
    window.geometry("500x500+450+100")
    #width, height = window.winfo_screenwidth(), window.winfo_screenheight()
    #window.geometry('%dx%d+0+0' % (width,height))
    #window.geometry("1080x800")
    button(window)
    #user_id(window)
    #passwd(window)
    #entry_text(window)
    #l_button(window)
    message_box(window)
    send_message(window, message_box)
    send_button(window,clicked)
    mainloop()

if __name__ == '__main__':
    main()
