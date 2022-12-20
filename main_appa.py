from tkinter import Tk, END, Text, Label
from tkinter.ttk import Entry, Button, LabelFrame, Frame, Style
from pass_gen import pass_gen, eesti_speller
from good import send_mail

root = Tk()
root.geometry("600x530+700+300")
root.resizable(width=False, height=False)
root.title("Narva Haigla tool by Deniss Hohlov")
nimi = "Nimi: "
perekonnanimi = "Perekonnanimi: "
ester = "Ester login: "
ik = "Isikukood: "
tel = "Telefon: "
info = "Info: "
pc_login = "Arvuti login: "
pc_pass = "Arvuti pass: "
ester_pass = "Ester pass: "
zimbra = "Zimbra: "
zimbra_pass = "Zimbra pass: "
text_width = 50
text_height = 10


def del_text(*event):
    txt_text.delete(1.0, END)
    txt_textSMS.delete(1.0, END)
    ent_name.delete(0, END)
    ent_surname.delete(0, END)
    ent_ester.delete(0, END)
    ent_ik.delete(0, END)
    ent_tel.delete(0, END)
    ent_info.delete(0, END)


def get_text(*event):
    global clipboard_text, clipboard_SMS
    dc_pass, heda_pass, password = pass_gen()
    name = eesti_speller(ent_name.get().lower().title())
    surname = eesti_speller(ent_surname.get().lower().title())
    zimbra_mail = name.lower() + "." + surname.lower() + "@narvahaigla.ee"
    dc_login = ent_ester.get()[1:].strip().lower().title()
    # name_print["text"] = nimi + name + " " + surname + '\n'
    clipboard_SMS = f"{pc_login}{dc_login}\n{pc_pass}{dc_pass}\n{ester}{ent_ester.get()}\n" \
                    f"{ester_pass}{heda_pass}\n{zimbra}{zimbra_mail}\n{zimbra_pass}{password}"
    clipboard_text = f"{nimi}{name} {surname}\n{clipboard_SMS}\n{ik}{ent_ik.get()}\n" \
                     f"{tel}{ent_tel.get()}\n{info}{ent_info.get()}"

    # print(clipboard_text)

    # name_ent.delete(0, END)
    txt_text.delete(1.0, END)
    txt_text.insert(index=1.0, chars=nimi + name + " " + surname + '\n')
    # text.insert(index=1.0, chars=nimi + name_ent.get() + '\n')
    txt_text.insert(index=2.0, chars=pc_login + dc_login + '\n')
    txt_text.insert(index=3.0, chars=pc_pass + dc_pass + '\n')
    txt_text.insert(index=4.0, chars=ester + ent_ester.get() + '\n')
    txt_text.insert(index=5.0, chars=ester_pass + heda_pass + '\n')
    txt_text.insert(index=6.0, chars=zimbra + zimbra_mail + '\n')
    txt_text.insert(index=7.0, chars=zimbra_pass + password + '\n')
    txt_text.insert(index=8.0, chars=ik + ent_ik.get() + '\n')
    txt_text.insert(index=9.0, chars=tel + ent_tel.get() + '\n')
    txt_text.insert(index=10.0, chars=info + ent_info.get())

    txt_textSMS.delete(1.0, END)
    txt_textSMS.insert(index=1.0, chars=pc_login + dc_login + '\n')
    txt_textSMS.insert(index=2.0, chars=pc_pass + dc_pass + '\n')
    txt_textSMS.insert(index=3.0, chars=ester + ent_ester.get() + '\n')
    txt_textSMS.insert(index=4.0, chars=ester_pass + heda_pass + '\n')
    txt_textSMS.insert(index=5.0, chars=zimbra + name.lower() + "." + surname.lower() + '\n')
    txt_textSMS.insert(index=6.0, chars=zimbra_pass + password + '\n')
    # return clipbloard_text


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
fr_frame = LabelFrame(root, text="To Alex")
fr_frameSMS = LabelFrame(root, text="SMS")
fr_first = Frame(root)

