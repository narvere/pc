from tkinter import Tk, Menu

root = Tk()


menu_bar = Menu(root)

def some_callback_function():
    print("Button pressed")


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=some_callback_function, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=some_callback_function)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

root.bind_all("<Control-o>", some_callback_function)


root.mainloop()
