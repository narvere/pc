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
        self.frame_right_bottom = None
        self.frame_left_bottom = None
        self.frame_left_top = None
        self.frame_right_top = None
        self.geometry(main_window_geometry)
        self.title(admin_tool_title)
        self.create_frames()

    def create_frames(self):
        self.frame_left_top = FrameLeft(self)
        self.frame_left_top.grid(row=0, column=0, sticky="w", pady=10, padx=10)

        self.frame_right_top = FrameUpdate(self, update_label_text)
        self.frame_right_top.grid(row=0, column=1, columnspan=3, sticky="ne", pady=10, padx=10)
        #
        # self.frame_left_bottom = FrameKeepass(self, keepass_frame)
        # self.frame_left_bottom.grid(row=1, column=0, columnspan=3, sticky="we", pady=10, padx=10)
        #
        # self.frame_right_bottom = FrameSMS(self, sms_frame)
        # self.frame_right_bottom.grid(row=2, column=0, columnspan=3, sticky="we", pady=10, padx=10)


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
        button.grid(row=3, column=1, columnspan=2, sticky="w")

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
