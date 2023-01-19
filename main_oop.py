import tkinter as tk
from variables import *
import sqlite3
import variables

from pass_generator import pass_gen, eesti_speller
from mail_engine import send_mail
import tkinter.messagebox as messagebox
from isikukood import ikood
import re

from validators import is_empty

clipboard_SMS_txt = ""
clipboard_keepass_text = ""

# Connect to the database
conn = sqlite3.connect('C:/Users/7272/PycharmProjects/pc/database.db')
cursor = conn.cursor()


# def show_menu_bar(*event):
#     menu_bar.pack(side="top", fill="x")

def copy_to_clipboard(self, clipboard_text, *event):
    """
    Clipboard engine
    :param self:
    :param clipboard_text:
    :param event: short key
    :return:
    """
    self.clipboard_clear()
    self.clipboard_append(clipboard_text)


def _form_print(self, labels_text):
    labels = []
    entries = []
    for i in range(len(labels_text)):
        label = tk.Label(self, text=labels_text[i], width=12, anchor="w")
        label.grid(row=i, column=0, pady=2)
        labels.append(label)

        entry = tk.Entry(self)
        entry.grid(row=i, column=1, sticky="w", ipadx=entry_len)
        entries.append(entry)


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menu_bar = MenuBar(self)
        self.frame_right_bottom = None
        self.frame_left_bottom = None
        self.frame_left_top = None
        self.frame_right_top = None
        self.geometry(main_window_geometry)
        self.title(admin_tool_title)
        self.create_frames()

    def create_frames(self):
        self.frame_left_top = FrameLeft(self)
        self.frame_left_top.grid(row=0, column=0, sticky="w", pady=10, padx=10, rowspan=7, columnspan=1)

        self.frame_right_top = FrameUpdate(self, update_label_text)
        self.frame_right_top.grid(row=0, column=1, columnspan=3, sticky="ne", pady=10, padx=10, rowspan=5)

        self.frame_left_bottom = FrameKeepass(self, keepass_frame)
        self.frame_left_bottom.grid(row=8, column=0, columnspan=3, sticky="we", pady=10, padx=10)

        self.frame_right_bottom = FrameSMS(self, sms_frame)
        self.frame_right_bottom.grid(row=9, column=0, columnspan=3, sticky="we", pady=10, padx=10)


def del_str(self, nr):
    # Delete a row with a specific id
    cursor.execute("DELETE FROM users WHERE id=?", (nr,))

    # Commit the changes
    conn.commit()
    fetching_data(self.frame_setup)


def fetching_data(frame_setup):
    # Select all rows from the table
    cursor.execute("SELECT * FROM users")

    # Fetch the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        mail = row[1]
        keepass = row[2]
        sms = row[3]

        # label_add_mail = Label(frame_setup, text=f"{entry_string}, {checkbox1_state_keepass}, {checkbox2_state_sms}")
        label_add_mail = tk.Label(frame_setup, text=f"{mail}, KeePass - {keepass}, SMS - {sms}")
        label_add_mail.grid(row=row[0], column=0, sticky="w")
        xxx = tk.Button(frame_setup, text="Del", command=lambda id=row[0]: del_str(id))
        xxx.grid(row=row[0], column=1)


class SetupWindow:
    def __init__(self, root):
        self.root = root
        self.new_window = None
        self.frame_setup = None
        self.checkbox1_var = tk.IntVar()
        self.checkbox2_var = tk.IntVar()
        self.entry_to_database = None

    def open_setup_window(self, event=None):
        """
        New window creation
        :return:
        """
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry(setup_window_geometry)
        self.new_window.title(admin_tool_title)
        self.frame_setup = tk.Frame(self.new_window)
        self.frame_setup.grid(row=0, column=0, columnspan=3, sticky="w", pady=10, padx=10)
        self.entry_to_database = tk.Entry(self.frame_setup)
        self.checkbox1_keepass = tk.Checkbutton(self.frame_setup, text=variables.keepass_frame,
                                                variable=self.checkbox1_var, onvalue=1, offvalue=0)
        self.checkbox2_sms = tk.Checkbutton(self.frame_setup, text=variables.sms_frame, variable=self.checkbox2_var,
                                            onvalue=1, offvalue=0)
        fetching_data(self.frame_setup)

        def is_valid_email(self, email):

            # Use the fullmatch() function to check if the email address matches the regular expression
            if re.fullmatch(email_regex, email):
                return True
            else:
                return False

        def error_setup(self, err):
            return messagebox.showerror("Error!", f"Поле cодержит ошибку: {self, err}!")

        def new_email_adding():
            """
            Button Add engine
            :return:
            """
            print("pushed")
            entry_string = self.entry_to_database.get()
            if self.is_valid_email(entry_string):
                # Perform action with entry_string
                print("valid email")
            else:
                self.error_setup("email")
            # if not is_valid_email(entry_string):
            #     error_setup(email_error_msg)
            #     return
            #
            # if not is_empty(entry_string):
            #     error_setup(smpty_string_msg)
            #     return
                # raise ValueError("String is empty")

            checkbox1_state_keepass = self.checkbox1_var.get()
            checkbox2_state_sms = self.checkbox2_var.get()

            if not any([checkbox1_state_keepass, checkbox2_state_sms]):
                error_setup(checkbox_msg)
                return
                # raise ValueError("No checkboxes selected")
            if checkbox1_state_keepass == 1:

                # Searching for a string with a specific ID
                cursor.execute("SELECT * FROM users WHERE keepass=?", (1,))
                row = cursor.fetchone()
                if bool(row):
                    error_setup(keepass_msg)
                    return
            if checkbox2_state_sms == 1:

                # Searching for a string with a specific ID
                cursor.execute("SELECT * FROM users WHERE sms=?", (1,))
                row = cursor.fetchone()
                if bool(row):
                    error_setup(sms_msg)
                    return

            self.entry_to_database.delete(0, tk.END)
            self.checkbox1_keepass.deselect()
            self.checkbox2_sms.deselect()
            # Insert a row of data
            cursor.execute("INSERT INTO users (email, keepass, sms) VALUES (?, ?, ?)",
                           (entry_string, checkbox1_state_keepass, checkbox2_state_sms))

            # Commit the changes
            conn.commit()
            fetching_data(self.frame_setup)

        button_add = tk.Button(self.frame_setup, text=add_email_button, command=new_email_adding)

        # Create a label widget and add it to the new window

        self.entry_to_database.grid(row=0, column=0, ipadx=entry_len, sticky="w")
        # Pack the checkbox widgets
        self.checkbox1_keepass.grid(row=0, column=1, sticky="w")
        self.checkbox2_sms.grid(row=0, column=2, sticky="w")
        button_add.grid(row=0, column=3, sticky="w")


