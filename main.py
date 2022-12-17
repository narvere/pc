from tkinter import Tk, Label, Entry, Button, END, Frame, Text, LabelFrame
from pass_gen import pass_gen, eesti_speller

root = Tk()
root.geometry("700x500+700+300")
root.resizable(width=False, height=False)
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





def get_text():
    dc_pass, heda_pass, password = pass_gen()
    name = eesti_speller(name_ent.get().lower().title())
    surname = eesti_speller(surname_ent.get().lower().title())
    zimbra_mail = name.lower() + "." + surname.lower() + "@narvahaigla.ee"
    dc_login = ester_ent.get()[1:].strip().lower().title()
    # name_print["text"] = name_ent.get()
    # name_ent.delete(0, END)
    text.delete(1.0, END)
    text.insert(index=1.0, chars=nimi + name + " " + surname + '\n')
    # text.insert(index=1.0, chars=nimi + name_ent.get() + '\n')
    text.insert(index=2.0, chars=pc_login + dc_login + '\n')
    text.insert(index=3.0, chars=pc_pass + dc_pass + '\n')
    text.insert(index=4.0, chars=ester + ester_ent.get() + '\n')
    text.insert(index=5.0, chars=ester_pass + heda_pass + '\n')
    text.insert(index=6.0, chars=zimbra + zimbra_mail + '\n')
    text.insert(index=7.0, chars=zimbra_pass + password + '\n')
    text.insert(index=8.0, chars=ik + ik_ent.get() + '\n')
    text.insert(index=9.0, chars=tel + tel_ent.get() + '\n')
    text.insert(index=10.0, chars=info + info_ent.get())

    textSMS.delete(1.0, END)
    textSMS.insert(index=1.0, chars=pc_login + dc_login + '\n')
    textSMS.insert(index=2.0, chars=pc_pass + dc_pass + '\n')
    textSMS.insert(index=3.0, chars=ester + ester_ent.get() + '\n')
    textSMS.insert(index=4.0, chars=ester_pass + heda_pass + '\n')
    textSMS.insert(index=5.0, chars=zimbra + name.lower() + "." + surname.lower() + '\n')
    textSMS.insert(index=6.0, chars=zimbra_pass + password + '\n')

# xxx = f"{nimi} + {name} + " " + surname + '\n'"
# Button(text='age', command=lambda: gtc(xxx)).grid(column=2, row=8)


frame = LabelFrame(root, text="To Alex")
frame.grid(row=8, column=0, columnspan=2, pady=5, padx=20)
frameSMS = LabelFrame(root, text="SMS")
frameSMS.grid(row=9, column=0, columnspan=2)

name_lb = Label(root, text=nimi)
surname_lb = Label(root, text=perekonnanimi)
ester_lb = Label(root, text=ester)
ik_lb = Label(root, text=ik)
tel_lb = Label(root, text=tel)
info_lb = Label(root, text=info)
# name_print = Label(root)

name_ent = Entry(root)
name_ent.icursor(5)
name_ent.focus()

surname_ent = Entry(root)
ester_ent = Entry(root)
ik_ent = Entry(root)
tel_ent = Entry(root)
info_ent = Entry(root)

enter_btn = Button(root, text="Enter", command=get_text)

name_lb.grid(row=0, column=0, sticky="e")
surname_lb.grid(row=1, column=0, sticky="e")
ester_lb.grid(row=2, column=0, sticky="e")
ik_lb.grid(row=3, column=0, sticky="e")
tel_lb.grid(row=4, column=0, sticky="e")
info_lb.grid(row=5, column=0, sticky="e")

name_ent.grid(row=0, column=1, sticky="w")
surname_ent.grid(row=1, column=1, sticky="w")
ester_ent.grid(row=2, column=1, sticky="w")
ik_ent.grid(row=3, column=1, sticky="w")
tel_ent.grid(row=4, column=1, sticky="w")
info_ent.grid(row=5, column=1, sticky="w")

enter_btn.grid(row=6, column=0, columnspan=2)
# name_print.grid(row=2, column=0)
# frame.grid(row=3, column=0)
text = Text(frame, width=text_width, height=text_height)
text.grid(row=7, column=0, columnspan=2)
# Label(frame, text="Test").grid(row=8, column=0)
textSMS = Text(frameSMS, width=text_width, height=6)
textSMS.grid(row=8, column=0, columnspan=2)


def gtc(dtxt):
    root.clipboard_clear()
    root.clipboard_append(dtxt)




root.mainloop()
