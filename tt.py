import tkinter as tk

def print_state():
    # Get the state of the checkbox
    state = check.state()
    print(state)

root = tk.Tk()
check = tk.Checkbutton(root, text="Option")
button = tk.Button(root, text="Print", command=print_state)
check.pack()
button.pack()
root.mainloop()
