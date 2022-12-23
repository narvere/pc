from tkinter import Tk, END, Text, Label, Frame, LabelFrame, Toplevel, IntVar, Checkbutton
from tkinter.ttk import Entry, Button, Style
from pass_gen import pass_gen, eesti_speller
from good import send_mail
import tkinter.messagebox as messagebox

root = Tk()
root.geometry("630x600+700+300")
root.resizable(width=False, height=False)
root.title("Narva Haigla tool by Deniss Hohlov")

# Mailing and SMS configurations
mail_to_alex = "alexey.bystrov@narvahaigla.ee"
mail_to_sms = "deniss.hohlov@narvahaigla.ee"

# Constants for input fields
label_first_name = "Nimi: "
label_last_name = "Perekonnanimi: "
label_ester_login = "Ester login: "
label_personal_id = "Isikukood: "
label_phone_number = "Telefon: "
label_additional_info = "Info: "
label_tht_code = "THT code: "
label_pc_login = "Arvuti login: "
label_pc_pass = "Arvuti pass: "
label_ester_pass = "Ester pass: "
label_zimbra_mail = "Zimbra: "
label_zimbra_pass = "Zimbra pass: "
text_width = 50
text_height = 11
enttry_len = 40


# Validation functions
def is_alpha(string):
    return string.isalpha()


def is_numeric(string):
    return string.isnumeric() and len(string) == 11


def is_alnum(string):
    return string.isalnum()


def is_empty(string):
    return bool(string)


# Other functions
def string_check(string):
    if not is_alpha(string.strip()):
        messagebox.showerror("Error", f"{label_first_name}или {label_last_name}- cодержат ошибку!")
        return 0


def numeric_check(string):
    if not is_numeric(string):
        messagebox.showerror("Error", f"{label_personal_id}- cодержит ошибку!")
        return 0


def login_tht_check(string):
    if not is_alnum(string):
        messagebox.showerror("Error", f"{label_ester_login}или {label_tht_code}- cодержат ошибку!")
        return 0


def checking_emty_string(string):
    if not is_empty(string):
        messagebox.showerror("Error", f"{label_additional_info}или {label_phone_number}- пустые!")
        return 0


def checking_emty_string2(string):
    if not is_empty(string):
        messagebox.showerror("Error", f"Адрес не введен!")
        return 0


def del_text(*event):
    text_text.delete(1.0, END)
    text_SMS.delete(1.0, END)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_ester.delete(0, END)
    entry_personal_id.delete(0, END)
    entry_tht_code.delete(0, END)
    entry_phone.delete(0, END)
    entry_info.delete(0, END)


def get_text(*event):
    if not string_check(entry_name.get()) and not string_check(entry_surname.get()):
        if not numeric_check(entry_personal_id.get()):
            if not login_tht_check(entry_ester.get()):
                if not checking_emty_string(entry_info.get()) and not checking_emty_string(entry_phone.get()):
                    global clipboard_text, clipboard_SMS_txt
                    additional_info, ester_login, ester_pass, first_name, first_name_speller, last_name_speller, \
                        last_surname, pc_login, pc_pass, personal_id, phone_number, tht_code, zimbra_mail, \
                        zimbra_pass = generate_message_variables()
                    clipboard_SMS_txt = f"{label_pc_login}{pc_login}\n{label_pc_pass}{pc_pass}\n{label_ester_login}{ester_login}\n" \
                                        f"{label_ester_pass}{ester_pass}\n{label_zimbra_mail}{zimbra_mail}\n{label_zimbra_pass}{zimbra_pass} "
                    clipboard_text = f"{label_first_name}{first_name} {last_surname} / {first_name_speller} {last_name_speller} " \
                                     f"\n{clipboard_SMS_txt}\n{label_personal_id}{personal_id}\n{label_tht_code}{tht_code}\n" \
                                     f"{label_phone_number}{phone_number}\n{label_additional_info}{additional_info}"

                    print_alex_method(ester_pass, first_name, first_name_speller, last_name_speller, last_surname,
                                      pc_login, pc_pass, zimbra_mail, zimbra_pass)

                    print_sms_method(ester_pass, first_name_speller, last_name_speller, pc_login, pc_pass, zimbra_pass)


