# Simple foreign exchage
A command-line tool to convert currencies. It depends on [Currency Coverter
API](https://www.currencyconverterapi.com/)

## Dependencies
- Python3
- python3-pip
- [poetry](https://github.com/python-poetry/poetry)

## Install (Only tested on Linux)
```bash
make install
```
## Install windows (needs to be run as Administrator)
```
Setup.ps1
```

## First time use
- Login on [Currency Converter API](https://www.currencyconverterapi.com/)
- Get your free/paid API_KEY
- Execute and follow the instructions:

```bash
cash 1 usd eur
#api_key (example): 05b811110dfe4133ff1f
#output (With current values): 
#USD 1.00 to EUR: 0.89
```

You will be asked for your API_KEY only once.

# Run
When running, the tool takes your first currency as your primary currency.

### Multiple currencies

```bash
cash 1 usd eur gbp
#output (With current values): 
#USD 1.00 to EUR: 0.89
#USD 1.00 to GBP: 0.80
```

### Calculate value on the way
You can also make runtime simple calculations like:

```bash
cash '12*2+24' usd eur
#output (With current values): 
#USD 48.00 to EUR: 42.65
```
