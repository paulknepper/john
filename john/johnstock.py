# johnstock.py -- demo on pulling yahoo finance csv
import csv
import sys
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlencode
from datetime import date

"""
Use python 3 for this script; this just pulls a stock based on a ticker
symbol and lets you go line by line to see how the data is formatted.

Ordinarily you would parse this apart into something usable for your
program to digest.  Just showing here how to get the raw data...the 
retrieval date of January 1, 1940 is arbitrary and can be changed as part 
of the URL.  Also, note that Yahoo's url schema numbers months from 0,
thus January = 0, August = 7, December = 11, etc.

Updated to run with one command: python3 johnstock.py <ticker>

Updated to pull just data from today (or yesterday if market still open
today).  To pull just today, at the command line use the -t flag:

$ python3 johnstock.py -t <ticker>
"""
TODAY = date.today()

def stockcheck(ticker='', dateflag=''):
    base_url = "http://ichart.finance.yahoo.com/table.csv?"
    params = {
            's':'', # stock ticker
            'd':'', # end month as int (Jan == 0)
            'e':'', # end day as int
            'f':'', # end year as int
            'g':'d', # ???
            'a':1, # start month (Jan == 0)
            'b':1, # start day
            'c':1940, # start year
            'ignore':'.csv'
            }
    if not ticker:
        # No ticker passed at command line, ask for one
        print("""
Enter a ticker symbol and retrieve stock data from as far back as August 
19, 2004.  Then iterate line by line to view what the data looks like.
        """)
        ticker = input("Enter a valid ticker symbol: ")
    params['s'] = ticker
    if dateflag == '-t':
        params['a'] = TODAY.month-1
        params['b'] = TODAY.day
        params['c'] = TODAY.year
    url = base_url +  urlencode(params)
    try:
        response = urlopen(url)
    except HTTPError:
        print("%s isn't a real ticker. I can't let you do that, John."
                % ticker.upper())
        sys.exit() # or just naked return?
    
    input("Ticker %s found. Press enter to parse data." % ticker.upper())
    # Note below probably very ugly way of doing this. Could have built
    # a couple generators to save memory and do same thing as reader.
    reader = csv.reader(response.read().decode().split('\n'))
    for line in reader:
        print(line)
        go = input("Press enter to continue or 'q' to quit. ")
        if go == 'q':
            break
    print("That's all there is...goodbye, John.")

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1: stockcheck()
    if len(args) == 2: stockcheck(sys.argv[1])
    if len(args) == 3: stockcheck(sys.argv[2], sys.argv[1])
