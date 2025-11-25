from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# setting up main window
root = Tk()
root.title("Denomination Counter")
root.configure(bg="darkgrey")
root.geometry("650x400")

# adding image and labels in the main window
upload = Image.open("money.jpg")

# resize the image resize() method
upload = upload.resize((200, 250))
image = ImageTk.PhotoImage(upload)
label = Label(root, image = image, bg = "lightblue")
label.place(x=180, y = 20)

label1 = Label(root,
               text = "Hey User! Welcome to Denomination Counter Application",
               bg = "lightblue")
label1.place(relx = 0.5, y = 340, anchor = CENTER)

# function to display a message box and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert !! Do you want to calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

# adding buttons to the main window
button1 = Button(root,
                 text = "Let's get started!",
                 command = msg,
                 bg = "brown",
                 fg = "white")
button1.place(x = 260, y = 360)

# function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denomincation Calculator")
    top.configure(bg = "lightgrey")
    top.geometry("600x350+50+50")

    label = Label(top, text = "Enter total amount" , bg ="lightgrey")

    entry = Entry(top)
    lbl = Label(top, text = "Here are number of notes for each denomination", bg = "lightgrey")

    l1 = Label(top, text = "2000", bg = "lightgrey")
    l2 = Label(top, text = "500", bg = "lightgrey")
    l3 = Label(top, text = "100", bg = "lightgrey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    btn = Button(top, text = "Calculate", command = calculator, bg = "brown", fg = "white")  

    # centering widgets in the top window
    label.place(x = 230, y = 50)   
    entry.place(x= 200, y = 80)
    btn.place(x=240, y = 120)   
    lbl.place(x=140, y =170)

    l1.place(x=180, y = 200)
    l2.place(x=180, y = 230)
    l3.place(x=180, y = 260)

    t1.place(x=270, y = 200)
    t2.place(x=270, y = 230)
    t3.place(x=270, y = 260)

    top.mainloop()

# start the GUI event loop
root.mainloop()