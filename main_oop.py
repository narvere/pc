import tkinter as tk
from variables import *


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
        self.frame_seft_bottom = None
        self.geometry(main_window_geometry)
        self.frame_left_top = None
        self.frame_right_top = None
        self.title(admin_tool_title)
        self.create_frames()

    def create_frames(self):
        self.frame_left_top = FrameLeft(self)
        self.frame_left_top.grid(row=0, column=0, sticky="w", pady=10, padx=10)

        self.frame_right_top = FrameUpdate(self, update_label_text)
        self.frame_right_top.grid(row=0, column=1, columnspan=3, sticky="ne", pady=10, padx=10)

        self.frame_seft_bottom = FrameKeepass(self, keepass_frame)
        self.frame_seft_bottom.grid(row=1, column=0, columnspan=3, sticky="ne", pady=10, padx=10)


class FrameLeft(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.entries = None
        self.create_widgets()

    def create_widgets(self):
        labels_text = [label_first_name, label_last_name, label_ester_login, label_personal_id, label_tht_code,
                       label_phone_number, label_additional_info]
        _form_print(self, labels_text)

        button = tk.Button(self.master, text="Enter", command=self.on_button_click)
        button.grid(row=7, column=0, columnspan=2)

    def on_button_click(self):
        for entry in self.entries:
            print(entry.get())


class FrameUpdate(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.create_widgets()

    def create_widgets(self):
        labels_text1 = [label_arvuti_login_upd_a, label_arvuti_pass_upd_a, label_ester_pass_upd_a,
                        label_zimbra_mail_upd_a, label_zimbra_pass_upd_a]
        _form_print(self, labels_text1)


def create_widgets(self):
    text_text = tk.Text(self, width=text_width, height=text_height)
    text_text.grid(row=0, column=0, rowspan=11, sticky="we")


class FrameKeepass(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        create_widgets(self)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
