# Poloniexport
<i>Compiles trading history into a simple and accurate report</i>

## Features
- Merges order spreads into single trades
- Calculates average entry/exit price including fees
- Estimates exit price and close date based on fifo method
- Adds additional metrics like profit and performance

## Quick Use
```python
git clone https://github.com/Crypto-AI/Poloniexport
cd Poloniexport
pip install -r requirements.txt
python poloniexport.py 
```

## Examples
#### Basic Usage
```python
import poloniexport

history = poloniexport.exportTrades(key, secret)
history.to_csv('history.csv')
```
```text
          date   orderNumber currencyPair  type         amount         entry         size
0   2017-03-22   10760836430     BTC_GAME   buy     351.555490  2.352728e-04     0.082711
1   2017-03-22   10761135131     BTC_GAME   buy     177.250720  2.375434e-04     0.042105
2   2017-03-23    4534228383       BTC_SC   buy  798000.000000  5.714285e-07     0.456000
3   2017-03-26    2237705070    BTC_BURST   buy  250141.585775  1.423559e-06     0.356091
4   2017-03-26   10902972152     BTC_GAME  sell     140.597354  3.472099e-04     0.048817
5   2017-03-26   10903012112     BTC_GAME  sell      86.188810  3.469999e-04     0.029908
6   2017-03-26    7920304929      BTC_DCR   buy      18.138713  1.494883e-02     0.271153
```
