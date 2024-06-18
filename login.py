"""#
from tkinter import *

class login :

    def __init__(self):
        self.root = Tk()

        self.root.geometry("400x400")
        self.root.title("Login")

        self.lb = Label(self.root, text='Register User', font=('cambria', 20, 'bold'))
        self.lb.pack()

        self.f = Frame(self.root)

        self.lb1 = Label(self.f,text='Email',font=('Book Antiqua', 14))
        self.lb1.grid(row=0,column=0,padx=10, pady=10)
        self.txt1 = Entry(self.f,font=('calibri', 14))
        self.txt1.grid(row=0,column=1,padx=10, pady=10)

        self.lb2 = Label(self.f,text="Password",font=('Book Antiqua', 14))
        self.lb2.grid(row=1,column=0,padx=10, pady=10)
        self.txt2 = Entry(self.f,show='*',font=('calibri', 14))
        self.txt2.grid(row=1,column=1,padx=10, pady=10)

        self.f.pack()

        self.btn = Button(self.root,text="Login",font=('Book Antiqua', 14))
        self.btn.pack(pady=20)

        self.root.mainloop()
login()
"""