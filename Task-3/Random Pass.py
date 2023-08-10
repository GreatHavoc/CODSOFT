from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title('Password Generator')
root.geometry('260x260')
root.resizable(0,0)
root.config(background='#24232a')
def pas():
    global box1
    length=''
    box1.delete("1.0","end")
    try:
        lists='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX1234567890@&'
        a=int(box.get(1.0,END))
        #custom exception
        if a<6 or a>16:
            raise ValueError
        s=random.sample(lists,a)
        for i in s:
            length+=i
        box1.insert(END,length,"center")

    except:
        messagebox.showerror('Error','Enter number in range 6-16')
global box1 
label1=Label(root,text='Enter the length of the Password',font=('Times',13),background='#24232a',foreground='#FFFFFF')
label1.grid(row=0,padx=(12,4),pady=(10,10),sticky='w',ipadx=5,ipady=5)

box=Text(root,font=('Times',13),width=10,height=1,background='#24232a',foreground='#FFFFFF')
box.grid(row=1,padx=(50,50),pady=(5,10))

b=Button(root,text='Generate',width=30,height=2,background='#24232a',activebackground='#a5ffaf',foreground='#FFFFFF',command=pas)
b.grid(row=2,padx=(13,10),pady=(10,10))

label2=Label(root,text='Your Password Will Show Here',font=('Times',13),background='#24232a',borderwidth=5,foreground='#FFFFFF')
label2.grid(row=3,padx=(12,10),pady=(10,0))

arrow=Label(text=u'\u21A7',font=('Times',14,'normal'),background='#24232a',foreground='#FFFFFF')
arrow.grid(row=4,padx=(50,50))

box1=Text(root,font=('Times',13),width=10,height=1,borderwidth=0,background='#24232a',foreground='#FFFFFF')
box1.grid(row=5,padx=(50,50),pady=(5,20),sticky='e,w,n,s')

root.mainloop()