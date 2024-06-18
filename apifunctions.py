import requests

def validateCoinSymbol(symbol):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=inr"
    x = requests.get(url)
    data = x.json()
    if "INR" in data:
        return True
    else:
        return False
#---------------- ----------------------------------------------------------------------------

def getWatchlistData(coinlst):
    #coinlst = coinstr.split(',')
    print(coinlst)
    coinstr = "".join(i+',' for i in coinlst)
    coinstr = coinstr[:-1]
    print(coinstr)
    mylist = []
    url = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={coinstr}&tsyms=inr"
    x = requests.get(url)
    data = x.json()
    #print(data)
    for i in coinlst:
        mainData = data["RAW"][i]['INR']
        d = {
            "symbol":i ,
            "price": mainData["PRICE"] ,
            "24high": mainData["HIGH24HOUR"] ,
            "24low": mainData["LOW24HOUR"] ,
            "supply": mainData["SUPPLY"] ,
            "marketcap" : mainData["MKTCAP"]
        }
        mylist.append(d)
    return mylist
    #print(mylist)
#x='BTC,ETH,USDT,USDC,BNB,BUSD,XRP,ADA,SOL,DOGE,DAI,DOT,TRX,SHIB,MATIC,AVAX,UNI,LEO,WBTC,LTC,FTT,CRO,LINK,XLM,ATOM,NEAR,XMR,ALGO,ETC,BCH,ICP,VET,FLOW,MANA,SAND,XTZ,HBAR,APE,EGLD,AAVE,FIL,TUSD,QNT,THETA,AXS,HNT,BSV,EOS,USDP,KCS,ZEC,MKR,BTT,USDN,OKB,XEC,MIOTA,USDD,RUNE,HT,GRT,KLAY,CHZ,FTM,NEO,CRV,BAT,PAXG'
#y=['mana','btc','anb']
#getWatchlistData(y)
#------------------------------------------------------------------------------------------------

#
def news():
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    x = requests.get(url)
    result = x.json()
    lst = []
    for i in range(0,len(result)):
        maindata = result["Data"][i]
        l = {
            'title':maindata["title"]
        }
        # print(l)
        lst.append(l)
    #print(lst)
    return lst
# news()

#-------------------------------------------------------------------------------------------------------------------
def allcoindata(coinstr):
    coinlst = coinstr.split(',')
    url = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={coinstr}&tsyms=inr"
    mylist = []
    x = requests.get(url)
    data = x.json()
    # print(data)
    for i in coinlst:
        mainData = data["RAW"][i]['INR']
        d = {
            "symbol": i,
            "price": mainData["PRICE"],
            "24high": mainData["HIGH24HOUR"],
            "24low": mainData["LOW24HOUR"],
            "supply": mainData["SUPPLY"],
            "marketcap": mainData["MKTCAP"]
        }
        mylist.append(d)
    #print(mylist)
    return mylist
#allcoindata('BTC,ETH,USDT,USDC,BNB,BUSD,XRP,ADA,SOL,DOGE,DAI,DOT,TRX,SHIB,MATIC,AVAX,UNI,LEO,WBTC,LTC,FTT,CRO,LINK,XLM,ATOM,NEAR,XMR,ALGO,ETC,BCH,ICP,VET,FLOW,MANA,SAND,XTZ,HBAR,APE,EGLD,AAVE,FIL,TUSD,QNT,THETA,AXS,HNT,BSV,EOS,USDP,KCS,ZEC,MKR,BTT,USDN,OKB,XEC,MIOTA,USDD,RUNE,HT,GRT,KLAY,CHZ,FTM,NEO,CRV,BAT,PAXG')