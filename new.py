from tkinter import Toplevel, Tk
from main_appa import Label


root = Tk()


def open_new_window():
    # Create the new window
    new_window = Toplevel(root)
    new_window.geometry("250x250")

    # Create a label widget and add it to the new window
    label = Label(new_window, text='This is a new window111')
    label.pack()