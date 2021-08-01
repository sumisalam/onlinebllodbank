from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector

m=Tk()
m.geometry("400x400")
m.title('ABC')

def mob(r):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="abcdb")
    cur = con.cursor()
    p = r.get()





    if (p=="" ):
             messagebox.showinfo("search","invalid search")
    else:
            sql = "select*from datas where phone=%s "
            val = (p,)
            cur.execute(sql, val)
            results = cur.fetchall()
            top6 = Toplevel()
            top6.geometry("500x500")
            top6.title("view details")

    h = ("id", "name", "age", "sex", "phone", "blood group", "rh")
    for i, d in enumerate(h):
        if i == 0:
            z = Label(top6, text=d, width=10, relief="groove")
            z.grid(row=0, column=i)
        else:
            r = Label(top6, text=d, width=10, relief="groove")
            r.grid(row=0, column=i)

    for i, d in enumerate(results):
        for columnno in range(7):

            if columnno == 0:
                e = Label(top6, text=d[columnno], width=10)
                e.grid(row=i + 1, column=columnno)
            else:

                f = Label(top6, text=d[columnno], width=10)
                f.grid(row=i + 1, column=columnno)


def phon():
    top5 = Toplevel()

    l1 = Label(top5, text="Phone")
    l1.place(x=50, y=60)

    r = Entry(top5, width=30)
    r.place(x=100, y=60)

    b = Button(top5, text="SEARCH", width=25, command=lambda: mob(r))
    b.place(x=100, y=150)


def searchdata(p, q):
    bg = p.get()
    rh = q.get()
    con = mysql.connector.connect(host="localhost", user="root", password="", database="abcdb")
    cur = con.cursor()


    if (bg=="---select---" or rh==""):
        messagebox.showinfo("search","All fields are required")
    else:
        sql = "select*from datas where bloodgroup=%s and rh=%s"
        val = (bg, rh)
        cur.execute(sql, val)
        results = cur.fetchall()

        top4 = Toplevel()
        top4.geometry("500x500")
        top4.title("View all")


    heading = ("id", "name", "age", "sex", "phone", "blood group", "rh")
#heading print
    for i, d in enumerate(heading):
        if i == 0:
            a = Label(top4, text=d, width=10, relief="groove")
            a.grid(row=0, column=i)
        else:
            b = Label(top4, text=d, width=10, relief="groove")
            b.grid(row=0, column=i)
#fetched data print
    for i, d in enumerate(results):
        for columnno in range(7):
            if columnno == 0:
                e = Label(top4, text=d[columnno], width=10)
                e.grid(row=i + 1, column=columnno)
            else:
                f = Label(top4, text=d[columnno], width=10)
                f.grid(row=i + 1, column=columnno)


def search():
    top3 = Toplevel()
    l1 = Label(top3, text="Blood Group")
    l1.place(x=80, y=60)

    p = ttk.Combobox(top3)
    p['values'] = ("---select---", "A", "B", "AB", "O")
    p.current(0)
    p.place(x=170, y=60)

    l1 = Label(top3, text="Rh")
    l1.place(x=80, y=100)

    q = StringVar()
    r1 = Radiobutton(top3, text="positive", variable=q, value="positive", tristatevalue=0)
    r1.place(x=170, y=100)
    r2 = Radiobutton(top3, text="negative", variable=q, value="negative", tristatevalue=0)
    r2.place(x=250, y=100)

    b = Button(top3, text="SEARCH", width=25, command=lambda: searchdata(p, q))
    b.place(x=100, y=150)


def viewdata():
    con = mysql.connector.connect(host="localhost", user="root", password="",database="abcdb")
    cur = con.cursor()
    cur.execute("select *from datas")
    result=cur.fetchall()

    top1 = Toplevel()
    top1.geometry("500x500")
    top1.title("View ALl")

    tuple = ("id", "name", "age", "phone","sex",  "bloodgroup", "rh")
    for index, data in enumerate(tuple):
        if index == 0:
            d = Label(top1, text=data, width=5, relief="groove", bg="red")
            d.grid(row=0, column=[index])
        else:
            c = Label(top1, text=data, width=10, relief="groove", bg="red")
            c.grid(row=0, column=[index])
    for i, d in enumerate(result):
        for columnno in range(7):
            if columnno == 0:
                e = Label(top1, text=d[columnno], width=10)
                e.grid(row=i + 1, column=columnno)
            else:
                f = Label(top1, text=d[columnno], width=10)
                f.grid(row=i + 1, column=columnno)