def print_sms_method(ester_pass, first_name_spelling, last_name_spelling, pc_login, pc_pass, zimbra_pass):
    # Clear txt_textSMS widget
    text_SMS.delete(1.0, END)

    # Insert text into txt_textSMS widget
    pc_login_text = f"{label_pc_login}{pc_login}\n"
    pc_pass_text = f"{label_pc_pass}{pc_pass}\n"
    ester_login_text = f"{label_ester_login}{entry_ester.get()}\n"
    ester_pass_text = f"{label_ester_pass}{ester_pass}\n"
    zimbra_mail_text = f"{label_zimbra_mail}{first_name_spelling.lower()}.{last_name_spelling.lower()}\n"
    zimbra_pass_text = f"{label_zimbra_pass}{zimbra_pass}\n"

    text_SMS.insert(index=1.0, chars=pc_login_text)
    text_SMS.insert(index=2.0, chars=pc_pass_text)
    text_SMS.insert(index=3.0, chars=ester_login_text)
    text_SMS.insert(index=4.0, chars=ester_pass_text)
    text_SMS.insert(index=5.0, chars=zimbra_mail_text)
    text_SMS.insert(index=6.0, chars=zimbra_pass_text)


def print_alex_method(ester_pass, first_name, first_name_spelling, last_name_spelling, last_surname, pc_login, pc_pass,
                      zimbra_mail, zimbra_pass):
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
    # Generate passwords
    pc_pass, ester_pass, zimbra_pass = pass_gen()

    # Generate spelling of first and last names

    first_name_spelling = eesti_speller(entry_name.get().strip().lower().title())
    last_name_spelling = eesti_speller(entry_surname.get().strip().lower().title())

    # Extract first and last names
    first_name = entry_name.get().strip().lower().title()
    last_surname = entry_surname.get().strip().lower().title()

    # Generate Zimbra email address
    zimbra_mail = f"{first_name_spelling.lower()}.{last_name_spelling.lower()}@narvahaigla.ee"

    # Generate PC login
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
    # name_print["text"] = nimi + first_name + " " + last_surname + '\n'
    return additional_info, ester_login, ester_pass, first_name, first_name_spelling, last_name_spelling, last_surname, \
        pc_login, pc_pass, personal_id, phone_number, tht_code, zimbra_mail, zimbra_pass


def show_error(ex):
    messagebox.showerror("Error", ex)


"""
Созданте горячих клавиш
"""

root.bind('<Control-e>', get_text)
root.bind('<Control-d>', del_text)
# root.bind('<Control-a>', lambda: gtc(clipboard_text))
# root.bind('<Control-s>', lambda: gtc(clipboard_SMS))
"""
Создание экземпляра Frame и LabelFrame 
"""
frame_alex = LabelFrame(root, text="To Alex")
frame_sms = LabelFrame(root, text="SMS")
frame_left_entries = Frame(root)
frame_right_setup = Frame(root)


