import pandas as pd
import numpy as np
import calendar
import datetime
import itertools
import operator
import time
import json
import copy
import poloniexapi
import models

def todate(u): return datetime.datetime.utcfromtimestamp(u)
def tounix(d): return calendar.timegm(d.timetuple())

def findTrade(trades, orderNumber):
    return [t for t in trades if t.orderNumber == orderNumber][0]

def addPerformance(trades, currencyPair):
    trades = [t for t in trades if t.currencyPair == currencyPair] 
    buys = [copy.deepcopy(t) for t in trades if t.type == "buy"] 
    sells = [copy.deepcopy(t) for t in trades if t.type == "sell"]
    buys.sort(key=lambda t: t.date)
    sells.sort(key=lambda t: t.date)
    i = 0
    for buy in buys:
        try:
            while buy.amount > sells[i].amount:
                buy.amount -= sells[i].amount
                sells[i].amount = 0
                i += 1
            sells[i].amount -= buy.amount
            buy.amount = 0
            b = findTrade(trades, buy.orderNumber)
            s = findTrade(trades, sells[i].orderNumber)
            b.exit = s.entry
            b.close = s.date.strftime("%Y-%m-%d")
            b.profit = b.amount*b.exit-b.amount*b.entry
            b.performance = ((b.exit-b.entry)/b.entry)*100
        except IndexError:
            pass

end = tounix(todate(time.time())+datetime.timedelta(days=1))
start = 1388534400 # Poloniex was started after 01/01/2014

def exportTrades(key, secret, end=end, start=start, advanced=False, currencyPair='all', specificMarket=False):
    try:
        connection = poloniexapi.Connection(key, secret)
        history = connection('returnTradeHistory', args={'currencyPair': currencyPair, 'start': start, 'end': end})
    except Exception as e:
        raise  RuntimeError('Poloniex Error: {0}'.format(e))

    if currencyPair != 'all':
        history = {currencyPair: history}    

    # Filter a specific market if requested
    if specificMarket:
        history = {k: history[k] for k in history if k.split('_')[0] == specificMarket}
    
    # Load all trades into Trade objects
    trades = []
    for pair in history:
        for trade in history[pair]:
            t = models.Trade(pair, trade)
            trades.append(t)

    # Group trades originating from the same order 
    gettr = operator.attrgetter('orderNumber')
    trades = [list(g) for k, g in itertools.groupby(sorted(trades, key=gettr), gettr)]

    # Add these individal trades together to form one averaged trade
    trades = [sum(trade) for trade in trades]

    # Sort all trades by their date
    trades.sort(key=lambda x: x.date)

    # Add exit prices, close dates, and trade performance
    if advanced:
        pairs = set([t.currencyPair for t in trades])
        for pair in pairs:
            addPerformance(trades, pair)       
        history = pd.DataFrame(columns=["date", "orderNumber", "currencyPair", "type", "amount", "entry", "size", "exit", "close", "profit", "performance"])
        trades = [t for t in trades if t.type=="buy"]
    else:
        history = pd.DataFrame(columns=["date", "orderNumber", "currencyPair", "type", "amount", "entry", "size"])

    for t in trades:
        t.date = t.date.strftime("%Y-%m-%d")
        t.size = t.amount*t.entry
        row = pd.read_json(json.dumps(t.__dict__), typ='series')
        history = history.append(row, ignore_index=True).replace(np.nan, '')
    return history