def save(e1,e2,e3,v,c,v1):
    con=mysql.connector.connect(host="localhost",user="root",password="")
    cur=con.cursor()
    cur.execute("create database if not exists abcdb")
    con = mysql.connector.connect(host="localhost", user="root", password="",database="abcdb")
    cur=con.cursor()
    cur.execute("create table if not exists datas(id int primary key auto_increment,name varchar(100),age int,phone bigint,sex varchar(100),bloodgroup varchar(100),rh varchar(100))")

    name=e1.get()
    age=e2.get()
    phone=e3.get()
    sex=v.get()
    bg=c.get()
    rh=v1.get()

    sql="insert into datas(name,age,phone,sex,bloodgroup,rh) values(%s,%s,%s,%s,%s,%s)"
    values=(name,age,phone,sex,bg,rh)
    cur.execute(sql,values)
    con.commit()
    con.close()
    messagebox.showinfo("info","data added")


    '''sql = "insert into datas(name,age,phone,sex,bloodgroup,rh)values(%s,%s,%s,%s,%s,%s)"
        values = (nam, ag, phon, se, bg, rh)
        cur.execute(sql, values)
        con.commit()
        con.close()
        messagebox.showinfo("information", "data added")'''


def adddata():
    top=Toplevel()
    top.geometry('400x400')
    top.title('Add data')
    l1=Label(top,text="ADD DATAS",fg="blue",font=30)
    l1.pack()

    n1=Label(top,text="Name")
    n1.place(x=80,y=60)

    e1=Entry(top,width=30)
    e1.place(x=170,y=60)

    n1 = Label(top, text="Age")
    n1.place(x=80, y=90)
    e2 = Entry(top, width=30)
    e2.place(x=170, y=90)

    n1 = Label(top, text="Phone")
    n1.place(x=80, y=120)
    e3 = Entry(top, width=30)
    e3.place(x=170, y=120)

    n1 = Label(top, text="Sex")
    n1.place(x=80, y=150)
    v=StringVar()
    r1=Radiobutton(top,text="male",variable=v,value="male",tristatevalue=0)
    r1.place(x=170,y=150)
    r1 = Radiobutton(top, text="female", variable=v, value="female", tristatevalue=0)
    r1.place(x=230, y=150)
    r1 = Radiobutton(top, text="others", variable=v, value="others", tristatevalue=0)
    r1.place(x=300, y=150)

    n1 = Label(top, text="Blood group")
    n1.place(x=80, y=180)

    c=ttk.Combobox(top)
    c['values']=("---select---","A","B","AB","0")
    c.current(0)
    c.place(x=170,y=180)

    n1 = Label(top, text="Rh")
    n1.place(x=80, y=210)
    v1 = StringVar()

    r1 = Radiobutton(top, text="positive", variable=v1, value="positive", tristatevalue=0)
    r1.place(x=170, y=210)
    r1 = Radiobutton(top, text="negative", variable=v1, value="negative", tristatevalue=0)
    r1.place(x=270, y=210)

    b = Button(top, text="Submit", bg="red", fg="white", width=10, height=1,command=lambda:save(e1,e2,e3,v,c,v1))
    b.place(x=80, y=250)

l=Label(m,text="ABC association",fg="blue",font=30)
l.pack()
b=Button(m,text="add data",bg="red",fg="white",width=20,height=3,command=adddata)
b.place(x=180,y=70)
b=Button(m,text="view data",bg="red",fg="white",width=20,height=3,command=viewdata)
b.place(x=180,y=150)
b=Button(m,text="search with bloodgroup",bg="red",fg="white",width=20,height=3,command=search)
b.place(x=180,y=230)
g = Button(m, text="search with phone number", bg="red", fg="white", width=20, height=3, command=phon)
g.place(x=180, y=300)
m.mainloop()