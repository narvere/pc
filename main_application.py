from tkinter import Tk, END, Text, Label, Frame, LabelFrame, Toplevel, IntVar, Checkbutton, Menu
from tkinter.ttk import Entry, Button, Style
import sqlite3
import variables
from variables import *
from pass_generator import pass_gen, eesti_speller
from mail_engine import send_mail
import tkinter.messagebox as messagebox
from isikukood import ikood
import re

from validators import is_empty

root = Tk()
root.geometry(main_window_geometry)
root.resizable(width=False, height=False)
root.title(title)

# Connect to the database
conn = sqlite3.connect(r'C:\Users\7272\Desktop\PycharmProjects\pc\database.db')
cursor = conn.cursor()

"""
Menu creation
"""
menu_bar = Menu(root)

"""
Создание экземпляра Frame и LabelFrame 
"""

frame_left_entries = Frame(root)
frame_right_setup = Frame(root)
frame_keepass = LabelFrame(root, text=keepass_frame)
frame_sms = LabelFrame(root, text=sms_frame)
frame_update = LabelFrame(root, text=update_label_text)


def del_text(*event):
    """
    Removing user text from manin window
    :param event:
    :return:
    """
    text_text.delete(1.0, END)
    text_SMS.delete(1.0, END)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_ester.delete(0, END)
    entry_personal_id.delete(0, END)
    entry_tht_code.delete(0, END)
    entry_phone.delete(0, END)
    entry_info.delete(0, END)
    entry_zimbra_mail_upd.delete(0, END)
    entry_zimbra_pass_upd.delete(0, END)
    entry_ester_pass_upd.delete(0, END)
    entry_arvuti_pass_upd.delete(0, END)
    entry_pc_login_upd.delete(0, END)


def error(err):
    return messagebox.showerror("Error!", f"Поле {err[:-2]} - cодержит ошибку!")


def error_setup(err):
    return messagebox.showerror("Error!", f"Поле cодержит ошибку: {err}!")


def creating_user_text(*event):
    """
    Getting validated user text, sending to clipboard, keepass and SMS functions
    :param event: event method is using for hot keys
    :return:
    """
    if "-" not in entry_name.get().strip():
        if not entry_name.get().strip().isalpha() and not entry_name.get().strip().isalnum():
            error(label_first_name)
            return 0
    if "-" not in entry_surname.get().strip():
        if not entry_surname.get().strip().isalpha() and not entry_surname.get().strip().isalnum():
            error(label_last_name)
            return 0
    if not entry_ester.get().strip().isalnum():
        error(label_ester_login)
        return 0
    if bool(entry_personal_id.get().strip()):
        if not ikood(entry_personal_id.get().strip()):
            error(label_personal_id)
            return 0
    if not bool(entry_phone.get().strip()):
        error(label_phone_number)
        return 0
    if not bool(entry_info.get().strip()):
        error(label_additional_info)
        return 0
    ester_pass, first_name, first_name_speller, last_name_speller, \
        last_surname, pc_login, pc_pass, zimbra_mail, zimbra_pass = clipboard_adding()

    # Data output to save to KeePass
    print_keepass_method(ester_pass, first_name, first_name_speller, last_name_speller, last_surname,
                         pc_login, pc_pass, zimbra_mail, zimbra_pass)
    # Data output to save to SMS
    print_sms_method(ester_pass, first_name_speller, last_name_speller, pc_login, pc_pass, zimbra_pass)


clipboard_SMS_txt = ""
clipboard_keepass_text = ""


