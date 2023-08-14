import tkinter as t
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
from openpyxl import load_workbook
import sqlite3


con=sqlite3.connect('contact_database.db')
cur=con.cursor()
wb=load_workbook('country.xlsx')
ws=wb['Sheet1']
cA=ws['A']
cB=ws['B']
countrylist=[]
for i in range(len(cA)):
    countrylist.append((cA[i].value,cB[i].value))
mail_list=["outlook.com","gmail.com","ymail.com","mail.com"]

def show_details(event):
    selected=lis.curselection()
    person_details=tb.Toplevel(title='Person Details',size=(350,400),position=(1000,300))
    person_details.iconbitmap('contact.ico')
    simple=int(str(selected)[1])
    tb.Label(person_details,font=('Georgia',13),style='primary',text=data[simple][0]).place(x=172,y=2)
    tb.Label(person_details,bootstyle='primary',font=('Georgia',12),text='Person Id').place(x=128,y=30)

    tb.Separator(person_details,bootstyle='info').place(x=0,y=57,width=350)
    tb.LabelFrame(person_details,text="First Name:",style='primary',height=60,width=160).grid(row=0,column=0,sticky='w',pady=(60,5),padx=(5,10))
    tb.Label(person_details,text=data[simple][1],font=('',12),style='info').place(y=80,x=15)
    tb.LabelFrame(person_details,text="Last Name:",style='primary',height=60,width=160).grid(row=0,column=1,sticky='w',pady=(60,5),padx=(10,5))
    tb.Label(person_details,text=data[simple][2],font=('Georgia',12),style='info').place(y=80,x=200)
    tb.LabelFrame(person_details,bootstyle='primary',text='ISD code',height=60,width=113).place(x=8,y=130)
    tb.Label(person_details,text=data[simple][4],font=('Georgia',12),style='info').place(x=12,y=150)
    tb.LabelFrame(person_details,bootstyle='primary',text='Mobile No.',height=60,width=218).place(x=127,y=130)
    tb.Label(person_details,text=data[simple][3],font=('Georgia',12),style=('info')).place(x=150,y=150)
    tb.LabelFrame(person_details,text="Email Address",style='primary',height=60,width=337).grid(row=2,columnspan=2,pady=75)
    tb.Label(person_details,text=data[simple][5],font=('Georgia',10),style='info').place(x=12,y=220)



def dosomthing():
    pass 
def update_contact():

    ums=tb.Toplevel(title='Create Contact Page',size=(400,470),position=(780,250))
    ums.iconbitmap('contact.ico')

    ums.mainloop()

    
def validate():
    con=sqlite3.connect('contact_database.db')
    cur=con.cursor()
    email_address=str(block1.get())+'@'+str(domain.get())
    try:
        if(email_address[0]=='@'):
            cur.execute("""INSERT INTO ContactDB('First_Name','Last_Name','Mobile_No','Mobile_id') VALUES (?,?,?,?)""",(fname.get(),lname.get(),mobile.get(),phoneid.get()))
            messagebox.showinfo('Success','Contact Added Successfully')
        else:
            cur.execute("""INSERT INTO ContactDB('First_Name','Last_Name','Mobile_No','Mobile_id','Email_address') VALUES (?,?,?,?,?)""",(fname.get(),lname.get(),mobile.get(),phoneid.get(),email_address))
            messagebox.showinfo('Success','Contact Added Successfully')
    except(sqlite3.IntegrityError):
        messagebox.showerror('Integrity Error','Number Entered by You is Too Short or Too Long or Already Exist')
        mobile.delete(0,'end')
    con.commit() 


