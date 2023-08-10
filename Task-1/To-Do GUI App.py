import tkinter as t
root=t.Tk()
root.geometry('200x35')
sroot = t.Label(root, text="Loading.... Please Wait!", font=40)
sroot.pack()
global count,task_list,task_details
count=0
task_list=[]
def main():
    root.destroy()
    tb1()
def update():
    u.destroy()
    tb1()
def create():
    c.destroy()
    tb1()
def lists():
    l.destroy()
    tb1()

def tb1():
    global tb
    tb=t.Tk()
    tb.title('Main Screen')
    tb.geometry('380x320')

    ask=t.Label(tb,text='What to do? Choose One!')
    ask.place(relx=0.5,rely=0.1,anchor='center')

    create=t.Button(tb,activebackground='#b3b3b3',text='Create List',command=creat_page)
    create.place(relx=0.5,rely=0.3,anchor='center')

    update=t.Button(tb,activebackground='#b3b3b3',text='Update Existing List',command=update_page)
    update.place(relx=0.5,rely=0.5,anchor='center')

    show=t.Button(tb,activebackground='#b3b3b3',text='Show List',command=show_list)
    show.place(relx=0.5,rely=0.7,anchor='center')

def add():
    global task_list,count,display_area,task_entry
    if(task_entry.get()==''): 
        t.messagebox.showerror("Error",message='Input is not valid!')
    else:
        count+=1
        task_list.append(task_entry.get()+'\n')
        display_area.insert('end -1 chars', "[" + str(count) + "] " + task_entry.get()+'\n')
        t.messagebox.showinfo('','Successfully Added!')

def add1():
    global task_list,count,display_area,task_entry
    if(task_entry.get()==''): 
        t.messagebox.showerror("Error",message='Input is not valid!')
    else:
        count+=1
        task_list.append(task_entry.get()+'\n')
        t.messagebox.showinfo('','Successfully Added!')

def delete():
    global task_list,count
    if count==0:
        t.messagebox.showerror('Error',message='Add Some Task First!')
        return
    if(int(task_entry.get())-1>count):
        t.messagebox.showerror('Error',message='No Such Task No. Present!')
    else:
        count-=1
        del task_list[int(task_entry.get())-1]
        display_area.delete(1.0,t.END)
        for i in range(len(task_list)) :
            display_area.insert('end -1 chars', "[ " + str(i + 1) + " ] " + task_list[i])

def creat_page():
    global c,task_entry
    tb.destroy()
    c=t.Tk()
    c.title('Create To-Do List')
    c.geometry('480x160')
    t.Label(c,text='Enter the task:').place(relx=.5,rely=.2,anchor='center')
    task_entry=t.Entry(c,bd=2,width=70,)
    task_entry.place(relx=.5,rely=.39,anchor='center')
    add_button=t.Button(c,text='Add '+ u'\u002B',command=add1)
    add_button.place(relx=.5,rely=.7,anchor='center')
    t.Button(c,text=u'\u2B90',command=create).place(relx=.05,rely=.9,anchor='sw')

def show_list():
    global l,task_list
    if(len(task_list)==0):
        t.messagebox.showinfo('','No task for today, Enjoy!')
    else:
        tb.destroy()
        l=t.Tk()
        l.title('To-Do List View')
        l.geometry('148x160')
        listbox=t.Listbox(l)
        listbox.pack(fill='both',side='left')
        scrollbar = t.Scrollbar(l)
        scrollbar.pack(fill='both',side='left')
        for values in task_list:
            listbox.insert(t.END, values)
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        t.Button(l,text=u'\u2B90',command=lists).place(relx=.05,rely=.9,anchor='sw')

def update_page():
    global u,display_area,task_entry
    tb.destroy()
    u=t.Tk()
    u.title('Update To-Do List')
    u.geometry('480x360')

    t.Label(u,text='Choose the task {id} to Delete:').place(relx=.5,rely=.2,anchor='center')

    display_area = t.Text(u, height = 5, width = 50,)
    display_area.place(relx=.5,rely=.49,anchor='center')
    fonts=("Times New Roman",12)
    display_area.configure(font=fonts)

    task_entry=t.Entry(u,bd=2,width=70,)
    task_entry.place(relx=.5,rely=.29,anchor='center')

    add_button=t.Button(u,text='Add (+)',command=add)
    add_button.place(relx=.4,rely=.7,anchor='center')

    delete_button=t.Button(u,text='Delete (-)',command=delete)
    delete_button.place(relx=.6,rely=.7,anchor='center')

    t.Button(u,text=u'\u2B90',command=update).place(relx=.05,rely=.9,anchor='sw')
    #to update message page when opened
    if(len(task_list)!=0):
        for i in task_list:
            display_area.insert('end -1 chars', "[" + str(count) + "] " + str(i))

root.after(1000,main)

root.mainloop()