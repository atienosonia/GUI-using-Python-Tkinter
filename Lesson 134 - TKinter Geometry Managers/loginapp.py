# import necessary libraries
from tkinter import *

# create window

root = Tk()
root.title("Login Application")
root.geometry("300x200")


# create a frame to organize elements better 
frame = Frame(master = root, height = 200, width= 300, bg = "lightgray")

# add widgets
# add label
lbl1 = Label(frame, text = "Full Name", bg = "lightblue" fg = "white", width=12)
lbl2 = Label(frame, text = "Password", bg = "lightblue" fg = "white", width=12)
lbl3 = Label(frame, text = "Email ID", bg = "darkblue", fg = "white", width=12)