def create_window():
    global fname,lname,phoneid,mobile,block1,domain
    cms=tb.Toplevel(title='Create Contact Page',size=(400,470),position=(980,250))
    cms.iconbitmap('contact.ico')

    info=tb.Label(cms,bootstyle='primary',font=('Georgia',12),text='Enter the contact details below: ').grid(row=0,padx=(6,0),pady=(10,0))

    sep1=tb.Separator(cms,bootstyle='info-dotted').place(x=0,y=50,width=400)

    name=tb.LabelFrame(cms,bootstyle='info',text='Name: ',height=100,width=390)
    name.grid(row=2,column=0,padx=(8,0),pady=(20,5),sticky='n,e,w,s')

    tb.Label(name,text="First Name:",font=('Georgia',12),style='primary').grid(row=0,column=0,pady=(7,5),padx=10)

    fname=tb.Entry(name,style='info',font=("Gerogia",12))
    fname.grid(row=0,column=1)
    tb.Label(name,text="Last Name:",font=('Georgia',12),style='primary').grid(row=1,column=0,pady=10,padx=10)
    lname=tb.Entry(name,style='info',font=("Gerogia",12))
    lname.grid(row=1,column=1)

    phone=tb.LabelFrame(cms,bootstyle='info',text='Phone No.: ',height=100,width=390)
    phone.grid(row=3,column=0,padx=(8,0),pady=5,sticky='n,e,w,s')
    tb.Label(phone,text="Select Country:",font=('Georgia',12),style='primary').grid(row=0,column=0,pady=10,padx=10,sticky='w')

    phoneid=tb.Combobox(phone,style='info',values=countrylist)
    phoneid.grid(row=0,column=1,sticky='w',padx=10,pady=10)
    phoneid.current(94)

    tb.Label(phone,text="Mobile No.:",font=('Georgia',11),style='primary').grid(row=1,column=0,pady=10,padx=10,sticky='w')
    mobile=tb.Entry(phone,style='info',font=("Gerogia",11),width=18)
    mobile.grid(row=1,column=1,padx=10,pady=10)

    email=tb.LabelFrame(cms,bootstyle='info',text='Email: ',height=100,width=390)
    email.grid(row=4,column=0,padx=(8,0),pady=5,sticky='n,e,w,s')
    block1=tb.Entry(email,style='primary',font=('Georgia',11),width=18)
    block1.grid(row=0,column=0,padx=(5,3),pady=10,sticky='w')
    at=tb.Label(email,text='@',font=('Georgia',11),style='primary').grid(row=0,column=1,padx=3,pady=(0,7))
    domain=tb.Combobox(email,style='info',values=mail_list,width=11)
    domain.grid(row=0,column=2,padx=4,pady=10)
    domain.current(1)

    add=tb.Button(cms,style='danger,outline',text='         +\nAdd Contact',command=validate)
    add.grid(row=5,padx=50,pady=7)

    cms.mainloop()

root=tb.Window(themename='superhero',title='Contacts App',size=(500,600),position=(500,250),resizable=(0,0))
root.iconbitmap('contact.ico')

create=tb.Button(root,text='         + \nCreate New',style='success outline',command=create_window,width=12)
update=tb.Button(root,text='          +- \nUpdate Existing',style='info outline')
delete=tb.Button(root,text='          - \nDelete Contact',style='danger outline')
create.place(y=30,x=25)
update.place(y=30,x=184)
delete.place(y=30,x=350)

sep=tb.Separator(root,bootstyle='info dotted')
sep.place(y=96,x=0,relwidth=1,width=500)
sep=tb.Separator(root,bootstyle='info dotted')
sep.place(y=170,x=0,relwidth=1,width=500)

label=tb.Label(root,text='Search Box->',style='secondary.TLabel',font=('Georgia',15)).place(x=10,y=117)

search_box=tb.Entry(root,style='info.TEntry')
search_box.place(x=280,y=118)

sf=ScrolledFrame(root, autohide=True,bootstyle='dark rounded',height=420,width=410)
sf.pack(pady=(175,4),expand=t.NO,padx=5)

lis=t.Listbox(sf,height=14,font=('Georgia',14),justify='center',highlightcolor='blue')
lis.pack(expand=t.NO,fill=t.BOTH)
cur.execute('SELECT * FROM ContactDB')
global data
data=cur.fetchall()
count=0
for i in data:
    lis.insert(count,i[1] +' '+i[2])
    count+=1
lis.bind('<Double-1>',show_details)
root.mainloop()