from tkinter import *
import os
def onclicking(value):
    if (value ==1):
        os.system("shutdown /s /t 5")
    elif value ==2:
        os.system("shutdown /r /t 5")
    elif value ==3:
        os.system(f"shutdown /s /t {int(entry.get())*60}")
    elif value == 4 :
        os.system(f"shutdown /s /t {int(entry.get())*60}")
def cancel():
    os.system("shutdown /a")
window = Tk()
window.title('Operation')
window.geometry("480x480")
v = IntVar()
Radiobutton(window,text ="Shutdown" , variable = v , value = 1).grid(row =0 ,sticky = W )
Radiobutton(window,text ="Restart" , variable = v , value = 2).grid(row = 1 ,sticky = W)
Radiobutton(window,text ="Set A Timer to shutdown" , variable = v , value = 3).grid(row =2 ,sticky = W)
Radiobutton(window,text ="Set A Timer to restart" , variable = v , value = 4).grid(row =3 ,sticky = W)
button1 = Button(window,text ='Done',command = lambda: onclicking(v.get()),bg='blue' ,fg ='white')
button2 = Button(window,text ='cancel',command = cancel,bg='red' ,fg ='black')
entry = Entry(window)
entry.insert(0,'enter a time in minutes')
entry.grid(row=4 ,columnspan =2)
button1.grid(row = 5 )
button2.grid(row = 5 ,column =1)
window.mainloop()