#

from tkinter import *
import connection
import tkinter.ttk
from apifunctions import *
class main :
    def __init__(self,userID):
        self.root = tkinter.Tk()
        self.root.state("zoomed")
        self.userID = userID
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()

        self.t1 = tkinter.ttk.Treeview(self.root,columns=('symbol','price',"24high",'24low','supply','marketcap'))
        self.t1.heading("symbol",text="Symbol")
        self.t1.heading("price",text="Price")
        self.t1.heading("24high",text="Increase in 24 hours ")
        self.t1.heading("24low", text="Decrease in 24 hours ")
        self.t1.heading("supply", text="Supply")
        self.t1.heading("marketcap", text="Marketcap")
        self.t1["show"]="headings"
        # self.getvalues()
        self.allcoin()
        self.lb3 = Label(self.root, text="All Coin Data", font=('arial', 26)).pack(pady=10)

        self.t1.pack(expand=True, fill='both')
        self.root.mainloop()

    def allcoin(self):
        data = allcoindata('BTC,ETH,USDT,USDC,BNB,BUSD,XRP,ADA,SOL,DOGE,DAI,DOT,TRX,SHIB,MATIC,AVAX,UNI,LEO,WBTC,LTC,FTT,CRO,LINK,XLM,ATOM,NEAR,XMR,ALGO,ETC,BCH,ICP,VET,FLOW,MANA,SAND,XTZ,HBAR,APE,EGLD,AAVE,FIL,TUSD,QNT,THETA,AXS,HNT,BSV,EOS,USDP,KCS,ZEC,MKR,BTT,USDN,OKB,XEC,MIOTA,USDD,RUNE,HT,GRT,KLAY,CHZ,FTM,NEO,CRV,BAT,PAXG')
        for i in range(len(data)):
            self.t1.insert("", index=i, values=list(data[i].values()))



    def getvalues(self):
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
        for j in range(len(results)):
            #print(list(results[j].values()))
            self.t1.insert("",index=j,values=list(results[j].values()))

#-------------------------------------------------------------------------------------------------#
#main(2)