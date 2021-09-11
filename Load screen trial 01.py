from tkinter import*
from tkinter.ttk import*

tk=Tk()
load= Progressbar(tk, length=200)

def bar():
    import time
    load['value']=20
    tk.update_idletasks()
    time.sleep(1)
    load['value']=50
    tk.update_idletasks()
    time.sleep(1)
    load['value']=100
    tk.update_idletasks()
    time.sleep(1)
    load['value']=150
    tk.update_idletasks()
    time.sleep(1)
    load['value']=170
    tk.update_idletasks()
    time.sleep(1)
    load['value']=200
    tk.update_idletasks()
    time.sleep(1)
load.pack()
Button(tk, text='START', command=bar).pack()
mainloop()
