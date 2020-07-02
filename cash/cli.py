from __future__ import print_function, unicode_literals
import json
import argparse
from pathlib import Path
import os.path
import yaml
from . import api
from . import install


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def parse_args():
    parser = argparse.ArgumentParser(prog='cash', usage='%(prog)s [amount] [currencies...]')
    parser.add_argument("amount", metavar='amount', nargs=1, help="Amount can be float (1.2) or a string operation('12*23')")
    parser.add_argument("currencies", nargs='+', metavar='currencies', help="COP USD JPY")
    args = parser.parse_args()
    if args.amount is None or args.currencies is None or len(args.currencies) <= 1:
        parser.print_help()
    return args


def run():
    args = parse_args()
    config = install.load_or_install()
    client = api.create_api_client()
    params = {'apiKey': config['api_key'], 'q': join_currencies(args.currencies) }
    response = client._('convert').get(query_params=params)
    results = json.loads(response.body)['results']
    evaluated = eval(args.amount[0])
    header = "%s %s" % (args.currencies[0].upper(), format(args.currencies[0], evaluated))
    for key, value in results.items():
        calculated = value['val'] * evaluated
        text="%s%s to %s:%s %s%s%s" % (color.BOLD, header, value['to'], color.END, color.GREEN, format(value['id'], calculated), color.END)
        print(text)


def format(identifier, value):
    return "{:,.6f}".format(value) if "BTC" in identifier.upper() else "{:,.2f}".format(value)

def join_currencies(currencies):
    result=[]
    for currency in currencies[1:len(currencies)]:
        result.append("%s_%s" % (currencies[0].upper(), currency.upper()))
    return ",".join(result)

