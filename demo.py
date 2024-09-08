from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 4002, clientId=1)

instrument = Future()
instrument.exchange = 'GLOBEX'
instrument.currency = 'USD'
instrument.symbol = 'MNQ'
instrument.localSymbol = 'MNQZ1'


        
bars = ib.reqHistoricalData(
    instrument, endDateTime='', durationStr='7 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas data frame (pandas needs to be installed):
df = util.df(bars)
print(df)