"""
Создание экземпляра Butoon 
"""
btn_cta = Button(fr_frame, text='Copy to Alex', command=lambda: gtc(clipboard_text))
btn_cts = Button(fr_frameSMS, text='Copy to SMS', command=lambda: gtc(clipboard_SMS))
btn_sta = Button(fr_frame, text='Send to Alex',
                 command=lambda: send_mail('deniss.hohlov@narvahaigla.ee', clipboard_text))
btn_sts = Button(fr_frameSMS, text='Send to SMS',
                 command=lambda: send_mail('deniss.hohlov@narvahaigla.ee', clipboard_text))

btn_enter = Button(fr_first, text="Enter", command=get_text, underline=0)

btn_delete = Button(fr_first, text="Delete", command=del_text, underline=0)
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
lb_name = Label(fr_first, text=nimi, width=12, anchor="w")
lb_surname = Label(fr_first, text=perekonnanimi, width=12, anchor="w")
lb_ester = Label(fr_first, text=ester, width=12, anchor="w")
lb_ik = Label(fr_first, text=ik, width=12, anchor="w")
lb_tel = Label(fr_first, text=tel, width=12, anchor="w")
lb_info = Label(fr_first, text=info, width=12, anchor="w")
lb_name_print = Label(fr_first)

"""
Создание экземпляра Text 
"""
txt_text = Text(fr_frame, width=text_width, height=text_height)
txt_textSMS = Text(fr_frameSMS, width=text_width, height=6)

"""
Создание экземпляра Entry 
"""
ent_name = Entry(fr_first)
ent_name.icursor(5)
ent_name.focus()

ent_surname = Entry(fr_first)
ent_ester = Entry(fr_first)
ent_ik = Entry(fr_first)
ent_tel = Entry(fr_first)
ent_info = Entry(fr_first)
ent_alex = Entry(fr_frame, width=30)
ent_alex.insert(END, 'deniss.hohlov@gmail.com')
ent_SMS = Entry(fr_frameSMS, width=30)
ent_SMS.insert(END, 'deniss.hohlov@gmail.com')

lb_name_print.grid(row=9, column=3)

"""
First frame
"""
fr_first.grid(row=0, column=0, columnspan=3, sticky="w")

lb_name.grid(row=0, column=0)
lb_surname.grid(row=1, column=0)
lb_ester.grid(row=2, column=0)
lb_ik.grid(row=3, column=0)
lb_tel.grid(row=4, column=0)
lb_info.grid(row=5, column=0)

ent_name.grid(row=0, column=1, sticky="w")
ent_surname.grid(row=1, column=1, sticky="w")
ent_ester.grid(row=2, column=1, sticky="w")
ent_ik.grid(row=3, column=1, sticky="w")
ent_tel.grid(row=4, column=1, sticky="w")
ent_info.grid(row=5, column=1, sticky="w")

btn_enter.grid(row=6, column=0, ipadx=10, ipady=5)
btn_delete.grid(row=6, column=1, ipadx=10, ipady=5)

"""
To Alex
"""
fr_frame.grid(row=4, column=0, columnspan=3)
txt_text.grid(row=0, column=0, rowspan=10)
btn_sta.grid(row=0, column=1, ipadx=10, ipady=5, sticky="n")
btn_cta.grid(row=1, column=1, ipadx=10, ipady=5, sticky="n")
ent_alex.grid(row=2, column=1, sticky="n")

"""
SMS frame content
"""
fr_frameSMS.grid(row=9, column=0, columnspan=3)
txt_textSMS.grid(row=0, column=0, rowspan=6)
btn_sts.grid(row=0, column=1, ipadx=10, ipady=5)
btn_cts.grid(row=1, column=1, ipadx=10, ipady=5)
ent_SMS.grid(row=2, column=1)


def gtc(dtxt, *event):
    root.clipboard_clear()
    root.clipboard_append(dtxt)


root.mainloop()