def clipboard_adding():
    """
    Text generation for clipboard saving
    :return:
    """
    additional_info, ester_login, ester_pass, first_name, first_name_speller, last_name_speller, \
        last_surname, pc_login, pc_pass, personal_id, phone_number, tht_code, zimbra_mail, \
        zimbra_pass, zimbra_mail_sms = generate_message_variables()
    # Save to clipboard SMS text
    global clipboard_SMS_txt, clipboard_keepass_text
    clipboard_SMS_txt = f"{label_pc_login}{pc_login}\n{label_pc_pass}{pc_pass}\n{label_ester_login}" \
                        f"{ester_login}\n" \
                        f"{label_ester_pass}{ester_pass}\n{label_zimbra_mail}{zimbra_mail_sms}\n" \
                        f"{label_zimbra_pass}{zimbra_pass}\n{label_phone_number}{phone_number}"
    # Save to clipboard KeePass text
    clipboard_keepass_text = f"{label_first_name}{first_name} {last_surname} / {first_name_speller} " \
                             f"{last_name_speller} " \
                             f"\n{clipboard_SMS_txt}\n{label_personal_id}{personal_id}\n" \
                             f"{label_tht_code}{tht_code}\n" \
                             f"{label_additional_info}{additional_info}"
    return ester_pass, first_name, first_name_speller, last_name_speller, \
        last_surname, pc_login, pc_pass, zimbra_mail, zimbra_pass


def print_sms_method(ester_pass, first_name_spelling, last_name_spelling, pc_login, pc_pass, zimbra_pass):
    """
    Creating an SMS message sending
    :param ester_pass: HEDA/ester password
    :param first_name_spelling: user first name
    :param last_name_spelling: user last name
    :param pc_login: user PC login
    :param pc_pass: user PC password
    :param zimbra_pass: user Zimbra mail pass
    :return:
    """
    # Clear txt_textSMS widget
    text_SMS.delete(1.0, END)

    # Insert text into txt_textSMS widget
    pc_login_text = f"{label_pc_login}{pc_login}\n"
    pc_pass_text = f"{label_pc_pass}{pc_pass}\n"
    ester_login_text = f"{label_ester_login}{entry_ester.get()}\n"
    ester_pass_text = f"{label_ester_pass}{ester_pass}\n"
    zimbra_mail_text = f"{label_zimbra_mail}{first_name_spelling.lower()}.{last_name_spelling.lower()}\n"
    zimbra_pass_text = f"{label_zimbra_pass}{zimbra_pass}\n"
    phone_pass_text = f"{label_phone_number}{entry_phone.get().strip()}\n"

    text_SMS.insert(index=1.0, chars=pc_login_text)
    text_SMS.insert(index=2.0, chars=pc_pass_text)
    text_SMS.insert(index=3.0, chars=ester_login_text)
    text_SMS.insert(index=4.0, chars=ester_pass_text)
    text_SMS.insert(index=5.0, chars=zimbra_mail_text)
    text_SMS.insert(index=6.0, chars=zimbra_pass_text)
    text_SMS.insert(index=7.0, chars=phone_pass_text)


def print_keepass_method(ester_pass, first_name, first_name_spelling, last_name_spelling, last_surname, pc_login,
                         pc_pass,
                         zimbra_mail, zimbra_pass):
    """
    Creating a message for KeePass sending
    :param ester_pass:
    :param first_name:
    :param first_name_spelling:
    :param last_name_spelling:
    :param last_surname:
    :param pc_login:
    :param pc_pass:
    :param zimbra_mail:
    :param zimbra_pass:
    :return:
    """
    # Clear txt_text widget
    text_text.delete(1.0, END)

    # Insert text into txt_text widget
    name_text = f"{label_first_name}{first_name_spelling} {last_name_spelling} / {first_name} {last_surname}\n"
    pc_login_text = f"{label_pc_login}{pc_login}\n"
    pc_pass_text = f"{label_pc_pass}{pc_pass}\n"
    ester_login_text = f"{label_ester_login}{entry_ester.get().strip()}\n"
    ester_pass_text = f"{label_ester_pass}{ester_pass}\n"
    zimbra_mail_text = f"{label_zimbra_mail}{zimbra_mail}\n"
    zimbra_pass_text = f"{label_zimbra_pass}{zimbra_pass}\n"
    personal_id_text = f"{label_personal_id}{entry_personal_id.get().strip()}\n"
    tht_code_text = f"{label_tht_code}{entry_tht_code.get().strip()}\n"
    phone_number_text = f"{label_phone_number}{entry_phone.get().strip()}\n"
    additional_info_text = f"{label_additional_info}{entry_info.get().strip()}"

    text_text.insert(index=1.0, chars=name_text)
    text_text.insert(index=2.0, chars=pc_login_text)
    text_text.insert(index=3.0, chars=pc_pass_text)
    text_text.insert(index=4.0, chars=ester_login_text)
    text_text.insert(index=5.0, chars=ester_pass_text)
    text_text.insert(index=6.0, chars=zimbra_mail_text)
    text_text.insert(index=7.0, chars=zimbra_pass_text)
    text_text.insert(index=8.0, chars=personal_id_text)
    text_text.insert(index=9.0, chars=tht_code_text)
    text_text.insert(index=10.0, chars=phone_number_text)
    text_text.insert(index=11.0, chars=additional_info_text)


