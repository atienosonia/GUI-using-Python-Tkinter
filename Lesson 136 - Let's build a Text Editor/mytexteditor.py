# import necessary packages
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

# setup root window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x600")
window.rowconfigure(0, weight=1, minsize=800)
window.columnconfigure(1, weight=1, minsize=800)

# function to open a file
def open_file():
    # open file for editing
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    # if a file is open then display the contents of the file 

    with open(filepath, "r") as input_file:
        # read contents of the file
        text = input_file.read()

        # insert contents of the file in the editor box
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codingal's Text Editor - {filepath}")    

    # Function to save a file
    