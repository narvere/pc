from tkinter import Tk, END, Text, Label, Frame, LabelFrame, Toplevel
from tkinter.ttk import Entry, Button, Style
from pass_gen import pass_gen, eesti_speller
from good import send_mail
import tkinter.messagebox as messagebox

root = Tk()
root.geometry("630x600+700+300")
root.resizable(width=False, height=False)
root.title("Narva Haigla tool by Deniss Hohlov")
nimi = "Nimi: "
perekonnanimi = "Perekonnanimi: "
ester = "Ester login: "
ik = "Isikukood: "
tel = "Telefon: "
info = "Info: "
tht = "THT code: "
pc_login = "Arvuti login: "
pc_pass = "Arvuti pass: "
ester_pass = "Ester pass: "
zimbra = "Zimbra: "
zimbra_pass = "Zimbra pass: "
text_width = 50
text_height = 11
# mail_to_alex = "deniss.hohlov@narvahaigla.ee"
mail_to_alex = "alexey.bystrov@narvahaigla.ee"
mail_to_sms = "deniss.hohlov@narvahaigla.ee"
ent_len = 40


def string_check(string):
    if not string.isalpha():
        messagebox.showerror("Error", f"{nimi}или {perekonnanimi}- cодержат ошибку!")
        return 0


def numeric_check(string):
    if not string.isnumeric() or len(string) != 11:
        print(string)
        messagebox.showerror("Error", f"{ik}- cодержит ошибку!")
        return 0


def login_tht_check(string):
    if not string.isalnum():
        messagebox.showerror("Error", f"{ester}или {tht}- cодержат ошибку!")
        return 0


def checking_emty_string(string):
    if not bool(string):
        messagebox.showerror("Error", f"{info}или {tel}- пустые!")
        return 0


def del_text(*event):
    txt_text.delete(1.0, END)
    txt_textSMS.delete(1.0, END)
    ent_name.delete(0, END)
    ent_surname.delete(0, END)
    ent_ester.delete(0, END)
    ent_ik.delete(0, END)
    ent_tht_kood.delete(0, END)
    ent_tel.delete(0, END)
    ent_info.delete(0, END)


def get_text(*event):
    if string_check(ent_name.get()) != 0 or string_check(ent_surname.get()) != 0:
        if numeric_check(ent_ik.get()) != 0:
            if login_tht_check(ent_ester.get()) != 0 and login_tht_check(ent_tht_kood.get()) != 0:
                if checking_emty_string(ent_info.get()) != 0 and checking_emty_string(ent_tel.get()) != 0:
                    global clipboard_text, clipboard_SMS
                    dc_pass, heda_pass, password = pass_gen()
                    name_s = eesti_speller(ent_name.get().strip().lower().title())
                    surname_s = eesti_speller(ent_surname.get().strip().lower().title())
                    name = ent_name.get().strip().lower().title()
                    surname = ent_surname.get().strip().lower().title()
                    zimbra_mail = name_s.lower() + "." + surname_s.lower() + "@narvahaigla.ee"
                    dc_login = ent_ester.get()[1:].strip().lower().title()
                    # name_print["text"] = nimi + name + " " + surname + '\n'
                    clipboard_SMS = f"{pc_login}{dc_login}\n{pc_pass}{dc_pass}\n{ester}{ent_ester.get()}\n" \
                                    f"{ester_pass}{heda_pass}\n{zimbra}{zimbra_mail}\n{zimbra_pass}{password}"
                    clipboard_text = f"{nimi}{name} {surname} / {name_s} {surname_s} \n{clipboard_SMS}\n{ik}{ent_ik.get()}\n{tht}{ent_tht_kood.get()}\n" \
                                     f"{tel}{ent_tel.get()}\n{info}{ent_info.get()}"

                    # print(clipboard_text)

                    # name_ent.delete(0, END)
                    txt_text.delete(1.0, END)
                    txt_text.insert(index=1.0,
                                    chars=nimi + name_s + " " + surname_s + " " + '/' + " " + name + " " + surname + '\n')
                    # text.insert(index=1.0, chars=nimi + name_ent.get() + '\n')
                    txt_text.insert(index=2.0, chars=pc_login + dc_login + '\n')
                    txt_text.insert(index=3.0, chars=pc_pass + dc_pass + '\n')
                    txt_text.insert(index=4.0, chars=ester + ent_ester.get().strip() + '\n')
                    txt_text.insert(index=5.0, chars=ester_pass + heda_pass + '\n')
                    txt_text.insert(index=6.0, chars=zimbra + zimbra_mail + '\n')
                    txt_text.insert(index=7.0, chars=zimbra_pass + password + '\n')
                    txt_text.insert(index=8.0, chars=ik + ent_ik.get().strip() + '\n')
                    txt_text.insert(index=9.0, chars=tht + ent_tht_kood.get().strip() + '\n')
                    txt_text.insert(index=10.0, chars=tel + ent_tel.get().strip() + '\n')
                    txt_text.insert(index=11.0, chars=info + ent_info.get().strip())

                    txt_textSMS.delete(1.0, END)
                    txt_textSMS.insert(index=1.0, chars=pc_login + dc_login + '\n')
                    txt_textSMS.insert(index=2.0, chars=pc_pass + dc_pass + '\n')
                    txt_textSMS.insert(index=3.0, chars=ester + ent_ester.get() + '\n')
                    txt_textSMS.insert(index=4.0, chars=ester_pass + heda_pass + '\n')
                    txt_textSMS.insert(index=5.0, chars=zimbra + name_s.lower() + "." + surname_s.lower() + '\n')
                    txt_textSMS.insert(index=6.0, chars=zimbra_pass + password + '\n')
                    # return clipbloard_text


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
fr_frame = LabelFrame(root, text="To Alex", bg='grey')
fr_frameSMS = LabelFrame(root, text="SMS", bg='yellow')
fr_left = Frame(root, bg='green')
fr_right = Frame(root, bg='black')
def open_new_window():
    # Create the new window
    new_window = Toplevel(root)

    # Create a label widget and add it to the new window
    label = Label(new_window, text='This is a new window')
    label.pack()
