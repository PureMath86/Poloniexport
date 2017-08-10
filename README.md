# Poloniexport
<i>Compiles trading history into a simple and accurate report</i>

## Features
- Merges order spreads into single trades
- Calculates average entry/exit price including fees
- Estimates exit price and close date based on fifo method
- Adds additional metrics like profit and performance

## Install
```text
git clone https://github.com/Crypto-AI/Poloniexport
cd Poloniexport
pip install -r requirements.txt
```

## Examples
#### Basic Usage
```python
import poloniexport

history = poloniexport.exportTrades(key="", secret="")
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

#### Advanced Usage
```python
import poloniexport

history = poloniexport.exportTrades(key="", secret="", advanced=True, specificMarket='BTC')
history.to_csv('history.csv')
```
```text
          date   orderNumber currencyPair type         amount         entry      size         exit       close       profit performance
0   2017-04-23    3104489431     BTC_EMC2  buy   13243.563694  8.542896e-06  0.113138      7.5e-06  2017-05-01   -0.0138117    -12.2078
1   2017-04-23    3134173721      BTC_FLO  buy     230.573538  1.343354e-05  0.003097    1.385e-05  2017-04-27  9.60227e-05     3.10009
2   2017-04-23    4981570593       BTC_SC  buy  299250.000000  6.215539e-07  0.186000      6.9e-07  2017-04-25    0.0204825     11.0121
3   2017-04-23    3134397497      BTC_FLO  buy       7.936029  1.347273e-05  0.000107    1.385e-05  2017-04-27  2.99398e-06     2.80021
4   2017-04-23    3134440454      BTC_FLO  buy    6750.743374  1.347022e-05  0.090934    1.385e-05  2017-04-27   0.00256379      2.8194
5   2017-04-25   12778307939     BTC_GAME  buy     609.971377  8.512068e-04  0.519212   0.00148541  2017-06-06     0.386848     74.5067
6   2017-04-25   12791685548     BTC_GAME  buy     266.035531  7.749675e-04  0.206169   0.00148541  2017-06-06     0.189004     91.6742
7   2017-04-30   11316867966      BTC_DCR  buy      20.391012  1.182465e-02  0.241117
8   2017-05-01    4227197614      BTC_HUC  buy    2562.061892  3.855784e-05  0.098788
9   2017-05-01   13024328801      BTC_LBC  buy    1997.000000  6.239359e-05  0.124600

```