def generate_message_variables():
    """
    Generating variables for messages from input user text
    :return: variabless for messages
    """
    # Generate passwords
    pc_pass, ester_pass, zimbra_pass = pass_gen()

    # If entered alternative PC password
    if bool(entry_arvuti_pass_upd.get()):
        pc_pass = entry_arvuti_pass_upd.get().strip()

    # If entered alternative ester password
    if bool(entry_ester_pass_upd.get()):
        ester_pass = entry_ester_pass_upd.get().strip()

    # If entered alternative Zimbra password
    if bool(entry_zimbra_pass_upd.get()):
        zimbra_pass = entry_zimbra_pass_upd.get().strip()

    # Generate spelling of first and last names
    first_name_spelling = eesti_speller(entry_name.get().strip().lower().title())
    last_name_spelling = eesti_speller(entry_surname.get().strip().lower().title())

    # Extract first and last names
    first_name = entry_name.get().strip().lower().title()
    last_surname = entry_surname.get().strip().lower().title()

    # Generate Zimbra email address
    zimbra_full_mail = f"{first_name_spelling.lower()}.{last_name_spelling.lower()}{mail}"
    zimbra_mail_sms = f"{first_name_spelling.lower()}.{last_name_spelling.lower()}"

    # zimbra_full_mail = 1
    # zimbra_mail_sms = "0"
    # print(zimbra_full_mail, zimbra_mail_sms)

    # If mail is changed. Influence to email in Keepass box
    # if bool(entry_zimbra_mail_upd.get()):
    #     zimbra_mail_sms = entry_zimbra_mail_upd.get().strip()

    if bool(entry_zimbra_mail_upd.get()):
        zimbra_full_mail = entry_zimbra_mail_upd.get().strip()
        print(zimbra_full_mail)

    # Generate PC login
    if bool(entry_pc_login_upd.get()):
        pc_login = entry_pc_login_upd.get().strip().lower().title()
    else:
        pc_login = entry_ester.get()[1:].strip().lower().title()

    # Extract HEDA/Ester login
    ester_login = entry_ester.get()

    # Extract personal ID
    personal_id = entry_personal_id.get()

    # Extract THT code
    tht_code = entry_tht_code.get()

    # Extract phone number
    phone_number = entry_phone.get()

    # Extract additional info
    additional_info = entry_info.get()
    return additional_info, ester_login, ester_pass, first_name, first_name_spelling, \
        last_name_spelling, last_surname, pc_login, pc_pass, personal_id, phone_number, \
        tht_code, zimbra_full_mail, zimbra_pass, zimbra_mail_sms


def creating_hotkeys():
    """
    Создание горячих клавиш
    """
    root.bind('<Control-e>', creating_user_text)
    root.bind('<Control-d>', del_text)

    # root.bind('<Control-a>', lambda: gtc(clipboard_text))
    # root.bind('<Control-s>', lambda: gtc(clipboard_SMS))


creating_hotkeys()


