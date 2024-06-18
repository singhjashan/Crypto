from tkinter import *
from connection import Connect
from apifunctions import validateCoinSymbol
import tkinter.messagebox as msg

class main:
    def __init__(self, userID):
        self.root = Tk()
        self.userID = userID
        self.root.geometry('600x600')
        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.lb = Label(self.root, text='Add Coin', font=('arial', 20, 'bold'))
        self.lb.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=20)

        self.lb1 = Label(self.f, text="Enter Coin Symbol", font=('arial', 14))
        self.lb1.grid(row=0, column=0, pady=10, padx=5)

        self.txt1 = Entry(self.f, font=('arial', 14))
        self.txt1.grid(row=0, column=1, pady=10, padx=5)

        self.btn = Button(self.f, text="Submit", font=('arial', 14), command=self.saveCoin)
        self.btn.grid(row=0,column=2, pady=10, padx=5)

        self.list = Listbox(self.root, font=('arial', 14), width=30)
        self.list.pack(pady=10)
        self.getValues()

        self.root.mainloop()

    def getValues(self):
        q = f"select symbol from watchlist where user_id='{self.userID}'"
        self.cr.execute(q)
        result = self.cr.fetchall()
        print(result)
        coins = []
        for i in result:
            print(i)
            coins.append(i[0])

        self.list.delete(0,'end')

        for i in range(0,len(coins)):
            self.list.insert(i, coins[i])


    def saveCoin(self):
        self.coin = self.txt1.get().upper()
        result = validateCoinSymbol(self.coin)
        if result is False:
            msg.showwarning("Warning", "Invalid Coin",parent=self.root)
        else:
            q = f"insert into watchlist values (null, '{self.coin}', '{self.userID}')"
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo("","coin has been added",parent=self.root)
            self.getValues()

# obj = main(2)
