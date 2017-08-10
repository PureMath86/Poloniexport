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