def open_setup_window(*event):
    """
    New window creation
    :return:
    """
    global frame_setup
    # Create the new window
    new_window = Toplevel(root)
    new_window.geometry(setup_window_geometry)
    new_window.title(admin_tool_title)
    frame_setup = Frame(new_window)
    frame_setup.grid(row=0, column=0, columnspan=3, sticky="w", pady=10, padx=10)

    # Create Tkinter variables to track the state of the checkboxes
    checkbox1_var = IntVar()
    checkbox2_var = IntVar()

    entry_to_database = Entry(frame_setup)

    # Create checkbox widgets
    checkbox1_keepass = Checkbutton(frame_setup, text=variables.keepass_frame, variable=checkbox1_var, onvalue=1,
                                    offvalue=0)
    checkbox2_sms = Checkbutton(frame_setup, text=variables.sms_frame, variable=checkbox2_var, onvalue=1, offvalue=0)
    fetching_data(frame_setup)

    def is_valid_email(email):

        # Use the fullmatch() function to check if the email address matches the regular expression
        if re.fullmatch(email_regex, email):
            return True
        else:
            return False

    def new_email_adding():
        """
        Button Add engine
        :return:
        """
        entry_string = entry_to_database.get()

        if not is_valid_email(entry_string):
            error_setup(email_error_msg)
            return 0

        if not is_empty(entry_string):
            error_setup(smpty_string_msg)
            return 0
            # raise ValueError("String is empty")

        checkbox1_state_keepass = checkbox1_var.get()
        checkbox2_state_sms = checkbox2_var.get()

        if not any([checkbox1_state_keepass, checkbox2_state_sms]):
            error_setup(checkbox_msg)
            return 0
            # raise ValueError("No checkboxes selected")
        if checkbox1_state_keepass == 1:

            # Ищем строку с определенным ID
            cursor.execute("SELECT * FROM users WHERE keepass=?", (1,))
            row = cursor.fetchone()
            if bool(row):
                error_setup(keepass_msg)
                return 0
        if checkbox2_state_sms == 1:

            # Ищем строку с определенным ID
            cursor.execute("SELECT * FROM users WHERE sms=?", (1,))
            row = cursor.fetchone()
            if bool(row):
                error_setup(sms_msg)
                return 0
        entry_to_database.delete(0, END)
        checkbox1_keepass.deselect()
        checkbox2_sms.deselect()
        # Insert a row of data
        cursor.execute("INSERT INTO users (email, keepass, sms) VALUES (?, ?, ?)",
                       (entry_string, checkbox1_state_keepass, checkbox2_state_sms))

        # Commit the changes
        conn.commit()
        fetching_data(frame_setup)

    # Create Add button
    button_add = Button(new_window, text=add_email_button, command=new_email_adding)

    # Create a label widget and add it to the new window

    entry_to_database.grid(row=0, column=0, ipadx=entry_len, sticky="w")
    # Pack the checkbox widgets
    checkbox1_keepass.grid(row=0, column=1, sticky="w")
    checkbox2_sms.grid(row=0, column=2, sticky="w")
    button_add.grid(row=0, column=3, sticky="w")


def del_str(nr):
    # Delete a row with a specific id
    cursor.execute("DELETE FROM users WHERE id=?", (nr,))

    # Commit the changes
    conn.commit()
    fetching_data(frame_setup)


def fetching_data(frame_setup):
    # Select all rows from the table
    cursor.execute("SELECT * FROM users")

    # Fetch the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        mail = row[1]
        keepass_checkbox = row[2]
        sms_checkbox = row[3]

        # label_add_mail = Label(frame_setup, text=f"{entry_string}, {checkbox1_state_keepass}, {checkbox2_state_sms}")
        label_add_mail = Label(frame_setup, text=f"{mail}, KeePass - {keepass_checkbox}, SMS - {sms_checkbox}")
        label_add_mail.grid(row=row[0], column=0, sticky="w")
        xxx = Button(frame_setup, text="Del", command=lambda id=row[0]: del_str(id))
        xxx.grid(row=row[0], column=1)


"""
Создание экземпляра Butoon 
"""
button_setup = Button(frame_right_setup, text=setup_button, command=open_setup_window)
button_copy_to_alex = Button(frame_keepass, text=copy_to_keepass_button,
                             command=lambda: copy_to_clipboard(clipboard_keepass_text))
button_copy_to_sms = Button(frame_sms, text=copy_to_sms_button, command=lambda: copy_to_clipboard(clipboard_SMS_txt))

