from tkinter import *
import tkinter.messagebox as msg
from connection import Connect
import userDashboard

class main:
    def __init__(self, userID):
        self.root = Tk()
        self.root.geometry('600x600')
        self.root.title('Change Password')
        self.userID = userID

        self.lb = Label(self.root, text='User Change Password', font=('arial', 20,'bold'))
        self.lb.pack(pady=20)

        self.f = Frame(self.root)

        self.lb1 = Label(self.f, text='User ID', font=('calibri', 14))
        self.lb1.grid(row=0,column=0, padx=10, pady=10)
        self.txt1 = Entry(self.f, font=('calibri', 14), width=30)
        self.txt1.grid(row=0,column=1, padx=10, pady=10)
        self.txt1.insert(0, self.userID)
        self.txt1.config(state='readonly')

        self.lb2 = Label(self.f, text='Old Password', font=('calibri', 14))
        self.lb2.grid(row=1,column=0, padx=10, pady=10)
        self.txt2 = Entry(self.f, font=('calibri', 14), width=30, show='*')
        self.txt2.grid(row=1,column=1, padx=10, pady=10)

        self.lb4 = Label(self.f, text='New Password', font=('calibri', 14))
        self.lb4.grid(row=2,column=0, padx=10, pady=10)
        self.txt4 = Entry(self.f, font=('calibri', 14), width=30, show='*')
        self.txt4.grid(row=2,column=1, padx=10, pady=10)

        self.f.pack()

        self.btn = Button(self.root, text='Login', font=('arial', 12), command=self.changePassword)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def changePassword(self):
        oldPass = self.txt2.get()
        newPass = self.txt4.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from user where id='{self.userID}' and password='{oldPass}'"
        cr.execute(q)
        result = cr.fetchone()
        if result is None:
            msg.showwarning('Warning',"Incorrect Old Password", parent=self.root)
        else:
            q1 = f"update user set password='{newPass}' where id='{self.userID}'"
            cr.execute(q1)
            conn.commit()
            msg.showinfo("Success","Password has been changed", parent=self.root)
            self.root.destroy()





# obj = main(2)