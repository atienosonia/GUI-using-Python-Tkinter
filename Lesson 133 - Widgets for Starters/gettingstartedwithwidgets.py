# import necessary libraries
from tkinter import *
from datetime import date

# create window
root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

# add widgets
# add label

lbl = Label(text = "Hey there!", fg = "black", bg="purple", height = 1, width = 300)

# add label for getting name as input from user
# use entry widget to create a text box for user to enter details 

name_lbl = Label(text = "Full Name", bg = "lightblue")
name_entry = Entry()

# funcion to display a message 
def display():

    # read input given by the user
    name = name_entry.get()

    # declaring a global variable to make it accessible anywhere in the program 

    global message

    message = "welcome to the application! \nToday's date is : "

    greet = "Hello " + name + "\n"

    # display details in the textbox
    # specify where to add details in the textbox
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# add a text widget to display information/messages

text_box = Text(height = 3)

# add buttopn and give value of command as name of the 
# function
# press button
# display function will be called automatically 

btn = Button(text = "Press Me !", command = display, height = 1, bg = "pink", fg= "black")

# organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# start the GUI event loop
root.mainloop()