button_send_to_alex = Button(frame_keepass, text=send_to_alex_button,
                             command=lambda: send_mail(keepass[1], clipboard_keepass_text))
button_send_to_deniss = Button(frame_keepass, text=send_to_alex_deniss,
                             command=lambda: send_mail(mail_to_deniss, clipboard_keepass_text))
button_send_to_sms = Button(frame_sms, text=send_to_sms_button,
                            command=lambda: send_mail(sms[1], clipboard_SMS_txt))

button_enter = Button(frame_left_entries, text=enter_button, command=creating_user_text, underline=0)

button_delete = Button(frame_update, text=delete_all_button, command=del_text, underline=0)
style = Style()
style.map('TButton',
          foreground=[('!active', 'purple'),
                      ('pressed', 'orange'),
                      ('active', 'red')],
          background=[
              ('pressed', 'brown'),
              ('active', 'white')]
          )

# btn_delete.configure(background='red')

"""
Создание экземпляра Label 
"""
label_name = Label(frame_left_entries, text=label_first_name, width=12, anchor="w")
label_surname = Label(frame_left_entries, text=label_last_name, width=12, anchor="w")
label_ester = Label(frame_left_entries, text=label_ester_login, width=12, anchor="w")
label_ik = Label(frame_left_entries, text=label_personal_id, width=12, anchor="w")
label_phone = Label(frame_left_entries, text=label_phone_number, width=12, anchor="w")
label_info = Label(frame_left_entries, text=label_additional_info, width=12, anchor="w")
label_tht_kood = Label(frame_left_entries, text=label_tht_code, width=12, anchor="w")
label_arvuti_login_upd = Label(frame_update, text=label_arvuti_login_upd_a, width=12, anchor="w")
label_arvuti_pass_upd = Label(frame_update, text=label_arvuti_pass_upd_a, width=12, anchor="w")
label_ester_pass_upd = Label(frame_update, text=label_ester_pass_upd_a, width=12, anchor="w")
label_zimbra_mail_upd = Label(frame_update, text=label_zimbra_mail_upd_a, width=12, anchor="w")
label_zimbra_pass_upd = Label(frame_update, text=label_zimbra_pass_upd_a, width=12, anchor="w")

"""
Создание экземпляра Text 
"""
text_text = Text(frame_keepass, width=text_width, height=text_height)
text_SMS = Text(frame_sms, width=text_width, height=text_text_height)

"""
Создание экземпляра Entry 
"""
entry_name = Entry(frame_left_entries)
# ent_name.icursor(5)
entry_name.focus()
entry_surname = Entry(frame_left_entries)
entry_ester = Entry(frame_left_entries)
entry_personal_id = Entry(frame_left_entries)
entry_tht_code = Entry(frame_left_entries)
entry_phone = Entry(frame_left_entries)
entry_info = Entry(frame_left_entries)
entry_pc_login_upd = Entry(frame_update)
entry_arvuti_pass_upd = Entry(frame_update)
entry_ester_pass_upd = Entry(frame_update)
entry_zimbra_mail_upd = Entry(frame_update)
entry_zimbra_pass_upd = Entry(frame_update)


def keepass_fob_db():
    global keepass, sms, entry_alex, entry_SMS
    # Ищем строку с определенным ID
    try:
        cursor.execute("SELECT * FROM users WHERE keepass=?", (1,))
        keepass = cursor.fetchone()
        cursor.execute("SELECT * FROM users WHERE sms=?", (1,))
        sms = cursor.fetchone()
    except Exception as e:
        print(f"Error retrieving data from the database: {e}")
    if keepass or sms:
        entry_alex = Label(frame_keepass, text=keepass[1])
        entry_SMS = Label(frame_sms, text=sms[1])
    else:
        entry_alex = Label(frame_keepass, text="None")
        entry_SMS = Label(frame_sms, text="None")


keepass_fob_db()


