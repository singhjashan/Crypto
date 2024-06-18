from tkinter import *
import tree_veiw
import tkinter.messagebox as msg
from connection import Connect
import changePass
import coins

class main:
    def __init__(self, userID, username):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('User Dashboard')

        self.username = username
        self.userID = userID

        self.rootMenu = Menu(self.root)  # Main Menu
        self.root.config(menu=self.rootMenu)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)   # Sub Menu
        self.rootMenu.add_cascade(label="Profile", menu=self.profileMenu)
        self.profileMenu.add_command(label="Change Password",command= lambda : changePass.main(userID))
        self.profileMenu.add_command(label="Logout",command= lambda : self.root.destroy())


        self.profileMenu = Menu(self.rootMenu, tearoff=0)  # Sub Menu
        self.rootMenu.add_cascade(label="Crypto", menu=self.profileMenu)
        self.profileMenu.add_command(label="coins", command=lambda: coins.main(userID))

        self.rootMenu.add_command(label="API",command=lambda : tree_veiw.main(userID))



        self.lb = Label(self.root, text=f"Welcome {username}", font=('arial', 28, 'bold'))
        self.lb.pack()

        self.root.mainloop()

# obj = main(2,'dfg')