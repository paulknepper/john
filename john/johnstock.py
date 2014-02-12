# johnstock.py -- demo on pulling yahoo finance csv
import csv
import sys
from urllib.error import HTTPError
from urllib.request import urlopen
from datetime import date

"""
Use python 3 for this script; this just pulls a stock based on a ticker
symbol and lets you go line by line to see how the data is formatted.

Ordinarily you would parse this apart into something usable for your
program to digest.  Just showing here how to get the raw data...the 
retrieval date of August 19, 2004 is arbitrary and can be changed as part 
of the URL.  Also, note that Yahoo's url schema numbers months from 0,
thus January = 0, August = 7, December = 11, etc.

Updated to run with one command: python3 johnstock.py <ticker>
"""
TODAY = date.today()

def stockcheck(ticker=sys.argv[1] if len(sys.argv) > 1 else ''):
    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&d=%s&e=%s&f=%s&\
g=d&a=7&b=19&c=2004&ignore=.csv"
    if not ticker:
        # No ticker passed at command line, ask for one
        print("""
Enter a ticker symbol and retrieve stock data from as far back as August 
19, 2004.  Then iterate line by line to view what the data looks like.
        """)
        ticker = input("Enter a valid ticker symbol: ")
    try:
        response = urlopen(url % (ticker.upper(), TODAY.month-1, TODAY.day,
            TODAY.year))
    except HTTPError:
        print("%s isn't a real ticker. I can't let you do that, John."
                % ticker.upper())
        sys.exit()
    
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

if __name__ == '__main__': stockcheck() 
