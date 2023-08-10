import tkinter as t
root=t.Tk()
root.title('Calculator 1.0')
root.geometry('350x400')
root.resizable(0,0)
root.configure(background='#34485c')
global display_value
display_value=''
solution=t.StringVar()


def delete():
    global display_value
    if(len(display_value)):
        display_value=display_value[0:-1]
        solution.set(display_value)
    else:
        solution.set('Nothing Here')


def press(n):
    global display_value
    display_value=display_value+str(n)
    solution.set(display_value)


def equal():
    try:
        global display_value
        total=str(eval(display_value))
        solution.set(total)
        display_value=total
    except:
        solution.set('Error')
        display_value=''


def clear():
    global display_value
    display_value=''
    solution.set('')


label=t.Label(root,text="Your Calculator",borderwidth=3,relief='sunken',background='#5b86b0')
label.configure(font=("Times",15,'normal'))
label.grid(row=0,columnspan=3,ipadx=(6),padx=(70,0),pady=(9,9))

display=t.Entry(root,width=20,borderwidth=2,background='#5b86b0',font=('Times',25),textvariable=solution)
display.grid(row=1,columnspan=4,padx=(2,4))

n1=t.Button(root,width=5,height=1,text='1',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(1))
n1.grid(row=2,column=0,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n1.config(font=('Times',14,'bold'))

n2=t.Button(root,width=5,height=1,text='2',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(2))
n2.grid(row=2,column=1,sticky='e,w,n,s',pady=(20,0,),padx=(7,3))
n2.config(font=('Times',14,'bold'))

n3=t.Button(root,width=5,height=1,text='3',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(3))
n3.grid(row=2,column=2,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n3.config(font=('Times',14,'bold'))

n4=t.Button(root,width=5,height=1,text='4',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(4))
n4.grid(row=3,column=0,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n4.config(font=('Times',14,'bold'))

n5=t.Button(root,width=5,height=1,text='5',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(5))
n5.grid(row=3,column=1,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n5.config(font=('Times',14,'bold'))

n6=t.Button(root,width=5,height=1,text='6',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(6))
n6.grid(row=3,column=2,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n6.config(font=('Times',14,'bold'))

n7=t.Button(root,width=5,height=1,text='7',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(7))
n7.grid(row=4,column=0,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n7.config(font=('Times',14,'bold'))

n8=t.Button(root,width=5,height=1,text='8',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(8))
n8.grid(row=4,column=1,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n8.config(font=('Times',14,'bold'))

n9=t.Button(root,width=5,height=1,text='9',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(9))
n9.grid(row=4,column=2,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n9.config(font=('Times',14,'bold'))

n0=t.Button(root,width=5,height=1,text='0',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press(0))
n0.grid(row=5,column=1,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
n0.config(font=('Times',14,'bold'))

add=t.Button(root,width=3,height=1,text='+',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press('+'))
add.grid(row=2,column=3,sticky='e,w,n,s',pady=(20,0),padx=(4,7))
add.config(font=('Times',14,'bold'))

sub=t.Button(root,width=3,height=1,text='-',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press('-'))
sub.grid(row=3,column=3,sticky='e,w,n,s',pady=(20,0),padx=(4,7))
sub.config(font=('Times',14,'bold'))

mul=t.Button(root,width=3,height=1,text='*',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press('*'))
mul.grid(row=4,column=3,sticky='e,w,n,s',pady=(20,0),padx=(4,7))
mul.config(font=('Times',14,'bold'))

div=t.Button(root,width=3,height=1,text='/',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=lambda: press('/'))
div.grid(row=5,column=3,sticky='e,w,n,s',pady=(20,0),padx=(4,7))
div.config(font=('Times',14,'bold'))

eq=t.Button(root,width=5,height=1,text='=',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=equal)
eq.grid(row=5,column=2,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
eq.config(font=('Times',14,'bold'))

cl=t.Button(root,width=5,height=1,text='clear',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=clear)
cl.grid(row=5,column=0,sticky='e,w,n,s',pady=(20,0),padx=(7,3))
cl.config(font=('Times',14,'bold'))

dl=t.Button(root,width=5,height=1,text='del',background='#5b86b0',activebackground='#34485c',borderwidth=2,command=delete)
dl.grid(row=6,columnspan=3,sticky='e,w,n,s',pady=(20,20),padx=(70,0))
dl.config(font=('Times',14,'bold'))

root.mainloop()
