import tkinter as t
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
from openpyxl import load_workbook
wb=load_workbook('country.xlsx')
ws=wb['Sheet1']
cA=ws['A']
cB=ws['B']
countrylist=[]
for i in range(len(cA)):
    countrylist.append((cA[i].value,cB[i].value))

print(countrylist[0][0])

def dosomthing():
    pass 
def create_new():
    cms=tb.Toplevel(title='Create Contact Page',size=(400,600),position=(780,250),resizable=(False,False))
    cms.iconbitmap('contact.ico')
    info=tb.Label(cms,bootstyle='primary',font=('Georgia',12),text='Enter the contact details below: ').grid(row=0,columnspan=1,padx=(6,0),pady=(10,0))
    sep1=tb.Separator(cms,bootstyle='info-dotted').place(x=0,y=50,width=400)
    name=tb.LabelFrame(cms,bootstyle='info',text='Name: ',height=100,width=390)
    name.grid(row=2,column=0,padx=4,pady=(20,5),sticky='n,e,w,s')
    tb.Label(name,text="First Name:",font=('Georgia',12),style='primary').grid(row=0,column=0,pady=10,padx=10)
    fname=tb.Entry(name,style='info',font=("Gerogia",12)).grid(row=0,column=1)
    tb.Label(name,text="Last Name:",font=('Georgia',12),style='primary').grid(row=1,column=0,pady=10,padx=10)
    lname=tb.Entry(name,style='info',font=("Gerogia",12)).grid(row=1,column=1)
    phone=tb.LabelFrame(cms,bootstyle='info',text='Phone No.: ',height=100,width=390)
    phone.grid(row=3,column=0,padx=4,pady=5,sticky='n,e,w,s')
    tb.Label(phone,text="Select Country:",font=('Georgia',12),style='primary').grid(row=0,column=0,pady=10,padx=10,sticky='w')
    com=tb.Combobox(phone,style='info',values=countrylist)
    com.grid(row=0,column=1)
    com.current(94)
    com.bind('<<ComboboxSelected>>',dosomthing)
    tb.Label(phone,text="Mobile No.:",font=('Georgia',11),style='primary').grid(row=1,column=0,pady=10,padx=10,sticky='w')
    mobile=tb.Entry(phone,style='info',font=("Gerogia",11)).grid(row=1,column=1)
    email=tb.LabelFrame(cms,bootstyle='info',text='Email: ',height=100,width=390)
    email.grid(row=4,column=0,padx=4,pady=5,sticky='n,e,w,s')
    cms.mainloop()
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



create=tb.Button(root,text='         + \nCreate New',style='success outline',command=create_new,width=12)
update=tb.Button(root,text='          +- \nUpdate Existing',style='info outline')
delete=tb.Button(root,text='          - \nDelete Contact',style='danger outline')
create.place(y=30,x=25)
update.place(y=30,x=184)
delete.place(y=30,x=350)

root.mainloop()