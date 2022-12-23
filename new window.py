import tkinter as tk

# Create the main window
window = tk.Tk()


# Define a function that will create the new window
def open_new_window():
    # Create the new window
    new_window = tk.Toplevel(window)

    # Create a label widget and add it to the new window
    label = tk.Label(new_window, text='Hello')
    label.pack()


# Create a button widget that will open the new window when clicked
button = tk.Button(window, text='Open new window111', command=open_new_window)
button.pack()

# Run the Tkinter event loop
window.mainloop()
