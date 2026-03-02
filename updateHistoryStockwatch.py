#!/usr/bin/env python2
# coding: utf8
# called by runscripts
import sys
import time
import os

# the imported data files should be manually down loaded from www.stockwatch.com and be placed in the directory /opt/moneydance/scripts/tmp/Stockwatch
# https://www.stockwatch.com/Quote/Download
# goto www.stockwatch.com and click on quotes->download quotes-> enter Symbol -> submit->select year -> select data.csv for the file name -> submit
# or goto https://www.stockwatch.com/ enter a symbol , pick Historical , pick the year. pick Download File Name data.csv ->submit , save it
# save the file to /opt/moneydance/scripts/tmp/Stockwatch
# or use dolphin to drag it from Downloads to the above
# you must have a stockwatch account and be logged in, you may need to change the file name to data2.csv or any name that ends in .csv
# one file per security . can be all the daily close values for that security for one year . file name can be anything that ends in .csv
# this program processes all the .csv files in this directory and moves them to /opt/moneydance/scripts/tmp/Done

# Tested on Tsx , New York and Canadian Mutual funds 
# The Canadian mutual fund symbols that stockwatch uses are different than what is used by most sites . 
# the StockwatchSymbols list in definitions.py must be filled in to convert mutual fund  symbols
# example 'TML202':'BIF*CDN',  my moneydance symbol is TML202 . Stockwatch uses BIF*CDN for this same fund.
# stock symbols are automaticly converted by this program from AAA.AA.A to AAA-AA-A-T or AAA-AA-A-N
# ie the stockwatch dots are converted to GlobeInvestor dashes and the exchange is tacked on the end -T is TSX -N is NYSE in newyork
# <ticker>	<date>	   <exchange>	<open>	<high>	<low>	<close>	<change>	<vol>	<trades>
# BRN*GLO	20141117	F	10.9856	10.9856	10.9856	10.9856	 -0.01	          0	0
# the above is the standard ASCII csv format produced by Stockwatch
# 
# Exchange codes used by Stockwatch
# Code 	Region 	Exchange
# U 	US 	Special code that matches any US symbol
# C 	Canada 	Special code that matches any Canadian symbol
# Z 	US 	Composite feed including the New York and American exchanges -- confirmed GlobeInvestor uses -N
# Q 	US 	Nasdaq, OTCBB, Pink Sheets and Other OTC
# O 	US 	OPRA - US Options
# S 	US 	S&P indexes
# P 	US 	PBOT indexes
# B 	US 	CBOE indexes
# I 	US 	Non-exchange and other indexes such as Dow Jones, Russel, Longon Gold Fix
# T 	Canada 	TSX - Toronto Stock Exchange -- confirmed same as GlobeInvestor
# V 	Canada 	TSX Venture Exchange
# M 	Canada 	Montreal Exchange
# C 	Canada 	CSE
# F 	Canada 	Canadian Mutual Funds  -- confirmed
# E is NEO

# on the developers console run ----->>>execfile("updateHistoryStockwatch.py") or use runscripts.py AFTER you down load the history
# issue #1 stockwatch doesn't use fundserv mutual fund numbers so we have to convert them . example BIP151 = BRN*GLO
# issue #3 it seems to overload moneydance and lock it up. added a sleep to slow it down. but still locks uo. maybe make sure you don't have a graph on display in moneydance use the reminders page
# the above seemed to work . I removed the sleep .. looks like moneydance was trying to update the view as the history was being updated.
# MD 2019 seems to not have this problem

#class updateHistoryStockwatch:
def main():
   import glob
   import sys
   import definitions

   
  
   def setPriceForSecurity(symbol, price2, dateint , volume2 , high2 , low2 ): # this version is the latest Dec 29 2017
     import scriptsIPC

     root = scriptsIPC.MoneyDance.getRootAccount()
  ##   currencies = root.getCurrencyTable() fix from roywsmith
     AcctBook = root.getBook() 
     currencies = AcctBook.getCurrencies()
     if price2 != 0:
       price2 = 1/price2
     else:
       print "Error Zero Price found Skipping it"
       return
     if low2 != 0:
       low2   = 1/low2
     else:
       low2 = price2
     if high2 != 0:
       high2  = 1/high2
     else:
       high2 = price2 
     security = currencies.getCurrencyByTickerSymbol(symbol) #returns a CurrencyType
     if not security:
       print "No security with symbol/name: %s"%(symbol)
       return
     if dateint:
       snapshot = security.setSnapshotInt(dateint, price2) # this returns a CurrencyType.Snapshot
       security.setUserRate(price2)
       snapshot.setDailyVolume (long(volume2) )
       snapshot.setUserRate ( price2 )
       snapshot.setUserDailyHigh ( high2 )
       snapshot.setUserDailyLow ( low2 )
       security.setSnapshotInt(dateint, price2).syncItem() # added this April 19 2019 for change in MD2019 see note below
     else:  
       print "88 No Date for symbol/name: %s"%(symbol)
     
#     print price2,volume2,high2,low2
#     print "91 Successfully set price for %s"%(security)
 
# words of wisdom from Sean Reilly on Jan 02 2019 
#Ah yes, sorry about that. We moved a while ago to requiring a sync/save call for snapshots to prevent an overflow of history entries which were coming from 
#calls to create snapshots which weren't meant to be saved. Anyway, you should just change any calls to security.setSnapshotInt(dateint, price) to 
#change any calls to security.setSnapshotInt(dateint, price) to invoke syncItem() on the result: security.setSnapshotInt(dateint, price).syncItem().
#I'll update the sample code now too.
   
	    	      
   
   files = glob.glob('/opt/moneydance/scripts/tmp/'+'Stockwatch/*.csv') # open the directory to be processsed
   
