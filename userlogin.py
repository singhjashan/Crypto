from tkinter import *
import tkinter.messagebox as msg

import dashboard2
from connection import Connect
import userDashboard

class main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x600')
        self.root.title('Login User')

        self.lb = Label(self.root, text='Login User', font=('arial', 20,'bold'))
        self.lb.pack(pady=20)

        self.f = Frame(self.root)

        self.lb2 = Label(self.f, text='Email', font=('calibri', 14))
        self.lb2.grid(row=1,column=0, padx=10, pady=10)
        self.txt2 = Entry(self.f, font=('calibri', 14), width=30)
        self.txt2.grid(row=1,column=1, padx=10, pady=10)

        self.lb4 = Label(self.f, text='Password', font=('calibri', 14))
        self.lb4.grid(row=3,column=0, padx=10, pady=10)
        self.txt4 = Entry(self.f, font=('calibri', 14), width=30, show='*')
        self.txt4.grid(row=3,column=1, padx=10, pady=10)
        self.f.pack()

        self.btn = Button(self.root, text='Login', font=('arial', 12), command=self.checkUser)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def checkUser(self):
        self.email = self.txt2.get()
        self.password = self.txt4.get()

        conn = Connect()
        cr = conn.cursor()
        q = f"select * from user where email='{self.email}' and password='{self.password}'"
        cr.execute(q)
        result = cr.fetchone()
        print(result)
        if result is None:
            msg.showwarning('Warning',"Invalid Email/Password",parent= self.root)
        else:
            msg.showinfo("success","Login Successful",parent= self.root)
            self.root.destroy()
            dashboard2.main(userID=result[0])



#obj = main()