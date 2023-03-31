from tkinter import *
from tkinter import ttk
from tkinter import messagebox
global ActivePlayer
global winner
global a,b,c,d,e,f,g,h,i
global user1
global user2
def game(p_1,p_2):
    global ActivePlayer
    global winner
    global a, b, c, d, e, f, g, h, i
    global user1
    global user2
    p1=p_1
    p2=p_2
    root=Tk()

    def rootexit():
        root.destroy()
        exit()

    root.protocol('WM_DELETE_WINDOW',rootexit)

    frame1=ttk.Frame(root,width=500,height=500)
    frame1.grid(row=0,column=0,sticky='nsew')

    l1=ttk.Label(frame1,text="Player 1")
    l1.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
    e1=ttk.Entry(frame1,width=20)
    e1.grid(row=0,column=1,sticky='nsew',padx=10,pady=10)

    l2=ttk.Label(frame1,text="Player 2")
    l2.grid(row=0,column=2,sticky='nsew',padx=10,pady=10)
    e2=ttk.Entry(frame1,width=20)
    e2.grid(row=0,column=3,sticky='nsew',padx=10,pady=10)



    frame2=ttk.Frame(root,width=50,height=50)
    frame2.grid(row=1,column=0,sticky='nsew')

    submit=ttk.Button(frame2,text='Start Play')
    submit.grid(row=0,column=1,sticky='nsew',padx=10,pady=10)

    def subClick():
        global user1
        global user2
        user1=e1.get()
        user2=e2.get()

        if user1=="" or user2=="":
            messagebox.showinfo(title='warning',message='Please Enter valid names to continue')
        elif user1==user2:
            messagebox.showinfo(title='warning', message='Please Enter different names to continue')
        else:
            root.title("{}'s turn (X)".format(user1))
            bu1.state(['!disabled'])
            bu2.state(['!disabled'])
            bu3.state(['!disabled'])
            bu4.state(['!disabled'])
            bu5.state(['!disabled'])
            bu6.state(['!disabled'])
            bu7.state(['!disabled'])
            bu8.state(['!disabled'])
            bu9.state(['!disabled'])

    submit.configure(command=subClick)
    root.title("Tic Tac Toe")

    ActivePlayer=1
    winner=-1
    a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;
    style=ttk.Style()
    style.theme_use('classic')
    style.configure('TButton',foreground='Red',background='Black',font=('consolas',15,'bold'))
    style.map('TButton',background=[('pressed','green')])

    style.configure('submit.TButton',foreground='Black',background='Blue',font=('consolas',10))
    submit.configure(style='submit.TButton')

    bu1=ttk.Button(frame2,text=" ",state=['disabled'])
    bu1.grid(row=1,column=0,sticky='nsew',ipadx=40,ipady=40)
    bu1.config(command=lambda :BuClick(1))

    bu2=ttk.Button(frame2,text=" ",state=['disabled'])
    bu2.grid(row=1,column=1,sticky='nsew',ipadx=40,ipady=40)
    bu2.config(command=lambda :BuClick(2))

    bu3=ttk.Button(frame2,text=" ",state=['disabled'])
    bu3.grid(row=1,column=2,sticky='nsew',ipadx=40,ipady=40)
    bu3.config(command=lambda :BuClick(3))

    bu4=ttk.Button(frame2,text=" ",state=['disabled'])
    bu4.grid(row=2,column=0,sticky='nsew',ipadx=40,ipady=40)
    bu4.config(command=lambda :BuClick(4))

    bu5=ttk.Button(frame2,text=" ",state=['disabled'])
    bu5.grid(row=2,column=1,sticky='nsew',ipadx=40,ipady=40)
    bu5.config(command=lambda :BuClick(5))

    bu6=ttk.Button(frame2,text=" ",state=['disabled'])
    bu6.grid(row=2,column=2,sticky='nsew',ipadx=40,ipady=40)
    bu6.config(command=lambda :BuClick(6))

    bu7=ttk.Button(frame2,text=" ",state=['disabled'])
    bu7.grid(row=3,column=0,sticky='nsew',ipadx=40,ipady=40)
    bu7.config(command=lambda :BuClick(7))

    bu8=ttk.Button(frame2,text=" ",state=['disabled'])
    bu8.grid(row=3,column=1,sticky='nsew',ipadx=40,ipady=40)
    bu8.config(command=lambda :BuClick(8))

    bu9=ttk.Button(frame2,text=" ",state=['disabled'])
    bu9.grid(row=3,column=2,sticky='nsew',ipadx=40,ipady=40)
    bu9.config(command=lambda :BuClick(9))

    frame1.rowconfigure(0,weight=1)
    frame1.rowconfigure(1,weight=1)
    frame1.columnconfigure(0,weight=1)
    frame1.columnconfigure(1,weight=1)
    frame1.columnconfigure(2,weight=1)
    frame1.columnconfigure(3,weight=1)

    frame2.rowconfigure(0,weight=1)
    frame2.rowconfigure(1,weight=1)
    frame2.rowconfigure(2,weight=1)
    frame2.columnconfigure(0,weight=1)
    frame2.columnconfigure(1,weight=1)
    frame2.columnconfigure(2,weight=1)


    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.columnconfigure(0,weight=1)

    def BuClick(id):
        global a, b, c, d, e, f, g, h, i
        global ActivePlayer
        p1=p_1
        p2=p_2
        global winner
        print("ID : {}".format(id))

        if ActivePlayer==1:
            p1.append(id)
            SetLayout(id,"X")
            ActivePlayer=2
            root.title("{}'s turn (O)".format(user2))
            print("p1 = {}".format(p1))
            if (1 in p1) and (2 in p1) and (3 in p1):
                winner=1
            elif (4 in p1) and (5 in p1) and (6 in p1):
                winner = 1
            elif (7 in p1) and (8 in p1) and (9 in p1):
                winner = 1
            elif (1 in p1) and (4 in p1) and (7 in p1):
                winner = 1
            elif (2 in p1) and (5 in p1) and (8 in p1):
                winner = 1
            elif (3 in p1) and (6 in p1) and (9 in p1):
                winner=1
            elif (1 in p1) and (5 in p1) and (9 in p1):
                winner=1
            elif (3 in p1) and (5 in p1) and (7 in p1):
                winner=1

        elif ActivePlayer==2:
            p2.append(id)
            SetLayout(id,"O")
            ActivePlayer=1
            root.title("{}'s turn (X)".format(user1))
            print("p2 = {}".format(p2))
            if (1 in p2) and (2 in p2) and (3 in p2):
                winner=2
            elif (4 in p2) and (5 in p2) and (6 in p2):
                winner = 2
            elif (7 in p2) and (8 in p2) and (9 in p2):
                winner = 2
            elif (1 in p2) and (4 in p2) and (7 in p2):
                winner = 2
            elif (2 in p2) and (5 in p2) and (8 in p2):
                winner = 2
            elif (3 in p2) and (6 in p2) and (9 in p2):
                winner = 2
            elif (1 in p2) and (5 in p2) and (9 in p2):
                winner=2
            elif (3 in p2) and (5 in p2) and (7 in p2):
                winner=2

        if winner == 1:
            res=messagebox.askquestion(title="Congratulations", message="{} wins\nDo you want to play again ?".format(user1))
            if res=='no':
                root.destroy()
                exit()
            elif res=='yes':
                root.destroy()

        elif winner == 2:
            res=messagebox.askquestion(title="Congratulations", message="{} wins\nDo you want to play again ?".format(user2))
            if res=='no':
                root.destroy()
                exit()
            elif res=='yes':
                root.destroy()


        if a==1 and b==1 and c==1 and d==1 and e==1 and f==1 and g==1 and h==1 and i==1 and winner==-1:
            res=messagebox.askquestion(title="Oops !!", message="Match Drawn\nDo you want to play again ?")
            if res=='no':
                root.destroy()
                exit()
            elif res=='yes':
                root.destroy()



    def SetLayout(id,Symbol):
        global a, b, c, d, e, f, g, h, i
        if id==1:
            bu1.config(text=Symbol)
            bu1.state(['disabled'])
            a=1

        elif id==2:
            bu2.config(text=Symbol)
            bu2.state(['disabled'])
            b=1
        elif id == 3:
            bu3.config(text=Symbol)
            bu3.state(['disabled'])
            c=1
        elif id == 4:
            bu4.config(text=Symbol)
            bu4.state(['disabled'])
            d=1
        elif id == 5:
            bu5.config(text=Symbol)
            bu5.state(['disabled'])
            e=1
        elif id == 6:
            bu6.config(text=Symbol)
            bu6.state(['disabled'])
            f=1
        elif id == 7:
            bu7.config(text=Symbol)
            bu7.state(['disabled'])
            g=1
        elif id == 8:
            bu8.config(text=Symbol)
            bu8.state(['disabled'])
            h=1
        elif id == 9:
            bu9.config(text=Symbol)
            bu9.state(['disabled'])
            i=1

    root.mainloop()


def main():
    while(1):
        p1=[]
        p2=[]
        print(p1)
        print(p2)
        game(p1,p2)



if __name__ == '__main__':main()