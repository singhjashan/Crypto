from tkinter import *

import changePass
import coins
import tree_veiw
from connection import Connect
import tkinter.ttk
from apifunctions import getWatchlistData,news,validateCoinSymbol
import tkinter.messagebox as msg

class main:
    def __init__(self, userID):
        self.root = Toplevel()
        self.userID = userID
        self.conn = Connect()
        self.cr = self.conn.cursor()
        self.root.state('zoomed')






        style = tkinter.ttk.Style()

        style.configure('Treeview', font=('arial', 12), rowheight=30)
        style.configure('Treeview.Heading', font=('arial', 12))

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        self.frame1 = Frame(self.root,  width=screenWidth, height=screenHeight/2)
        self.frame2 = Frame(self.root,  width=screenWidth, height=screenHeight/2)
        self.frame1.pack(pady=10, padx=10)

        self.lb2 = Label(self.frame2, text='My Watchlist', font=('arial',26)).pack(pady=10)

        self.t1 = tkinter.ttk.Treeview(self.frame2,columns=('symbol','price',"24high",'24low','supply','marketcap'))
        self.t1.heading("symbol",text="Symbol")
        self.t1.heading("price",text="Price")
        self.t1.heading("24high",text="Increase in 24 hours ")
        self.t1.heading("24low", text="Decrease in 24 hours ")
        self.t1.heading("supply", text="Supply")
        self.t1.heading("marketcap", text="Marketcap")
        self.t1["show"]="headings"
        self.getWatchlishValues()
        self.t1.pack(expand=True, fill='both', padx=5, pady=10)

        self.frame2.pack(pady=10, padx=10)
        self.frame1.pack_propagate(0)
        self.frame2.pack_propagate(0)

        self.frane11 = Frame(self.frame1, height=screenHeight/2,width=screenWidth/3)

        self.lb1 = Label(self.frane11, text='My Coins', font=('arial',26)).pack(pady=10)

        self.list = Listbox(self.frane11, font=('arial', 14))
        self.list.pack(pady=10, expand=True, fill='both',padx=5)
        self.getCoinsValue()


        self.frane12 = Frame(self.frame1, height=screenHeight/2,width=screenWidth*2/3)

        self.frane11.grid(row=0, column=0, pady=10,padx=5)
        self.frane12.grid(row=0, column=1, pady=10,padx=5)

        self.lb3 = Label(self.frane12, text="Top News", font=('arial',26)).pack(pady=10)

        self.newsList = Listbox(self.frane12, font=('arial', 14))
        self.newsList.pack(pady=10, expand=True, fill='both',padx=10)

        allNews = news()
        print(allNews)
        for i in range(len(allNews)):
            # print(i)
            self.newsList.insert(i, allNews[i]['title'])
        self.frane11.pack_propagate(0)
        self.frane12.pack_propagate(0)






        self.rootMenu = Menu(self.root)  # Main Menu
        self.root.config(menu=self.rootMenu)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)   # Sub Menu
        self.rootMenu.add_cascade(label="Profile", menu=self.profileMenu)
        self.profileMenu.add_command(label="Change Password",command= lambda : changePass.main(userID))
        self.profileMenu.add_command(label="Logout",command= lambda : self.root.destroy())


        # self.profileMenu = Menu(self.rootMenu, tearoff=0)  # Sub Menu
        # self.rootMenu.add_cascade(label="Crypto", menu=self.profileMenu)
        # self.profileMenu.add_command(label="coins", command=lambda: coins.main(userID))

        self.rootMenu.add_command(label="Add Coin",command=lambda : self.addCoinWindow())
        self.rootMenu.add_command(label="API",command=lambda : tree_veiw.main(userID))




        self.root.mainloop()


    def addCoinWindow(self):

        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.lb = Label(self.root1, text='Add Coin', font=('arial', 20, 'bold'))
        self.lb.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=20)

        self.lb1 = Label(self.f, text="Enter Coin Symbol", font=('arial', 14))
        self.lb1.grid(row=0, column=0, pady=10, padx=5)

        self.txt1 = Entry(self.f, font=('arial', 14))
        self.txt1.grid(row=0, column=1, pady=10, padx=5)

        self.btn = Button(self.f, text="Submit", font=('arial', 14), command=self.saveCoin)
        self.btn.grid(row=0,column=2, pady=10, padx=5)

        self.root1.mainloop()


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
            self.getCoinsValue()
            self.getWatchlishValues()


    def getCoinsValue(self):
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

    def getWatchlishValues(self):
        q = f"select symbol from watchlist where user_id={self.userID}"
        self.cr.execute(q)
        result = self.cr.fetchall()
        #print(result)
        coins=[]
        for i in result :
            #print(result)
            coins.append(i[0])
        #print(coins)
        results = getWatchlistData(coins)
        #print(results)

        for k in self.t1.get_children():
            self.t1.delete(k)

        for j in range(len(results)):
            #print(list(results[j].values()))
            self.t1.insert("",index=j,values=list(results[j].values()))



# obj=main(2)