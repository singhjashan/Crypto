from tkinter import *
import signup
import userlogin

class main:
    def __init__(self):
        self.root = Tk()
        self.root.title('Main Page')
        self.root.geometry('400x400')

        self.btn1 = Button(self.root, text="Register User", width=20,
                           command=self.onpenSignupPage)
        self.btn1.pack(pady=40)

        self.btn2 = Button(self.root, text="User Login", width=20,
                           command=lambda : userlogin.main()) # Using Lambda func.
        self.btn2.pack(pady=20)


        self.root.mainloop()

    def onpenSignupPage(self):
        signup.main()

obj = main()

# Lambda function -> Single line function -> anonymous function