# DEMO info
# entry_name.insert(END, 'deniss')
# entry_surname.insert(END, 'hohlov')
# entry_ester.insert(END, 'a7272')
# entry_personal_id.insert(END, '38410103729')
# entry_tht_code.insert(END, 'd00077')
# entry_phone.insert(END, '55944212')
# entry_info.insert(END, 'it-mees')


#

# lb_name_print.grid(row=9, column=3)

def left_frame():
    """
    Left frame
    """
    frame_left_entries.grid(row=0, column=0, columnspan=3, sticky="w", pady=10, padx=10)
    labels = [label_name, label_surname, label_ester, label_ik, label_tht_kood, label_phone, label_info]
    entries = [entry_name, entry_surname, entry_ester, entry_personal_id, entry_tht_code, entry_phone, entry_info]
    # Labels printing
    for i, label in enumerate(labels):
        label.grid(row=i, column=0, pady=2)
    # Entries printing
    for i, entry in enumerate(entries):
        entry.grid(row=i, column=1, sticky="w", ipadx=entry_len)
    button_enter.grid(row=7, column=1, ipadx=15, ipady=5, pady=10)
    button_delete.grid(row=5, column=0, padx=10, sticky="nw", pady=10)


def update_frame():
    """
    Frame for additional information for old employ
    :return:
    """
    frame_update.grid(row=0, column=1, columnspan=3, sticky="ne", pady=10, padx=10)

    label_arvuti_login_upd.grid(row=0, column=0, sticky="w")
    label_arvuti_pass_upd.grid(row=1, column=0, sticky="w")
    label_ester_pass_upd.grid(row=2, column=0, sticky="w")
    label_zimbra_mail_upd.grid(row=3, column=0, sticky="w")
    label_zimbra_pass_upd.grid(row=4, column=0, sticky="w")

    entry_pc_login_upd.grid(row=0, column=1, sticky="w")
    entry_arvuti_pass_upd.grid(row=1, column=1, sticky="w")
    entry_ester_pass_upd.grid(row=2, column=1, sticky="w")
    entry_zimbra_mail_upd.grid(row=3, column=1, sticky="w")
    entry_zimbra_pass_upd.grid(row=4, column=1, sticky="w")


def fight_frame():
    """
    Right frame
    """
    frame_right_setup.grid(row=0, column=2)
    # button_setup.grid(row=0, column=0)


def keepass_frame():
    """
    To Alex
    """
    frame_keepass.grid(row=4, column=0, columnspan=3, padx=10)
    text_text.grid(row=0, column=0, rowspan=11, sticky="we")
    button_copy_to_alex.grid(row=0, column=1, ipadx=10, ipady=5, sticky="we")
    button_send_to_alex.grid(row=1, column=1, ipadx=10, ipady=5, sticky="we")
    entry_alex.grid(row=2, column=1, sticky="we", padx=10)
    button_send_to_deniss.grid(row=3, column=1, ipadx=10, ipady=5, sticky="we")


def sms_frame():
    """
    SMS frame content
    """
    frame_sms.grid(row=9, column=0, columnspan=3, pady=10)
    text_SMS.grid(row=0, column=0, rowspan=6, sticky="we")
    button_send_to_sms.grid(row=1, column=1, ipadx=10, ipady=5, sticky="we")
    button_copy_to_sms.grid(row=0, column=1, ipadx=10, ipady=5, sticky="we")
    entry_SMS.grid(row=2, column=1, padx=10, sticky="we")


left_frame()
fight_frame()
keepass_frame()
sms_frame()
update_frame()


def copy_to_clipboard(clipboard_text, *event):
    """
    Clipboard engine
    :param clipboard_text:
    :param event: short key
    :return:
    """
    root.clipboard_clear()
    root.clipboard_append(clipboard_text)


def show_menu_bar(*event):
    menu_bar.pack(side="top", fill="x")


# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Setup", command=open_setup_window, accelerator="Ctrl+F")
# file_menu.add_command(label="Save", command=some_callback_function)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
root.bind('<Control-f>', open_setup_window)
# root.bind_all("<Control-m>", show_menu_bar)
# Set the menu bar as the window menu
root.config(menu=menu_bar)
# conn.close()
root.mainloop()
