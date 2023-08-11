import tkinter as t
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

def create_new():
    c=tb.Window(themename='superhero',title='Create Contact Page',size=(500,600),position=(780,250),resizable=(False,False))
    c.iconbitmap('contact.ico')
    

root=tb.Window(themename='superhero',title='Contacts App',size=(500,600),position=(750,250),resizable=(0,0))
root.iconbitmap('contact.ico')

sep=tb.Separator(root,bootstyle='info dotted')
sep.place(y=96,x=0,relwidth=1,width=500)
sep=tb.Separator(root,bootstyle='info dotted')
sep.place(y=170,x=0,relwidth=1,width=500)
sf=ScrolledFrame(root, autohide=True,bootstyle='dark rounded',height=420,width=410)
sf.pack(pady=(175,4),expand=t.NO)
label=tb.Label(root,text='Search Box->',style='secondary.TLabel',font=('Georgia',15)).place(x=10,y=117)
search_box=tb.Entry(root,style='info.TEntry')
search_box.place(x=280,y=118)



create=tb.Button(root,text='         + \nCreate New',style='success outline',command=create_new)
update=tb.Button(root,text='          +- \nUpdate Existing',style='info outline')
delete=tb.Button(root,text='          - \nDelete Contact',style='danger outline')
create.place(y=30,x=30)
update.place(y=30,x=180)
delete.place(y=30,x=350)

root.mainloop()