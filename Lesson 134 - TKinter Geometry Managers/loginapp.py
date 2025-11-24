# import necessary libraries
from tkinter import *

# create window

root = Tk()
root.title("Login Application")
root.geometry("400x300")


# create a frame to organize elements better 
frame = Frame(master = root, height = 200, width= 300, bg = "lightgray")

# add widgets
# add label
lbl1 = Label(frame, text = "Full Name", bg = "lightblue", fg = "white", width=12)
lbl2 = Label(frame, text = "Password", bg = "lightblue", fg = "white", width=12)
lbl3 = Label(frame, text = "Email ID", bg = "lightblue", fg = "white", width=12)

 
# use entry widget to create a text box for user to enter details

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# function to display message 
def display():
    name = name_entry.get()
    greet = "Hey" + " " + name
    message = "\nCongratulations for your new account!!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

# textbox to display message
textbox = Text(bg = "lightgrey", fg = "black")

# add a button, when pressed, message will be displayed 
btn = Button(text = "Create Account", command = display, bg = "indigo", fg = "white")


# arrange all widgets
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)

name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)

email_entry.place(x=150, y=80)
lbl3.place(x=20, y =140)

pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

# start the GUI event loop
root.mainloop()