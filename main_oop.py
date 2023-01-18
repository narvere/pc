import tkinter as tk
from variables import *


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame_left_entries = None
        self.frame_update = None
        self.title(admin_tool_title)
        self.create_frames()

    def create_frames(self):
        self.frame_left_entries = FrameLeft(self)
        self.frame_left_entries.grid(row=0, column=0)

        self.frame_update = FrameUpdate(self, update_label_text)
        self.frame_update.grid(row=0, column=2)


class FrameLeft(tk.Frame):
    @classmethod
    def form_print(cls, master, labels_text):
        labels = []
        entries = []
        for i in range(len(labels_text)):
            label = tk.Label(master, text=labels_text[i], width=12, anchor="w")
            label.grid(row=i, column=0)
            labels.append(label)

            entry = tk.Entry(master)
            entry.grid(row=i, column=1, sticky="w", ipadx=entry_len)
            entries.append(entry)

    def __init__(self, master):
        super().__init__(master)
        self.labels = None
        self.entries = None
        self.create_widgets()

    def create_widgets(self):

        labels_text = [label_first_name, label_last_name, label_ester_login, label_personal_id, label_tht_code,
                       label_phone_number, label_additional_info]

        self.form_print(self.master, labels_text)

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
        # label = tk.Label(self, text="This is Frame 2")
        # label.pack()
        labels_text = [label_arvuti_login_upd_a, label_arvuti_pass_upd_a, label_ester_pass_upd_a,
                       label_zimbra_mail_upd_a, label_zimbra_pass_upd_a]
        # self.form_print(self.master, labels_text)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("My Tkinter App")
#
#         self.labels = []
#         self.entries = []
#
#         labels_text = [label_first_name, label_last_name, label_ester_login, label_personal_id, label_tht_code,
#                        label_phone_number, label_additional_info]
#
#         for i in range(7):
#             label = tk.Label(master, text=labels_text[i], width=12, anchor="w")
#             label.grid(row=i, column=0)
#             self.labels.append(label)
#
#             entry = tk.Entry(master)
#             entry.grid(row=i, column=1, sticky="w", ipadx=entry_len)
#             self.entries.append(entry)
#
#         button = tk.Button(master, text="Enter", command=self.on_button_click)
#         button.grid(row=7, column=0, columnspan=2)
#
#     def on_button_click(self):
#         for entry in self.entries:
#             print(entry.get())
#
#
# root = tk.Tk()
# app = App(root)
# root.mainloop()
