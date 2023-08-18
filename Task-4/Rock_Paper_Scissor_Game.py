from tkinter import *
import random
from PIL import Image,ImageTk
root=Tk()
root.title("RPS Game")
root.geometry('550x400')
global scorep,scorec,cpc
scorep,scorec=0,0

def resets():
    global scorec,scorep
    scorec,scorep=0,0
    canva.itemconfig(person_score, text=scorep)
    canva.itemconfig(computer_score, text=scorec)

def button(n):
    global scorec,scorep,cpc,result
    cpc=random.randrange(1,4)

    if(n==1):
        rp=canva.create_image(100,300,image=rockp)
        root.after(600,lambda: canva.delete(rp))
    elif(n==2):
        pp=canva.create_image(100,300,image=paperp)
        root.after(600,lambda: canva.delete(pp))
    else:
        sp=canva.create_image(100,300,image=scissorp)
        root.after(600,lambda: canva.delete(sp))


    if(cpc==2 and n==1):
        result='Computer Wins ->'
        scorec+=5
    elif(cpc==1 and n==3):
        result='Computer Wins ->'
        scorec+=5
    elif(cpc==3 and n==2):
        result='Computer Wins ->'
        scorec+=5
    elif(cpc==n):
        result='= Tie ='
    else:
        result='<- You Win'
        scorep+=5

    if(cpc==1):
        rc=canva.create_image(460,300,image=rockc)
        root.after(600,lambda: canva.delete(rc))
    elif(cpc==2):
        pc=canva.create_image(460,300,image=paperc)
        root.after(600,lambda: canva.delete(pc))
    else:
        sc=canva.create_image(460,300,image=scissorc)
        root.after(600,lambda: canva.delete(sc))

    a=canva.create_text(270,300,text=result,font=('Georgia',18))
    root.after(600, lambda: canva.delete(a))
    root.after(600,lambda: canva.delete())
    canva.itemconfig(person_score, text=scorep)
    canva.itemconfig(computer_score, text=scorec)


bg=PhotoImage(file='img/l1.png')

rockc=Image.open('img/rock.png').resize((50,66),Image.LANCZOS).rotate(90,expand=1).transpose(Image.FLIP_TOP_BOTTOM)
rockc=ImageTk.PhotoImage(rockc)
paperc=Image.open('img/paper.png').resize((50,66),Image.LANCZOS).rotate(90,expand=1).transpose(Image.FLIP_TOP_BOTTOM)
paperc=ImageTk.PhotoImage(paperc)
scissorc=Image.open('img/scissors.png').resize((50,66),Image.LANCZOS).rotate(90,expand=1).transpose(Image.FLIP_TOP_BOTTOM)
scissorc=ImageTk.PhotoImage(scissorc)

rockp=Image.open('img/rock.png').resize((50,66),Image.LANCZOS).rotate(270,expand=1)
rockp=ImageTk.PhotoImage(rockp)
paperp=Image.open('img/paper.png').resize((50,66),Image.LANCZOS).rotate(270,expand=1)
paperp=ImageTk.PhotoImage(paperp)
scissorp=Image.open('img/scissors.png').resize((50,66),Image.LANCZOS).rotate(270,expand=1)
scissorp=ImageTk.PhotoImage(scissorp)

canva=Canvas(root,width=550,height=400)
canva.pack(fill='both',expand=True)
canva.create_image(0,0,image=bg,anchor='nw')
canva.create_text(60,60,text="Your Score",font=('Times',15,UNDERLINE))
canva.create_text(470,60,text="Computer Score",font=('Times',15,UNDERLINE))
canva.create_text(280,120,text="Choose One To Start The Game!",font=('Lexend ',20,'normal'),fill='Black')
b1=Button(root,text='Rock 🪨',width=6,height=1,font=('Times',15),command=lambda:button(1),bg='#6c8fbd',activebackground='#506c91')
b1_w=canva.create_window(80,200,anchor='sw',window=b1)
b2=Button(root,text='Paper 📰',width=7,height=1,font=('Times',15),command=lambda:button(2),bg='#6c8fbd',activebackground='#506c91')
b2_w=canva.create_window(230,200,anchor='sw',window=b2)
b3=Button(root,text='      Scissior ✂️',width=8,height=1,font=('Times',15),command=lambda:button(3),bg='#6c8fbd',activebackground='#506c91')
b3_w=canva.create_window(380,200,anchor='sw',window=b3)
reset=Button(root,text="Try Again?",font=('Times',13),command=resets,bg='#6c8fbd',activebackground='#506c91')
resetw=canva.create_window(230,380,window=reset,anchor='sw')
person_score=canva.create_text(48,45,anchor='sw',text=scorep,font=('Lexend',20),fill='#8f2e51')
computer_score=canva.create_text(465,45,anchor='sw',text=scorep,font=('Lexend',20),fill='#8f2e51')



root.mainloop()