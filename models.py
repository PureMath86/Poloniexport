import datetime
import copy

class Trade():
    def __init__(self, currencyPair, trade):
        self.currencyPair = currencyPair
        self.orderNumber = int(trade['orderNumber'])
        self.date = datetime.datetime.strptime(trade['date'], '%Y-%m-%d %H:%M:%S')
        self.type = trade['type']       
        self.amount = float(trade['amount'])
        self.entry = float(trade['rate'])

        if self.type == 'buy':
            paid = float(trade['total'])
            self.amount = self.amount*(1.0-float(trade['fee'])) # Fee manually applied
            self.entry = paid/self.amount

        if self.type == 'sell': 
            made = float(trade['total']) # Fee is already applied          
            self.entry = made/self.amount

    def __add__(self, other):
        if self.type != other.type:
            raise TypeError("Can only combine like types")

        new = copy.deepcopy(self)
        new.date = min(self.date, other.date)
        new.amount = self.amount+other.amount
        new.entry = (self.entry*self.amount+other.entry*other.amount)/new.amount
        return new

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return "Trade ID: {0} {1}: {2} {3} @ {4} on {5}".format(int(self.orderNumber),
                                                                self.currencyPair,
                                                                self.type,
                                                                self.amount,
                                                                self.entry,
                                                                self.date)