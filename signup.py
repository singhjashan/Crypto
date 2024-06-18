#

from tkinter import *
import tkinter.messagebox as msg
from connection import Connect

class main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x600')
        self.root.title('Register User')

        self.lb = Label(self.root, text='Register User', font=('cambria', 20,'bold'))
        self.lb.pack(pady=20)

        self.f = Frame(self.root)

        self.lb1 = Label(self.f, text='Name', font=('Book Antiqua', 14))
        self.lb1.grid(row=0,column=0, padx=10, pady=10)
        self.txt1 = Entry(self.f, font=('calibri', 14), width=30)
        self.txt1.grid(row=0,column=1, padx=10, pady=10)

        self.lb2 = Label(self.f, text='Email', font=('Book Antiqua', 14))
        self.lb2.grid(row=1,column=0, padx=10, pady=10)
        self.txt2 = Entry(self.f, font=('calibri', 14), width=30)
        self.txt2.grid(row=1,column=1, padx=10, pady=10)

        self.lb3 = Label(self.f, text='Mobile', font=('Book Antiqua', 14))
        self.lb3.grid(row=2,column=0, padx=10, pady=10)
        self.txt3 = Entry(self.f, font=('calibri', 14), width=30)
        self.txt3.grid(row=2,column=1, padx=10, pady=10)

        self.lb4 = Label(self.f, text='Password', font=('Book Antiqua', 14))
        self.lb4.grid(row=3,column=0, padx=10, pady=10)
        self.txt4 = Entry(self.f, font=('calibri', 14), width=30, show='*')
        self.txt4.grid(row=3,column=1, padx=10, pady=10)

        self.f.pack()

        self.btn = Button(self.root, text='Submit', font=('Book Antiqua', 12), command=self.registerUser)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def registerUser(self):
        self.name = self.txt1.get()
        self.email = self.txt2.get()
        self.mobile = self.txt3.get()
        self.password = self.txt4.get()

        if len(self.name) == 0 or len(self.email) == 0 or len(self.mobile) == 0 or len(self.password) == 0:
            msg.showwarning('Warning',"Please Input all Data",parent= self.root)
        else:
            conn = Connect()
            cr = conn.cursor()

            q = f"select * from user where email='{self.email}' or mobile='{self.mobile}'"
            cr.execute(q)
            result = cr.fetchone()
            if result is None:
                q = f"insert into user values(null,'{self.name}','{self.email}','{self.mobile}','{self.password}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo('Success','User has been Registered',parent= self.root )
                self.root.destroy()
            else:
                msg.showwarning("Warning","Same Email or Mobile already exists",parent= self.root)

#main()