"""
Создание экземпляра Butoon 
"""
btn_setup = Button(fr_right, text="Setup", command=open_new_window)
btn_cta = Button(fr_frame, text='Copy to Alex', command=lambda: gtc(clipboard_text))
btn_cts = Button(fr_frameSMS, text='Copy to SMS', command=lambda: gtc(clipboard_SMS))

btn_sta = Button(fr_frame, text='Send to Alex',
                 command=lambda: send_mail(mail_to_alex, clipboard_text))
btn_sts = Button(fr_frameSMS, text='Send to SMS',
                 command=lambda: send_mail(mail_to_sms, clipboard_text))
# except Exception as ex:
#     show_error(ex)

btn_enter = Button(fr_left, text="Enter", command=get_text, underline=0)

btn_delete = Button(fr_left, text="Delete all", command=del_text, underline=0)
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
lb_name = Label(fr_left, text=nimi, width=12, anchor="w")
lb_surname = Label(fr_left, text=perekonnanimi, width=12, anchor="w")
lb_ester = Label(fr_left, text=ester, width=12, anchor="w")
lb_ik = Label(fr_left, text=ik, width=12, anchor="w")
lb_tel = Label(fr_left, text=tel, width=12, anchor="w")
lb_info = Label(fr_left, text=info, width=12, anchor="w")
lb_tht_kood = Label(fr_left, text=tht, width=12, anchor="w")
lb_name_print = Label(fr_left)

"""
Создание экземпляра Text 
"""
txt_text = Text(fr_frame, width=text_width, height=text_height)
txt_textSMS = Text(fr_frameSMS, width=text_width, height=6)

"""
Создание экземпляра Entry 
"""
ent_name = Entry(fr_left)
# ent_name.icursor(5)
ent_name.focus()
ent_surname = Entry(fr_left)
ent_ester = Entry(fr_left)
ent_ik = Entry(fr_left)
ent_tht_kood = Entry(fr_left)
ent_tel = Entry(fr_left)
ent_info = Entry(fr_left)
ent_alex = Entry(fr_frame, width=30)
ent_alex.insert(END, 'deniss.hohlov@gmail.com')
ent_SMS = Entry(fr_frameSMS, width=30)
ent_SMS.insert(END, 'deniss.hohlov@gmail.com')

lb_name_print.grid(row=9, column=3)

"""
Left frame
"""
fr_left.grid(row=0, column=0, columnspan=3, sticky="w", pady=10)

lb_name.grid(row=0, column=0, padx=10, pady=2)
lb_surname.grid(row=1, column=0, pady=2)
lb_ester.grid(row=2, column=0, pady=2)
lb_ik.grid(row=3, column=0, pady=2)
lb_tht_kood.grid(row=4, column=0, pady=2)
lb_tel.grid(row=5, column=0, pady=2)
lb_info.grid(row=6, column=0, pady=2)

ent_name.grid(row=0, column=1, sticky="w", ipadx=ent_len)
ent_surname.grid(row=1, column=1, sticky="w", ipadx=ent_len)
ent_ester.grid(row=2, column=1, sticky="w", ipadx=ent_len)
ent_ik.grid(row=3, column=1, sticky="w", ipadx=ent_len)
ent_tht_kood.grid(row=4, column=1, sticky="w", ipadx=ent_len)
ent_tel.grid(row=5, column=1, sticky="w", ipadx=ent_len)
ent_info.grid(row=6, column=1, sticky="w", ipadx=ent_len)

btn_enter.grid(row=7, column=1, ipadx=15, ipady=5, pady=10)
btn_delete.grid(row=0, column=2, padx=10)

"""
Right frame
"""
fr_right.grid(row=0, column=2)
btn_setup.grid(row=0, column=0)


"""
To Alex
"""
fr_frame.grid(row=4, column=0, columnspan=3, padx=10)
txt_text.grid(row=0, column=0, rowspan=11)
btn_sta.grid(row=0, column=1, ipadx=10, ipady=5, sticky="n")
btn_cta.grid(row=1, column=1, ipadx=10, ipady=5, sticky="n")
ent_alex.grid(row=2, column=1, sticky="n", padx=10)

"""
SMS frame content
"""
fr_frameSMS.grid(row=9, column=0, columnspan=3)
txt_textSMS.grid(row=0, column=0, rowspan=6)
btn_sts.grid(row=0, column=1, ipadx=10, ipady=5)
btn_cts.grid(row=1, column=1, ipadx=10, ipady=5)
ent_SMS.grid(row=2, column=1, padx=10)


def gtc(dtxt, *event):
    root.clipboard_clear()
    root.clipboard_append(dtxt)


root.mainloop()