class MenuBar:
    def __init__(self, root):
        self.root = root
        self.setup_window = SetupWindow(root)
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Setup", command=self.setup_window.open_setup_window)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def setup(self):
        print("Setup selected")


class FrameLeft(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        labels_text = [label_first_name, label_last_name, label_ester_login, label_personal_id, label_tht_code,
                       label_phone_number, label_additional_info]
        _form_print(self, labels_text)


class FrameUpdate(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.entries = None
        self.create_widgets()

    def create_widgets(self):
        labels_text1 = [label_arvuti_login_upd_a, label_arvuti_pass_upd_a, label_ester_pass_upd_a,
                        label_zimbra_mail_upd_a, label_zimbra_pass_upd_a]
        _form_print(self, labels_text1)
        button = tk.Button(self.master, text="Enter", command=self.on_button_click)
        button.grid(row=6, column=1, sticky="wn", padx=10, )

    def on_button_click(self):
        for entry in self.entries:
            print(entry.get())


class FrameKeepass(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.entry_alex = None
        self.create_widgets()

    def create_widgets(self):
        self.keepass_frame_widget()
        self.keepass_from_db()

    def keepass_from_db(self):
        global keepass
        try:
            cursor.execute("SELECT * FROM users WHERE keepass=?", (1,))
            keepass = cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving data from the database: {e}")
        if keepass:
            self.entry_alex = tk.Label(self, text=keepass[1])
            self.entry_alex.grid(row=2, column=1, sticky="we", padx=10)
        else:
            self.entry_alex = tk.Label(self, text="None")
            self.entry_alex.grid(row=2, column=1, sticky="we", padx=10)

    def keepass_frame_widget(self):
        text_text = tk.Text(self, width=text_width, height=text_height)

        button_send_to_alex = tk.Button(self, text=send_to_alex_button,
                                        command=lambda: send_mail(keepass[1], clipboard_keepass_text))
        button_copy_to_alex = tk.Button(self, text=copy_to_keepass_button,
                                        command=lambda: copy_to_clipboard(clipboard_keepass_text))

        text_text.grid(row=0, column=0, rowspan=11, sticky="we")
        button_send_to_alex.grid(row=1, column=1, ipadx=10, ipady=5, sticky="we")
        button_copy_to_alex.grid(row=0, column=1, ipadx=10, ipady=5, sticky="we")


class FrameSMS(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.entry_sms = None
        self.create_widgets()

    def create_widgets(self):
        self.sms_frame_widget()
        self.sms_from_db()

    def sms_from_db(self):
        global sms
        try:
            cursor.execute("SELECT * FROM users WHERE sms=?", (1,))
            sms = cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving data from the database: {e}")
        if sms:
            self.entry_sms = tk.Label(self, text=sms[1])
            self.entry_sms.grid(row=2, column=1, padx=10, sticky="we")
        else:
            self.entry_sms = tk.Label(self, text="None")
            self.entry_sms.grid(row=2, column=1, padx=10, sticky="we")

    def sms_frame_widget(self):
        text_sms = tk.Text(self, width=text_width, height=text_text_height)
        button_send_to_sms = tk.Button(self, text=send_to_sms_button,
                                       command=lambda: send_mail(sms[1], clipboard_SMS_txt))
        button_copy_to_sms = tk.Button(self, text=copy_to_sms_button,
                                       command=lambda: copy_to_clipboard(clipboard_SMS_txt))

        text_sms.grid(row=0, column=0, rowspan=6, sticky="we")
        button_send_to_sms.grid(row=1, column=1, ipadx=10, ipady=5, sticky="we")
        button_copy_to_sms.grid(row=0, column=1, ipadx=10, ipady=5, sticky="we")


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
