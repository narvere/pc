from tkinter import Tk, Menu

root = Tk()

# Create a menu
menu = Menu(root)
root.config(menu=menu)


def some_callback_function(*event):
    print("Button pressed")


# Create a menu button with a keyboard shortcut
menu.add_command(label="Push Me", accelerator="Ctrl+P", command=some_callback_function)

# Set up the keyboard binding for the shortcut
root.bind_all("<Control-p>", some_callback_function)

root.mainloop()
