#!/usr/bin/env python
# coding: utf8
# called by updateDaylyStockwatch.py

#purpose is to get the csv index data to update the currencies (exchange rates in money dance) FX$CAD/USD
# choice of indexes #of values
# B -CBOE Indexes        305       "Chicago Board of Trade" example BFLY is the Cboe S&P 500 Iron Butterfly Index
# F - Mutual Funds        0
# H - PBOT Indexes        5        "Philadelphia Board of Trade" 
# I Indexes              4482 
# Q Nasdaq               8100
# S S&P Indexes          2490
# X Amex                 2013
# NYSE                   3109
#The download you requested can be performed by the following URL:
#https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&date=20180330&exopt=N&ex=I&ats=N&id=userName&pw=password
#Note: If you leave out the &date=<date> part you will get the most recent date available. Otherwise set it to the specific date you want.
#This URL will always give you the most recent date:
#https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=I&ats=N&id=userName&pw=password
# the above was with I selected &ex=I , should use https
# the I Indexes contains the currencys FX$.... FX$CAD/USD is 0.7757   FX$USD/CAD is 1.28825 there are around 100 CAD conversions in this file


import sys
import urllib2
import urllib
import Passwords # defines UserName and PassWord

def main():
        print("fetchhtmlDaylySyockwatchIndexs.py started")
        #execfile("Passwords.py") # defines UserName and PassWord


        file2 = open('/opt/moneydance/scripts/tmp/StockwatchDay/indexs.csv', 'wb')
        print ("opening", file2)

        url = 'https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=I&ats=N&id=' + Passwords.UserName + '&pw=' + Passwords.PassWord


        print '39 url ',url
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0 SeaMonkey/2.49.1 Slackware/14.2')]


        req = urllib2.Request(url)
        try:
                response = opener.open(url)
        except urllib2.URLError as e:
                if hasattr(e, 'reason'):
                        print '49 We failed to reach a server.'
                        print '50 Reason: ', e.reason
                if hasattr(e, 'code'):
                        print '52 The server couldn\'t fulfill the request.'
                        print '51 Error code: ', e.code
        else:
                print '55 responce ', response.headers
                webContent = response.read()           # just got a single line of column headings when the market was closed.for days close request
                #  print 'length=', len(webContent)       #  got  1932 lines when I specified a day
                #  print webContent


                file2.write(webContent) # this function does not return anything useful
                file2.close()
                print "63 Done fetchhtmlDaylyStockwatchIndexs.py"

if  __name__ == '__main__': # was started with execfile
  print "fetchhtmlDaylySyockwatchIndexs.py executed by execfile"
  main()
else:   # was started by import
  print "fetchhtmlDaylySyockwatchIndexs.py loaded by import"
