from tkinter import *

#setting up main window
root = Tk()
root.geometry("400x400")
root.title("main")

# function to open nwe (top level) window
def topwin():
    # setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("top level")

    # adding a lable widget to Top Window
    l2 = Label(top, text = "This is a top level window")
    l2.pack()

    top.mainloop()

# adding a label and button widget to root (main) window
l = Label(root, text = "This is the root window")
btn = Button(root, text = "Click here to open another window", command= topwin)

# arrange widgets
l.pack()
btn.pack()
root.mainloop()