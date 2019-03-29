from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import scrolledtext


def list_of_platforms(plugin_names):
    number_of_plugins = len(plugin_names)
    for number, name in enumerate(plugin_names, 1):
        res = number, name
    return res



window = Tk()
window.geometry('550x350+50+50')
window.title("SPREAD")

#FACEBOOK
var1 = IntVar()
Checkbutton(window, text="Facebook", variable=var1).grid(row=0, sticky=W)

fb = Label(window, text="Email address: ", width=15)
fb.grid(column=0, row=1)

facebook_u = Entry(window, width=25)
facebook_u.grid(column=1, row=1)

fb1 = Label(window, text="Password: ", width=15)
fb1.grid(column=0, row=2)

facebook_p = Entry(window, width=25)
facebook_p.grid(column=1, row=2)

#btn1 = Button(window, text="Login", width=5)
#btn1.grid(column=50, row=0)

facebook_l = Button(window, text="Login", width=5)
facebook_l.grid(column=3, row=3)

#TWITTER
var1 = IntVar()
Checkbutton(window,text="Twitter",variable=var1).grid(row=3,sticky=W)

twt =Label(window, text="Email address:", width=15)
twt.grid(column=0, row=4)

twt_u = Entry(window, width=25)
twt_u.grid(column=1, row=4)

twt1 = Label(window, text="Password:", width=15)
twt1.grid(column=0, row=5)

twt_p = Entry(window, width=25)
twt_p.grid(column=1, row=5)

twt_l = Button(window, text="Login", width=5)
twt_l.grid(column=3, row=6)


#txt1 = scrolledtext.ScrolledText(window,width=40,height=10).grid(column=2,row = 7)
#chk_state = BooleanVar()
#chk_state.set(True)

#var1 = IntVar()
#Checkbutton(window,text="Facebook",variable=var1).grid(row=0,sticky=W)
#txt = Entry(window,width=50)
#txt.grid(column=2,row=0)

#var2 = IntVar()
#Checkbutton(window, text="Twitter", variable=var2).grid(row=1, sticky=W)
#txt1 = Entry(window, width=50)
#btn2 = Button(window, text="Login")
#btn2.grid(column=5, row=1)
#txt1.grid(column=2, row=1)

#button = tk.Button(master=frame, text='press', command=list_of_platforms)
#chk.grid(column=0, row=0)

message = Label(window, text="Message box")
message.grid(column=0, row=90)
xt = scrolledtext.ScrolledText(window, width=40, height=10)
xt.grid(column=1, row=100)


def clicked():
    messagebox.showinfo('Message title', 'Message sent!!')

btn = Button(window, text="SEND", command=clicked)
btn.grid(column=3, row=300)
window.mainloop()
