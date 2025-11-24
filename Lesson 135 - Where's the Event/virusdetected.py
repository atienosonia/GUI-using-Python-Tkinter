# import necessary libraries
from tkinter import *
from tkinter import messagebox

# setup Tkinter window
root = Tk()
root.title("Virus Detected")    
root.geometry("200x250")

# function for displaying warning message
# this will be called once the button is clicked 
# messagebox.showwarning("window name", "text to be")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found!!")

# adding buttoon widget to window
button = Button(root, text = "Scan for Virus", command = msg, bg = "crimson", fg = "black")

button.place(x = 40, y = 80)

# entering main event loop
root.mainloop()