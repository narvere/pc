import tkinter as tk
import tkinter.messagebox as messagebox

def show_error():
    messagebox.showerror("Error", "An error has occurred")

def show_info():
    messagebox.showinfo("Info", "This is some information")

def ask_question():
    response = messagebox.askquestion("Question", "Do you want to continue?")
    if response == "yes":
        print("Continuing...")
    else:
        print("Canceling...")

root = tk.Tk()

error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.pack()

info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack()

question_button = tk.Button(root, text="Ask Question", command=ask_question)
question_button.pack()

root.mainloop()