#   print files

   counter = 0
   
   for fle in files:
##    ++counter # Python doesn't support ++
    counter += 1
    fin = open(fle,'r')
#   <ticker>,<date>,<exchange>,<open>,<high>,<low>,<close>,<change>,<vol>,<trades> ... this is what a data.csv file from stockwatch looks like

    print '117 fle ', fle
    sym = fin.readline() # disgard the first line its a header
    print '119 header ',sym            # print the header .. need to check this header
    if sym.count("ticker") == 0:
       fin.close()
       dest = fle
       dest = dest.replace('/',' ')
       dest = dest.strip()
       lst = dest.split()
       filename = lst[len(lst)-1]
#   print filename
       print '128 Moving file to:' + '/opt/moneydance/scripts/tmp/'+'Done/'+filename
       os.rename(fle, '/opt/moneydance/scripts/tmp/'+'Done/'+filename)  # move it out ... maybe its a left over from Stock-update-Stockwatch.py
       continue # the for loop
#       raise Exception ("No ticker in csv File")

    while 1:
       sym = fin.readline()
       if len(sym) <= 0:
         break
#       sym = sym.replace(',',' ') # strip out all the comma s
     
       lst = sym.split(",") # chop it up into 10 fields    

   #  print lst[0] #ticker
   #  print lst[1] #date
   #  print lst[2] #exchange
   #  print lst[3] #open
   #  print lst[4] #high
   #  print lst[5] #low
   #  print lst[6] #close
   #  print lst[7] #change
   #  print lst[8] #volume
   #  print lst[9] #trades
# the mutual funds have been removed from everything except this program so its a todo.
       if lst[2] == 'F':
          print '152 Its a Mutual Fund' # so we need to look up the symbol
          tickerSym = None
          Description = lst[0]
#        Description = Description[:10] #20 was too long try 10 characters
#        print "DESC=", Description
     
          for fundsym , fundname in definitions.StockwatchSymbols.items():  # use the list in definitions to look up the ticker ... this list is gone
#        print fundsym , fundname
#        print len(fundname)
	     if len(fundname) <= 0: break
	     if  fundname.count (Description) > 0:
#	     print "found it", fundsym ,fundname
	       tickerSym = fundsym
#	     print "found tickerSym=",tickerSym
	       break
          if tickerSym == None:	
	     print "168 updateHistoryStockwatch.py Ticker symbol Look up failed ------------------------"
	     break
       else : 
         tickerSym = lst[0] # need to add a -T to the end of it to match the Globeinvestor standard
         tickerSym = tickerSym.replace('.','-')  #  sym = sym.replace(')',' ')  Stockwatch uses dots but GlobeInvestor uses dashes
         if lst[2] == 'T':
             tickerSym = tickerSym+'-T' # if its the TSX
         if lst[2] == 'Z':    
             tickerSym = tickerSym+'-N' # if its the NewYork  Stockwatch=Z and GlobeInvestor=N differ here  
         if lst[2] == 'V':    
             tickerSym = tickerSym+'-X' # Toronto Venture Exchange Stockwatch=V GlobeInvestor=X  TMX=TSXV   
         if lst[2] == 'E':    
             tickerSym = tickerSym+'-NEO' # NEO ATS  TMX=shows both AQL and AQN (AQL is high speed normal trading .AQN is NEO(slow filtered trading))
                                          # stockwatch shows them as E and U , GlobeInvestor just blows up.
             
       volume = long (lst[8])  
       high = float ( lst[4] )
       low =  float  ( lst[5])
# --------------- looks like the date is already in the right format 
     
       number = int( lst[1] ) # this is the date
#     print tickerSym,float(lst[6]),number,volume,high,low
       setPriceForSecurity(tickerSym,float(lst[6]),number , volume , high , low )            # this is a local function
       print '191 ',tickerSym,float(lst[6]),number,volume,high,low
#      time.sleep(1) # moneydance was freezing up this seemed to help. moneydance will not run while this program is running?? (around 250 values per year per symbol.
#     break 
#   print fle+" time to move it"  # fle has a full path
    fin.close()
    dest = fle
    dest = dest.replace('/',' ')
    dest = dest.strip()
    lst = dest.split()
    filename = lst[len(lst)-1]
#   print filename
    print '202 Moving file to '+'/opt/moneydance/scripts/tmp/'+'Done/'+filename
    os.rename(fle, '/opt/moneydance/scripts/tmp/'+'Done/'+filename)
    # end while
   #end for
   if counter == 0:
     print"There are no files to process"
     print"You have to down load them manually"
     print"Save them as /opt/moneydance/scripts/tmp/Stockwatch/anyname.csv"
     print"One file for each Symbol" 
     print"One year of Closing prices in each file"
#     sys.stderr.write("this is a test\n") # didn't work
#     print >>sys.stderr, "another test" # didn't work
#     sys.stdout.write("yet another test\n") # didn't work
#     time.sleep(30)                                        sleep puts moneydance to sleep too 
     #wait = input("PRESS ENTER TO CONTINUE.") # this messed up everything . moneydance froze . had to kill java 
   else:
     print "217 files processed=",counter
     
   print "219 Done updateHistoryStockwatch.py"

if  __name__ == '__main__': # was started with execfile
  print "updateHistoryStockwatch.py executed by execfile"
  main()
else:   # was started by import
  print ("import passed __name__" , __name__)
  print "updateHistoryStockwatch.py loaded by import"