def open_new_window():
    # Create the new window
    new_window = Toplevel(root)
    new_window.geometry("500x250")

    # Create Tkinter variables to track the state of the checkboxes
    checkbox1_var = IntVar()
    checkbox2_var = IntVar()

    entry_to_database = Entry(new_window)
    # mm = entry_to_database.get()
    # Create checkbox widgets
    checkbox1 = Checkbutton(new_window, text="Keepass", variable=checkbox1_var, onvalue=1, offvalue=0)
    checkbox2 = Checkbutton(new_window, text="SMS", variable=checkbox2_var, onvalue=1, offvalue=0)

    # Define callback functions to print the state of the checkboxes
    def print_checkbox_state(checkbox_var, checkbox_num):
        return checkbox_var, checkbox_num
        # print(f"Keepass {checkbox_num} SMS: {checkbox_var.get()}")

        # printing()
        # print(entry_to_database.get())

    def process_inputs():
        entry_string = entry_to_database.get()
        if not is_empty(entry_string):
            raise ValueError("String is empty")

        checkbox1_state = checkbox1_var.get()
        checkbox2_state = checkbox2_var.get()
        if not any([checkbox1_state, checkbox2_state]):
            raise ValueError("No checkboxes selected")
        label_add_mail = Label(new_window, text=f"{entry_string}, {checkbox1_state}, {checkbox2_state}")
        label_add_mail.grid(row=1, column=0, sticky="w")
        entry_to_database.delete(0, END)
        checkbox1.deselect()
        print(entry_string, checkbox1_state, checkbox2_state)

    # Create Add button
    button_add = Button(new_window, text="Add", command=process_inputs)

    # Create a label widget and add it to the new window

    entry_to_database.grid(row=0, column=0, ipadx=enttry_len)
    # Pack the checkbox widgets
    checkbox1.grid(row=0, column=1)
    checkbox2.grid(row=0, column=2)
    button_add.grid(row=0, column=3)


"""
Создание экземпляра Butoon 
"""
button_setup = Button(frame_right_setup, text="Setup", command=open_new_window)
button_copy_to_alex = Button(frame_alex, text='Copy to Alex', command=lambda: gtc(clipboard_text))
button_copy_to_sms = Button(frame_sms, text='Copy to SMS', command=lambda: gtc(clipboard_SMS_txt))

button_send_to_alex = Button(frame_alex, text='Send to Alex',
                             command=lambda: send_mail(mail_to_alex, clipboard_text))
button_send_to_sms = Button(frame_sms, text='Send to SMS',
                            command=lambda: send_mail(mail_to_sms, clipboard_text))
# except Exception as ex:
#     show_error(ex)

button_enter = Button(frame_left_entries, text="Enter", command=get_text, underline=0)

button_delete = Button(frame_left_entries, text="Delete all", command=del_text, underline=0)
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

"""
Создание экземпляра Text 
"""
text_text = Text(frame_alex, width=text_width, height=text_height)
text_SMS = Text(frame_sms, width=text_width, height=6)

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
entry_alex = Entry(frame_alex, width=30)
entry_alex.insert(END, 'deniss.hohlov@gmail.com')
entry_SMS = Entry(frame_sms, width=30)
entry_SMS.insert(END, 'deniss.hohlov@gmail.com')

# lb_name_print.grid(row=9, column=3)

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
    entry.grid(row=i, column=1, sticky="w", ipadx=enttry_len)

button_enter.grid(row=7, column=1, ipadx=15, ipady=5, pady=10)
button_delete.grid(row=0, column=2, padx=10)

"""
Right frame
"""
frame_right_setup.grid(row=0, column=2)
button_setup.grid(row=0, column=0)

"""
To Alex
"""
frame_alex.grid(row=4, column=0, columnspan=3, padx=10)
text_text.grid(row=0, column=0, rowspan=11, sticky="we")
button_send_to_alex.grid(row=0, column=1, ipadx=10, ipady=5, sticky="we")
button_copy_to_alex.grid(row=1, column=1, ipadx=10, ipady=5, sticky="we")
entry_alex.grid(row=2, column=1, sticky="we", padx=10)

"""
SMS frame content
"""
frame_sms.grid(row=9, column=0, columnspan=3, pady=10)
text_SMS.grid(row=0, column=0, rowspan=6, sticky="we")
button_send_to_sms.grid(row=0, column=1, ipadx=10, ipady=5, sticky="we")
button_copy_to_sms.grid(row=1, column=1, ipadx=10, ipady=5, sticky="we")
entry_SMS.grid(row=2, column=1, padx=10, sticky="we")


def gtc(dtxt, *event):
    root.clipboard_clear()
    root.clipboard_append(dtxt)


root.mainloop()
