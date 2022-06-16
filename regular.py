from tkinter import *
from tkinter import Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re

file_name = None

root = Tk()
root.title("Регулярные выражения")
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
    
mainmenu = Menu(root)
root.config(menu=mainmenu)

def click_findall():
    list_result.delete(0, END)
    pattern = re.compile(ent_regex.get())
    result = pattern.findall(txt_edit.get('1.0', END))
    for i in result:
        list_result.insert(END, i)


def click_clear():
    list_result.delete(0, END)


def click_add():
    pattern = re.compile(ent_regex.get())
    result = pattern.findall(txt_edit.get('1.0', END))
    for i in result:
        list_result.insert(END, i)

def up():
    res = re.sub(ent_regex.get(), ent_up.get(), txt_edit.get("1.0", END))
    txt_edit.delete("1.0", END)
    txt_edit.insert("1.0", res)





fr_functions = Frame(root)
fr_functions.columnconfigure(0, weight=1)
fr_functions.rowconfigure(4, weight=1)

se_functions = Frame(root)
se_functions.columnconfigure(0, weight=1)
se_functions.rowconfigure(2, weight=1)

ent_regex = Entry(fr_functions)
ent_regex.grid(column=0, row=0, sticky=N, padx=2, pady=2)

btn_findall = Button(fr_functions, text='Найти', command=click_findall)
btn_findall.grid(column=0, row=1, sticky=EW, padx=2, pady=2)

list_result = Listbox(fr_functions)
list_result.grid(column=0, row=4, sticky=NSEW, padx=2, pady=2)

txt_edit = Text(se_functions)
txt_edit.grid(row=0, column=0, sticky="nsew")

fr_functions.grid(column=1, row=0, sticky=NS)
se_functions.grid(column=0, row=0, sticky=NS)

btn_add = Button(fr_functions, text='Добавить', command=click_add)
btn_add.grid(column=0, row=5, sticky=EW, padx=2, pady=2)

btn_clear = Button(fr_functions, text='Очистить', command=click_clear)
btn_clear.grid(column=0, row=6, sticky=EW, padx=2, pady=2)


ent_up = Entry(fr_functions)
ent_up.grid(column=0, row=2, sticky=N, padx=4, pady=6)

btn_re = Button(fr_functions, text='Заменить', command=up)
btn_re.grid(column=0, row=3, sticky=EW, padx=2, pady=2)

root.mainloop()