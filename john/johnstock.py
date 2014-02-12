# johnstock.py -- demo on pulling yahoo finance csv
import csv
import sys
from urllib.error import HTTPError
from urllib.request import urlopen

"""
Use python 3 for this script; this just pulls a stock based on a ticker
symbol and lets you go line by line to see how the data is formatted.

Ordinarily you would parse this apart into something usable for your
program to digest.  Just showing here how to get the raw data...the 
retrieval date of July 19, 2004 is arbitrary and can be changed as part of
the URL.
"""

def main():
    print("""
Enter a ticker symbol and retrieve stock data from as far back as July 19,
2004.  Then iterate line by line to view what the data looks like.
""")

    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&d=1&e=12&f=2014&\
g=d&a=7&b=19&c=2004&ignore=.csv"

    ticker = input("Enter a valid ticker symbol: ")
    try:
        response = urlopen(url % ticker.upper())
    except HTTPError:
        print("I can't let you do that, John. Enter a real ticker.")
        sys.exit()
    
    input("Press enter to parse data")
    # Note below probably very ugly way of doing this. Could have built
    # a couple generators to save memory and do same thing as reader.
    reader = csv.reader(response.read().decode().split('\n'))
    for line in reader:
        print(line)
        go = input("Press enter to continue or 'q' to quit. ")
        if go == 'q':
            break
    print("That's all there is...goodbye, John.")

if __name__ == '__main__': main()
