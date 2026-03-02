#!/usr/bin/env python
# coding: utf8
# version 2/17/2025

import sys
def lineNo():  return (str(sys._getframe(1).f_lineno) + ' ')
XferCategory = 'Unknown' # will get changed by BANK transactions BMOdescTable
global memo
memo = ''

#class ScotiaInvnew:
def main():

  from time import mktime , localtime ,strftime
  from datetime import datetime
  import BMOdescTable

#  sys.stdout = open ('/dev/pts/3', 'w') # when this cript is started by ScotiaPicker.py stdout gets messed up (a java swing problem)
#  sys.stderr = open ('/dev/pts/3', 'w') # this doesn't seem to work .. need to check the moneydance console

#  execfile("/opt/moneydance/scripts/definitions.py")
#  import AccountNames  # defines accountNames .. the Bank Investment accounts
#  execfile("BondTable.py") # defines BondTable

#  csvfile = "/home/wayne/ScotiaBank/transactionHistory.csv" # this was the old default location for www.ScotiaBank.com file name
#  csvfile = "/home/wayne/Downloads/transactionHistory.csv" # this is where firefox puts them now
#  execfile("selectScotiaBankCsvfile.py") # go get the right csv file in ~/Downloads
#  file3 = open('/opt/moneydance/scripts/tmp/selectScotiaBankCsvfile.txt', 'rb') # this is where the selectScotiaBankCsvfile.py script puts the selected csv file name now
#  print lineNo() + str(file3)
#  csvfile = file3.read()
#  file3.close()

  csvfile = ""
  import selectScotiaBankCsvfile
  selectScotiaBankCsvfile.main() # jan 20 2026
  import scriptsIPC
  logger = scriptsIPC.logger
  csvfile = scriptsIPC.csvFile # selectCIBCcsvfile.py filled this in
  print lineNo() + "Scotia_Inv_new is Processing ", csvfile
  if csvfile == '' or csvfile == None:
     print lineNo() + "csvfile is empty"
     raise Exception (lineNo() + " selectScotiaBankCsvfile is not working")
  logger.info("Starting")


#  list of BONDS & GIC's .. alternate way of doing the Bond Table
# a dictionary of lists .. the items in the list don't have names '
#  BondTable = dict({  a dictionary of lists
#    '5VJYFL0':['ZAG BANK MONTHLY INTEREST GIC',2.95,'2023-03-15',0,0],    
#    '13321LAH1':['CAMECO CORPORATION',3.75,'2022-11-14',246.58,24.99],      
#    '136765BA1':['CANADIAN WESTERN BANK SR UNSECURED',2.924,'2022-12-15',142.60,24.99],    
#    '11257ZAC3':['BROOKFIELD ASSET MGMT INC MED TERM NTS',4.54,'2023-03-31',410.47,24.99],    
#    '303901AZ5':['FAIRFAX FINANCIAL HLDS LTD SR UNSECURED',4.25,'2027-12-06',232.88,24.99],    
#    '51925DBP0':['LAURENTIAN BANK OF CANADA SENIOR DEPOSIT NOTES',3.0,'2022-09-12',3.29,24.99]    
#    })

# the Bond Table has been moved to its own script BondTable.py
# a dictionary of dictionaries  .. each item gets a nice name
#  BondTable = dict({
##    '5VJYFL0':{'desc':'ZAG BANK MONTHLY INTEREST GIC','coupon':2.95,'date':'2023-03-15','accrued':0,'fee':0},
#    '5VJYFL0':{'desc':'DESJARDINS TRUST INC MONTHLY INTEREST GIC','coupon':2.95,'date':'2023-03-15','accrued':0,'fee':0},
#    '13321LAH1':{'desc':'CAMECO CORPORATION','coupon':3.75,'date':'2022-11-14','accrued':246.58,'fee':24.99},
#    '136765BA1':{'desc':'CANADIAN WESTERN BANK SR UNSECURED','coupon':2.924,'date':'2022-12-15','accrued':142.60,'fee':24.99},
#    '11257ZAC3':{'desc':'BROOKFIELD ASSET MGMT INC MED TERM NTS','coupon':4.54,'date':'2023-03-31','accrued':410.47,'fee':24.99},
#    '303901AZ5':{'desc':'FAIRFAX FINANCIAL HLDS LTD SR UNSECURED','coupon':4.25,'date':'2027-12-06','accrued':232.88,'fee':24.99},
#    '51925DBP0':{'desc':'LAURENTIAN BANK OF CANADA SENIOR DEPOSIT NOTES','coupon':3.0,'date':'2022-09-12','accrued':3.29,'fee':24.99},
#    '5W62553'  :{'desc':'BANK OF MONTREAL ANNUAL INTEREST GIC DUE 11/15/2024  INT  2.350% CPN INT   ON    5000 BND REC 11/14/24 PAY 11/15/24' }
#    })


#  PreferedShareTable = dict({ # a dictionary of dictionaries  .. not used
#    'CU-PR-F-T':{'desc':'CDN UTIL 4.5% CUM RDM CU.PR.F','type':'Fixed Cumulative','coupon':4.5,'issue-date':'2013-03-19','series':'CC','first-redem-date':'2018-06-1','first-redem-price':26}, # redemption price drops .25 per year until it reaches $25 on june 1 2022
#    'GWO-PR-S-T':{'desc':'Great West Life Preferred GWO.PR.S','type':'Fixed Non Cumulative','coupon':5.2,'issue-date':'2014-05-22','series':'S','first-redem-date':'2019-06-30','first-redem-price':26}   # redemption price drops .25 per year until it reaches $25 on june 30 2023
#    })


#  from definitions import definitions
#  execfile("/opt/moneydance/scripts/definitions.py") #user.home is /home/wayne --- run jython_info.py to check it out
# the name used by Scotia for mutual funds  carries the fund number in brackets
# used to look up the ticker symbol , given the description used by Scotia Investments only good for processing downloads from Scotia Investments
# so the description needs to be the description used by Scotia Itrade not the description used by moneydance
# if a transaction is missing its ticker .. the ticker can be looked up using this Table .. if the description hasn't changed ....'
# Scotia-Inv.py select-Scotiabank-Inv-file2.py are no longer used . The csv file imported is always /home/wayne/ScotiaBank/transactionHistory.csv


#  ScotiaDescTable = { # these are all mutual funds ?  #moved to ScotiaDescTable.py
#   'TML202':'FRANKLIN BISSETT CDN EQUITY FD (202)',
#   'MFC738':'CUNDILL CANADIAN SECURITY FUND SER C (738)',
#   'BIP151':'BRANDES GLOBAL EQUITY FUND (151)',
#   'FID281':'FIDELITY CANADIAN ASSET ALLOCATION FUND ISC (281)',
#   'BNS344':'SCOTIA SELECTED MAXIMUM GROWTH PORTFOLIO (344)',
#   'BNS361':'SCOTIA MORTGAGE INCOME FUND (361)',
#   'BNS741':'SCOTIA SELECTED BALANCED INCOME & GROWTH PORTFOLIO (741)',
#   'BNS357':'SCOTIA MONEY MARKET FUND (357)',
#   'BMO146':'BMO DIVIDEND FUND (146)',
#   'BMO471':'BMO Select Trust Fixed Income (471)'
#   }

# takes care of some if the simple action remaps
# memo is a global
# processTxnBMO can only handle Buy,Sell,Short,Cover,Dividend,ROC,Interest,DVF,MiscInc,MiscExp,BANK
# the complex remaps are still done inside processTxnBMO
# moneydance only has SELL,BUY,SHORT,COVER,DIVIDEND, DIVIDEND_REINVEST,MISCINC,MISCEXP,Xfr
  def remapActions(action):
    global memo # you can read the global memo without this but not write to it ???
    memo = memo
    newAction = None
    if action == 'DivReinvest' :
        memo = action + ' ' + memo
        action = 'DVF'

    if action == 'Cash in lieu' :  # showed up $7.58 on M&B TNT when it split 1 for 5.75
        memo = action + ' ' + memo
        action = 'Dividend'

    if action == 'Redemption' :
        memo = action + ' ' + memo
        action = 'Sell'

    if action == 'Non resident tax': # from Granite
        memo = action + ' ' + memo
        action = 'MiscExp'

    if action == 'Div' :
        memo = action + ' ' + memo
        action = 'Dividend'

    return action


# given a BOND description try to find the ticker that goes with it.
  def lookupBondTicker(description,table): 
    tickerSym = None
    description = description[:10] # only checking 10 characters
    for ticker in table:
#      print ticker, table[ticker]['desc']
      desc = table[ticker]['desc']
      if len(desc) <= 0: break
      if desc.count(description) > 0:
        print lineNo() + "lookupBond found it in the bond table", ticker
        tickerSym = ticker
        break
    return tickerSym


  def lookupTicker(description,table):
 #     print "Missing ticker symbol, try Looking it up using the description "
    tickerSym = None
    description = description[:14] #20 was too long
#      print "DESC=", description
    for fundsym , fundname in table.items(): 
#      print fundsym , fundname
#      print len(fundname)
	if len(fundname) <= 0: break
	if  fundname.count (description) > 0:
	  print lineNo() + "found it", fundsym ,fundname
	  tickerSym = fundsym
#	print "found tickerSym=",tickerSym
	  break
#    if tickerSym is None:
#	print "Ticker symbol Look up failed ------------------------.  TXN"
    return tickerSym

   
  def str2date(day,month,year): # Scotia ??? the month is already a number Scotia changed something new date format 2025-02-12 for FEB
    from time import mktime , localtime
    monthss = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']    
#   month,day,year = date.strip().split('/')
    month = month.upper()
 #  print month
 #  print day
 #  print year
    index = monthss.index(month)
    index = index + 1
 #  print index	
    a=(int(year),index,int(day), 0, 0, 0, 0, 0, -1)
    x = mktime(a) # returns a float date-time number
    y = localtime(x) # returns a tuple of 9 elements like 'a' above . for use with strftime()
    return y
  
  def str2dateBMO(day,month,year):
    from time import mktime , localtime
#   month,day,year = date.strip().split('/')
 #  print month
 #  print day
 #  print year
    a=(int(year),int(month),int(day), 0, 0, 0, 0, 0, -1)
    x = mktime(a) # returns a float date-time number
    y = localtime(x) # returns a tuple of 9 elements like 'a' above . for use with strftime()
    return y
   
  def mdDate(dateStr):
    dates = dateStr.split('/')
    mm = dates[0]
    if len(mm) < 2:
      mm = '0' + mm
    dd = dates[1]
    if len(dd) < 2:
      dd = '0' + dd
    return int(dates[2] + mm + dd)

# found where the extra CR was coming from ... the amount was the last field in the csv I forgot to pull a CR at the end of the file we could strip the out here
  def mdQty(qtyStr, decimals): # it appears to take a number like (5000.00) and change it to -500000 if decimals are 2
    l = len(qtyStr)
#    print 'qtyStr l decimals',qtyStr,l,decimals # 5000 6 2
    if l == 0:
      return 0
    neg = ''
    md = ''
    frac = ''
    newfrac = ''
    i = 0
    while i < l:
      c = qtyStr[i]
      i = i + 1
      if c == '(':
	neg = '-'
      elif c == '$' or c == ',' or c == ')' or c == '\n' or c == '\r':  # it looks for LF new line 0x0a .. but not \r CR 0x0d added \r
	pass
      elif c == '.':
	frac = qtyStr[i:i+decimals]
	i = 0
	while i < decimals:
	  if i >= len(frac):
	    break
	  c = frac[i]
	  if c == ')' or c == '\n' or c == '\r': # added /r
#            print "frac c=)or \\n" , c
	    newfrac = newfrac + '0'
	  else:
#	  	print "frac c=",c
	    newfrac = newfrac + c
	  i = i + 1
	break
      else:
	md = md + c
#      	print 'mdQty md=' , md
    while len(newfrac) < decimals:
      newfrac = newfrac + '0'         
#    print 'neg', neg # sign
#    print 'md' , md
#    print 'newfrac',newfrac
#    print neg + md + newfrac  # These all look clean ???? will try scubbing the string
#    newString = neg + md + newfrac
#    newString = newString.strip()
#    print newString
#    print ":".join("{:02x}".format(ord(c)) for c in newString) # worked 35:30:30:30:0d:30:30  we got an extra CR carriage return from some where end of md ?
#    print ":".join("{:02x}".format(ord(c)) for c in "500000")  # worked 35:30:30:30:30:30
#    print "md"
#    print ":".join("{:02x}".format(ord(c)) for c in md )  # 35:30:30:30:0d yes its in md
#    print "qtyStr"
#    print ":".join("{:02x}".format(ord(c)) for c in qtyStr ) # 35:30:30:30:0d:0a  both CR and LF are fed to us
    x = long(neg + md + newfrac) #ValueError: invalid literal for long() with base 10: '500000' ...  makes no sense
#    x = long(newString) # failed
#    x = long(float(newString)) # ValueError: invalid literal for float: 500000
#    x = long(float(str(newString))) ValueError: invalid literal for float: 500000
#    x = long("500000")  # this worked ???????????????????????????????????????????????????????????????
#    print 'mdQty returning integer=',x
    return x
  
# The currencies within Moneydance are held within a CurrencyTable. 
# This will be populated with all predefined currencies, 
# not just the ones you have selected. In addition there are entries for securities. 
# If one of your investment accounts holds shares for say, IBM, there will be a currency for IBM. 
#
# The account will have a balance of the number of shares and a currency of IBM.
# The data is accessed via theAccountBook, it is held as an array of CurrencyType. 
# There is a nested class called CurrencyType.Type that determines whether the CurrencyType is a currency or a security. 
  
  
   
  def getSecurityAcct(rootAcct, invAcct, tickerSym):
    import com.infinitekind.moneydance.model.Account
    import com.infinitekind.moneydance.model.CurrencyTable
    import com.infinitekind.moneydance.model.AccountBook
 
 # below makes sure currencies.getCurrencyByTickerSymbol is never called with tickerSym = None .. it blows up with a Java Null pointer error
    if tickerSym is None:
      return None
    
 #   Rootaccount2 = getRootAccount() # test
 #   objAcctBook = extension.getUnprotectedContext().getCurrentAccountBook() #test
 #   CurrencyTable2 = objAcctBook.getCurrencies() # test
 #   rootAcct = moneydance.getRootAccount()
    AcctBook = rootAcct.getBook() 
    if AcctBook is None:
      print lineNo() + "rootAcct.getBook() failed"
      return None
    
    currencies = AcctBook.getCurrencies()
    if currencies is None:
      print lineNo() + "AcctBook.getCurrencies() failed"
      return None
#    print "ticker is ",tickerSym
    curr = None
#    currencies = rootAcct.getCurrencyTable() 
#   AttributeError: 'com.infinitekind.moneydance.model.Account' object has no attribute 'getCurrencyTable'
#    print lineNo() + " ticker is ", tickerSym
##    try:
    curr = currencies.getCurrencyByTickerSymbol(tickerSym)
#    except RuntimeError as err:
#    except IndexError as err:
#    except LookupError as err:
#    except BaseException as err:
#    except BaseException as err:
#    except SystemExit as err:
#    except OSError as err:
#    except SystemError as err:
#    except KeyError as err:
#    except KeyError as err:
# can't find anything to catch a NullPointerException'
##    except:
##        print lineNo() + "Security not found1 ",tickerSym
 #       raise Exception ('Ticker is missing from the Account')
#  rootAcct.getCurrencyTable()  throws a java.lang.NullPointerException: java.lang.NullPointerException: Parameter specified as non-null is null: method
#  when a security is missing in the Investment account will need to wrap it in a try.....except now
    if curr is None:
#      print tickerSym, "Security not found2 ",tickerSym
      return None
# debug    print "curr ",curr #said PATHFINDER INCOME FUND PCD-UN 
#    sz = rootAcct.getSubAccountCount() # this one said 380 accounts
    sz = invAcct.getSubAccountCount() # says 15 , they are all the securities used by this investment account accoun
#debug    print "sz",sz
    i = 0
    for i in xrange(0,sz): 
      subAcct = invAcct.getSubAccount(i)
# debug     print "subAccount",subAcct.getAccountName()
#      if subAcct.getAccountType() == invAcct.AccountType.valueOf("SECURITY") :
#	print "its a SECURITY Type "     they are all SECURITY types
      if subAcct.getAccountType() != invAcct.AccountType.valueOf("SECURITY") :
	continue # skip it if its not a SECURITY
      if subAcct.getAccountName() == curr.getName(): # the name of the subaccount matches the security name
# debug	print "found it ",curr
	return subAcct
    return None
#    secAcctName = invAcct.getAccountName() + ':' + curr.getName() ..........this doesn't work anymore was wierd anyways
#    print "secAcctName",secAcctName
#    secAcct = rootAcct.getAccountByName(secAcctName)    
##    secAcct = AcctBook.getAccountByName(secAcctName)
#    if secAcct is None:
#      print "security (ticker) acct not found",secAcctName
#    return secAcct
#public java.util.List<Account> getSubAccounts(AcctFilter search) ######################## maybe could use this function instead of the for loop above
#Return a list of all accounts under this account matching the given filter. 
#This includes accounts not just direct children but all accounts under this one in the hierarchy.

    
#    New function for MD2015  
#    static ParentTxn 	makeParentTxn(AccountBook book, int date, int taxDate, long dateEntered, 
#             java.lang.String checkNumber, set to blank
#             Account account, 
#             java.lang.String description, 
#             java.lang.String memo, 
#             long id, -- set to -1 ??
#             byte status) -- set to unreconciled
#    Shortcut to create a ParentTxn object.

#static SplitTxn 	makeSplitTxn(ParentTxn parentTxn, 
#                        long parentAmount,            0          -amt
#                        long splitAmount,             0          -amt    
#                        float  rate,                  100         100
#                        Account account,              secAcct     incAcct
#                        java.lang.String description, desc        desc 
# -1 for new txn         long txnId,                   -1           -1
#                        byte status)                  unrec       unrec
# split parameter TAG_INVST_SPLIT_TYPE =        TAG_INVST_SPLIT_SEC   TAG_INVST_SPLIT_INC  TAG_INVST_SPLIT_EXP  TAG_INVST_SPLIT_FEE  TAG_INVST_SPLIT_TYPE   TAG_INVST_SPLIT_XFR
# parent setTransferType                 TRANSFER_TYPE_DIVIDEND  TRANSFER_TYPE_BUYSELL TRANSFER_TYPE_MISCINCEXP TRANSFER_TYPE_BUYSELLXFR TRANSFER_TYPE_BANK TRANSFER_TYPE_DIVIDENDXRF TRANSFER_TYPE_SHORTCOVER

#Creates a SplitTxn with the parentAmount having a negative effect on the account of parentTxn, and splitAmount having a positive effect on the account of this SplitTxn.
# see the spread sheet "Investment Transactions.ods"

#    processTxn(root,     invAcct ,   secAcct, transdate ,desc, memo,activity,long2 Total-Amount$,long4 shares Quantity,float2 Price ,float2 BrokerFee, tickerSym)
  global processTxn
  def processTxn(rootAcct, invAcct, secAcct, dateInt,     desc, memo, action,  amt,                       stocks,               rate,              BrokerFee, tickerSym):
    from com.infinitekind.moneydance.model import AbstractTxn
    from com.infinitekind.moneydance.model import ParentTxn
    from com.infinitekind.moneydance.model import SplitTxn
    from com.infinitekind.moneydance.model import TxnUtil
    from com.infinitekind.moneydance.model import InvestTxnType
    
    if action == 'CASHINLIEU' or action == 'MERGER' or action == 'DEPOSIT' or action == 'NAMECHG' or action =='REDEEMED' or action == 'TRANSFER' :
      memo = action + memo
    if action == 'EXCHADJ' or action == 'EXERCISE' or action == 'JOURNAL' or action == 'ADJUSTMENT' or action == 'DVF' or action == 'WITHDRAW':
      memo = action + memo
    if action == 'TAX' or action == 'FEE' or action == 'GST' or action == 'TRT' or action == 'EXPIRED' or action == 'PAYMENT':
      memo = action + memo

# IvestTxnType --- not coded yet ---  SHORT, COVER, DIVIDENDXFR,
# BUY SELL DIVIDEND INTEREST DIVIDEND_REINVEST BANK .. implemented
# BuyXfr SellXfr MiscInc MiscExp .......not seen at ScotiaBank so not tested
# MiscExp is used for Accrued interest on Bond purchases manually

    if action == 'ADJUSTMENT': action = 'DIVIDEND_REINVEST' # these are both money market fund things .works like a real stock dividend
    if action == 'DVF': action = 'DIVIDEND_REINVEST' # these are both money market fund things .works like a real stock dividend
    if action == 'EXPIRED': action = 'SELL'
    if action == 'REDEEMED': action = 'SELL'
    if action == 'EXCHADJ':
      if stocks >= 0: action = 'BUY'
      else: action = 'SELL'
    if action == 'EXERCISE':
      if stocks >= 0: action = 'BUY'
      else: action = 'SELL'
    if action == 'MERGER':
      if stocks >= 0: action = 'BUY'
      else: action = 'SELL'
    if action == 'NAMECHG':
      if stocks >= 0: action = 'BUY'
      else: action = 'SELL'
    if action == 'TRANSFER': 
      print lineNo() + 'stocks=',stocks
      if stocks == 0: 
        action = 'DEPOSIT' 
      else:action = 'BUY'
    if action == 'DEPOSIT' or action == 'TRT' or action == 'JOURNAL' or action == 'TGL' :    # we will have no security to go with this
      action = 'BANK'
    if action == 'WITHDRAW':
      action = 'BANK'      
    if action == 'CASH DIV' or action == 'STOCKDIV' or action == 'CASHINLIEU': # moneydance has no stockdiv it uses a BUY or DIV_REINVEST . 
      action = 'DIVIDEND'
    if action == 'PAYMENT' or action == 'TAX' or action == 'GST' or action == 'FEE':
      action = 'BANK'      
    if action == 'Stock dividend':
      action = 'DIVIDEND'
    if action == 'Deposit':
      action = 'BANK'

# done remapping actions
     
    AcctBook = rootAcct.getBook()                  #2015-1
    txnSet = AcctBook.getTransactionSet()          #2015-2 
    Partxn = ParentTxn.makeParentTxn(AcctBook,dateInt, dateInt, dateInt, "", invAcct,  desc, memo, -1, AbstractTxn.STATUS_UNRECONCILED) #2015
    if action == 'BUY' or action == 'SELL' :  # don't need an inc split because it doesn't effect your income
#      print 'BUY/SELL amt=',amt # 15000 = $150.00 total value of transaction (long ) 2 decimals
#      print 'BUY/SELL stocks=',stocks # 1000000 =  100 number of stocks (long ) 4 decimals
#      print 'BUY/SELL rate=',rate # price 840.0 = $8.40  (float)  2 decimals 
#      print 'BUY/SELL BrokerFee =',BrokerFee # fee 840.0 = $8.40 (float) 2 decimals    
# with scotia on a buy the amount is negative and on a sell the amount is positive
      if action == 'SELL':
	 TxnUtil.setInvstTxnType(Partxn,InvestTxnType.SELL)
         secSplit = SplitTxn.makeSplitTxn(Partxn, long ((amt + BrokerFee ) * -1.0) , long(stocks), float(rate) , secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)  #SELL stocks(stock) is negative amt is positive
      else: # its a BUY
	 TxnUtil.setInvstTxnType(Partxn,InvestTxnType.BUY)
         secSplit = SplitTxn.makeSplitTxn(Partxn, long ((amt + BrokerFee) * -1.0 ) , long(stocks), float(rate), secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)  #BUY stocks is positive amt is negative  
      TxnUtil.setSecurityPart(secSplit)
      Partxn.addSplit(secSplit)
      feeAcct = None  
      feeAcct = rootAcct.getAccountByName('Fees Broker')
      if feeAcct is None:
        print lineNo() + "no catagory Fees Broker"
        return     
      feeSplit = SplitTxn.makeSplitTxn(Partxn, long (BrokerFee) ,0,0, feeAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)  #fees
      TxnUtil.setCommissionPart(feeSplit)
      Partxn.addSplit(feeSplit)      
    elif action == 'BuyXfr' or action == 'SellXfr':
      print lineNo() + " We Don't Do BuyXfr or SellXfr use BANK plus Buy or Sell"
      return # not doing Xfr buys and sells for now . do them manually
    elif action == 'DIVIDEND':
                                # moneydance has no stockdiv it uses a BUY or DIV_REINVEST .
                                #I cannot tell diffence between a CASH DIV and StOCKDIV at Scotia . 
                                #FRANKLIN BISSETT CDN EQUITY FD (202) REINVEST 12/20/16 @ $99.5000 PLUS FRACTIONS OF 0.918 BOOK VALUE $1;782.88      	TML202	22-Dec-2016	22-Dec-2016	CAD	STOCKDIV	17	CAD	0	0
      if stocks != 0 and amt == 0: # so we have stock thats free .. this must be a real stock divided thats being reinvested..some STOCKDIV are really CASH DIV its messed up at scotia
	if desc.count ("FRACTIONS OF") > 0:
	      print lineNo() + "we got mutual fund fractions in the desc"
	      index = desc.find("FRACTIONS OF")
	      desc2 = desc[index+12:]
	      lst5 = desc2.split()
	      print lineNo() + "fraction =",lst5[0] # 0.918 stocks fraction
              stocks = stocks + long(float(lst5[0]) * 10000.0 ) # 4 decimal places on stock quantity
              print lineNo() + "stocks=",stocks
	      index = desc.find("BOOK VALUE")
	      desc2 = desc[index+10:]
	      desc2 = desc2.replace('$','')
	      desc2 = desc2.replace(';','')
	      desc2 = desc2.strip() 
	      lst5 = desc2.split()
	      print lineNo() + "Book Value=",lst5[0] # 1782.88 amt
              amt =  long(float(lst5[0]) * 100.0) # 2 decimals on amount. let md calc the price.
              print lineNo() + "MD amt=",amt
#              raise Exception ('here we are') 
        TxnUtil.setInvstTxnType(Partxn,InvestTxnType.DIVIDEND_REINVEST) # could just post it as a Stock BUY with price = 0 and no fee's 
        secSplit = SplitTxn.makeSplitTxn(Partxn, amt, stocks, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)     # amt=total cost , stocks=stocks , rate=stock price  fee=?
        TxnUtil.setSecurityPart(secSplit)
        Partxn.addSplit(secSplit)    
        autoAcct = None  
        autoAcct = rootAcct.getAccountByName('non taxable stock dividend')  # looks up an income catagory
        if autoAcct is None:
          print lineNo() + "no catagory called non taxable stock dividend"
          return
        incSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED) #2015 autoAcct is the income catagory like "Dividend Income"
        TxnUtil.setIncomePart(incSplit)
        Partxn.addSplit(incSplit)                  
      else:	
        TxnUtil.setInvstTxnType(Partxn,InvestTxnType.DIVIDEND)
        secSplit = SplitTxn.makeSplitTxn(Partxn, 0, 0, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED) #2015 secAcct is for the ticker symbol stats
        TxnUtil.setSecurityPart(secSplit)
        Partxn.addSplit(secSplit)
        autoAcct = None  
        autoAcct = rootAcct.getAccountByName('non taxable dividend') # looks up an income catagory
        if autoAcct is None:
          print lineNo() + "no catagory called non taxable dividend"
          return
        incSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED) #2015 autoAcct is the income catagory like "Dividend Income"
        TxnUtil.setIncomePart(incSplit)
        Partxn.addSplit(incSplit)
    elif action == 'INTEREST':
      TxnUtil.setInvstTxnType(Partxn,InvestTxnType.DIVIDEND)
      secSplit = SplitTxn.makeSplitTxn(Partxn, 0, 0, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED) #2015 secAcct is for the ticker symbol stats
      TxnUtil.setSecurityPart(secSplit)
      Partxn.addSplit(secSplit)
      autoAcct = None  
      autoAcct = rootAcct.getAccountByName('Interest Income') # looks up an income catagory
      if autoAcct is None:
        print lineNo() + " no catagory called Interest Income"
        return
      incSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED) #2015 autoAcct is the income catagory like "Dividend Income"
      TxnUtil.setIncomePart(incSplit)
      Partxn.addSplit(incSplit)      
    elif action == 'DIVIDEND_REINVEST': # stock reinvest ... in scotia land it looks like only the moneymarket uses this DVF so its really interest . maybe a flag to pull the data out of the desc
# sample desc on DVF transaction     "SCOTIA MONEY MARKET FUND (357) REINVEST 01/24/13 @ 10.0000 PLUS FRACTIONS OF 0.006 BOOK VALUE      $       .06     "
#      if stocks == 0 and amt == 0: # something wrong here .. must be Money Market fund
      if  desc.count ("MONEY MARKET") > 0: # the factional data is in the desc . I guess the stock is assumed to have no fractions
#	  print "its the Money Market fund"
	 if desc.count ("FRACTIONS OF") > 0:
	      print lineNo() + "we got mutual fund fractions in the desc"
	      index = desc.find("FRACTIONS OF")
	      desc2 = desc[index+12:]
	      lst5 = desc2.split()
	      print lineNo() + "fraction =",lst5[0] # 0.918 stocks fraction
              stocks = stocks + long(float(lst5[0]) * 10000.0 ) # 4 decimal places on stock quantity
              print lineNo() + "stocks=",stocks
	      index = desc.find("BOOK VALUE")
	      desc2 = desc[index+10:]
	      desc2 = desc2.replace('$','')
	      desc2 = desc2.replace(';','')
	      desc2 = desc2.strip() 
	      lst5 = desc2.split()
	      print lineNo() + "Book Value=",lst5[0] # 1782.88 amt
              amt =  amt + long(float(lst5[0]) * 100.0) # 2 decimals on amount. let md calc the price.
              print lineNo() + "MD amt=",amt
#             raise Exception ('here we are') 
      else:
          print lineNo() + "warning DVF transaction that's not from the money market fund"
          
      TxnUtil.setInvstTxnType(Partxn,InvestTxnType.DIVIDEND_REINVEST)
      secSplit = SplitTxn.makeSplitTxn(Partxn, amt, stocks, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)     # amt=total cost , stocks=stocks , rate=stock price  fee=?
      TxnUtil.setSecurityPart(secSplit)
      Partxn.addSplit(secSplit)    
      autoAcct = None  
      autoAcct = rootAcct.getAccountByName('non taxable interest')  # looks up an income catagory
      if autoAcct is None:
        print lineNo() + "no catagory called non taxable interest"
        return
      incSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED) #2015 autoAcct is the income catagory like "Dividend Income"
      TxnUtil.setIncomePart(incSplit)
      Partxn.addSplit(incSplit)                  
    elif action == 'MiscInc':    # must have security to go with this income use FAKE if its missing can also have fees and a fee category
      TxnUtil.setInvstTxnType(Partxn,InvestTxnType.MISCINC)
      if secAcct is not None:    # must have found a ticker
         secSplit = SplitTxn.makeSplitTxn(Partxn, 0, 0, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)
         TxnUtil.setSecurityPart(secSplit)
         Partxn.addSplit(secSplit)
      autoAcct = None  
      autoAcct = rootAcct.getAccountByName('non taxable interest') # a catagory for the income
      if autoAcct is None:
        print lineNo() + "no catagory called non taxable interest"
        return
      incSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED)
      TxnUtil.setIncomePart(incSplit)     
      Partxn.addSplit(incSplit)
    elif action == 'MiscExp':    # must have a security to go with this expense.if none use the FAKE one. the amt sign needs to be negitive.can also have fees and fee catagory
      TxnUtil.setInvstTxnType(Partxn,InvestTxnType.MISCEXP)
      if secAcct is not None:    # must have found a ticker
         secSplit = SplitTxn.makeSplitTxn(Partxn, 0, 0, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)
         TxnUtil.setSecurityPart(secSplit)
         Partxn.addSplit(secSplit)
      autoAcct = None  
      autoAcct = rootAcct.getAccountByName('Bank Fees') # a catagory
      if autoAcct is None:
        print lineNo() + "no catagory called Bank Fees"
        return
      expSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED)
      TxnUtil.setExpensePart(expSplit)     
      Partxn.addSplit(expSplit)
    elif action == 'BANK' : 
      TxnUtil.setInvstTxnType(Partxn,InvestTxnType.BANK)
      autoAcct = rootAcct.getAccountByName('unknown') # a catagory. this should be the account that transferred the money in or out.
      if autoAcct is None:
        print lineNo() + "no catagory called unknown"
        return
#      print 'amount',amt
      incSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED)
      TxnUtil.setIncomePart(incSplit)     
      Partxn.addSplit(incSplit)  
    elif action == 'REI' : # a dividend is being held for reinvestment later .. try makeing it a MISCEXP  
 #     print 'REI amount',amt
      if amt < 0:
	TxnUtil.setInvstTxnType(Partxn,InvestTxnType.MISCEXP)
      else: 	
        TxnUtil.setInvstTxnType(Partxn,InvestTxnType.MISCINC)
      if secAcct is not None:    # must have found a ticker
         secSplit = SplitTxn.makeSplitTxn(Partxn, 0, 0, 0, secAcct, desc, -1, AbstractTxn.STATUS_UNRECONCILED)
         TxnUtil.setSecurityPart(secSplit)
         Partxn.addSplit(secSplit)
      autoAcct = None  
      autoAcct = rootAcct.getAccountByName('REI') # a catagory
      if autoAcct is None:
        print lineNo() + "no catagory called REI"
        return
      expSplit = SplitTxn.makeSplitTxn(Partxn, -amt, -amt, 0, autoAcct, '', -1, AbstractTxn.STATUS_UNRECONCILED)
      if amt < 0:
        TxnUtil.setExpensePart(expSplit)     
      else:
        TxnUtil.setIncomePart(expSplit)     	
      Partxn.addSplit(expSplit)
    else: 
      print lineNo() + "Error Unknown action", action
      print lineNo() + " Desc ",desc
      print lineNo() + " secAcct ",secAcct
      import ShowMessage66
      ShowMessage66.ShowMessage66("Unknown Action Faking a Short: " + action)
      print lineNo() + "Unknown Action Faking a Short ", action
      print lineNo() + "using recursion on processTxnBMO"
      memo = 'Fake Short Action was '+ action +' ' + memo  # this only works because of the recursion
      processTxnBMO(rootAcct, invAcct, secAcct, dateInt, desc, memo,'Short', amt, val, rate, BrokerFee, tickerSym ) # try recursion
#      raise Exception ('Unknown Action')
      return

    txnSet.addNewTxn(Partxn)
    import time
    time.sleep (0.100)  # seems to have fixed the thread crashes ... its in seconds ,,,, 100 milliseconds
#.........................................end of processTxn function    
#  raise Exception('I know Python!')
# .........................................................This Script continues execution from here

   
  print lineNo() +" Scotia-Inv-new.py reading transactions from ",csvfile
  # if this script is called by execfile() there are now 2 arguments
  # if its called using os.system there are also 2 arguments
  # I had a bug in runScrits.py .. I was passing a blank argument for some reason
  # now execfile and os.system do the same thing ... you only need 2 arguments
#  accountName = None
#  print "len(sys.argv) " , len (sys.argv) # says 2 for os,sys ... says 3 for execfile
#  print "argv1 ",sys.argv[0]  # for os.sys this contains the calling file name Scotia-Inv-new.py
#  print "argv2 ",sys.argv[1]  # for os.sys this contains the account number .. the first argument
#  print "argv3 ",sys.argv[2]  # crash IndexError: index out of range: 2

#  while(1):
#    if len(sys.argv) < 2:
#      print lineNo() + 'this script expects 2 arguments, the Callers name and the Account Name'
#      break
#    if len(sys.argv[0]) < 10:
#      print lineNo() + 'this script needs argv[0] filled in with with the callers name like runScripts.py or ScotiaPicker.py'
#      break
#    if len(sys.argv[1]) < 6:
#      print lineNo() + 'this script needs argv[1] filled in with the Scotia Account Name'
#      break
#    if sys.argv[1] != 'runScripts': # who cares
#      print lineNo() + 'argv[1] must be runScripts'
#      break
#    print lineNo() + "accountName ",sys.argv[1]
#    accountName = sys.argv[1]
#    sys.argv = [''] # clean the arguments out.... why
#    break

  from datetime import datetime
  import scriptsIPC
  accountName = scriptsIPC.accountName # the names are the same by accident this was set by runScripts
    
#  if accountName is None: # must be running from the console , so lets get an account number from the console user
#      i = 0
#      for i in xrange(0,len(accountNames)): # prints a list of all Known Scotia Accounts on the console
#	print "Enter "+str(i)+" for ",accountNames[i]
#
#      var = raw_input("Please enter an Account number: ")
##  print "you entered", var
#      number = int(var)
#      print lineNo() + "upating account ", accountNames[number]
#      accountName = accountNames[number]
      
#  raise Exception('I know Python!')
  import scriptsIPC
  accountName = scriptsIPC.accountName # the names are the same by accident this was set by runScripts
  if accountName is None:
      print lineNo() + " We need an Account Name"
      raise Exception (lineNo() + ' We need an Account Name')
  else:
      print lineNo() + " Using Account Name:" + accountName
  
  root = scriptsIPC.MoneyDance.getRootAccount()
  #currencies = root.getCurrencyTable()

#  fin = open( runScripts.infile ,'r') # this is the csv file we are going to process
  fin = open( csvfile ,'r') # this is the csv file we are going to process

  sym = fin.readline()                 #read the first line and throw it away
  #print 'HEADER=',sym

  while 1:
    sym = fin.readline()
#    print lineNo() + "len(sym) " , len(sym)
    if len(sym) <= 50:
      break
    sym = sym.lstrip().rstrip() # remove trailing and proceeding garbage CR LF \r \n ' ' and spaces
#  sym = sym.replace(',',' ') # changes , to blanks.. don't do this'
    lst = sym.split(',')      # removes the  ',' too
    print lineNo() + str(lst)
    
# Note Scotia has hidden the fee in the "Settlement Amount" and moneydance adjusts the price to compensate. Messes things up
# so the amt passed to moneydance needs to be "Settlement Amount" + Fee and the Fee needs to be updated
# moneydance displays the amt - the fee so if you add the fee to it on a "SELL" it works out. On a "Buy" it should be the opposite.
# the amt passed to moneydance needs to be the result of the sale or purchase without the fee.
# "Fees Broker" is a good category/Account for the fees
# sample of the Scotia csv file layout.
#Description	                                                                                Symbol	Transaction Date	Settlement Date	Account Currency	Type	Quantity	Currency of Price	Price	Settlement Amount
#PATHFINDER INCOME FUND TR UNIT DIST      ON    1000 SHS REC 01/31/18 PAY 02/15/18      	PCD.UN	15-Feb-2018	        15-Feb-2018     	  CAD	      CASH DIV	   0	          CAD	                   0	    50


#    print 'Description=',lst[0]
#    print 'Symbol=',lst[1]
#    print 'Tranaction Date=',lst[2]
#    print 'Settlement Date=',lst[3]
#    print 'Account Currency=',lst[4]
#    print 'Transaction Type=',lst[5]
#    print 'Quantity=',lst[6]
#    print 'Currency of Price=',lst[7]
#    print 'Price=',lst[8]
#    print 'Settlement Amount=',lst[9]
#    raise Exception ('DEbug')
  
    transdate = lst[2].split('-') # scotia now uses yyyy-mm-dd ... oh and the month is a number now  oh and the order is flipped
    try:
      day = transdate[2]
      month = transdate[1]
      year= transdate[0]
    except IndexError as err:
      print lineNo() + "Got an IndexError on date"
      print lineNo() + "Looks like this is not a Scotia csv file"
      raise Exception (lineNo() + "Looks like this is not a Scotia csv file")
#    print 'day=',day
#    print 'month=',month
#    print 'year=',year
#    raise Exception ('DEbug')

#    date = str2date ( day,month,year )
    date = str2dateBMO(day,month,year) # try the BMO version
    transdate = int (strftime("%Y%m%d",date)) # 20120130
#    invAcct = root.getAccountByName(runScripts.accountName)
    invAcct = root.getAccountByName(accountName)
    if invAcct is None: # this is a big deal .....we need to stop now .. not just break
      print lineNo() +"Scotia-Inv-new.py missing the name of the Moneydance account to update"
      print lineNo() + "BAD ................................................................... Account Name " + accountName
      raise Exception (lineNo() + "Moneydance Cannot Find This Account Name ")

#    memo = 'Scotia-Inv.py'
    import datetime

    t = datetime.datetime.now()
    memo = t.strftime(' %m/%d/%Y-%I-%M-%S ')
 
    secAcct = None  
    tickerSym = lst[1]
    Description = lst[0]
    tickerSym = tickerSym.strip() # turned " " into "" an empty string
    Description = Description.strip()
    Action = lst[5]
    
 # Scotia-Inv-new is not using the ScotiaDescTable any more
 #   print "len,tickerSym ",len(tickerSym),tickerSym
 #   if (len(tickerSym) <= 0) or (tickerSym == ' '):  # this also picks up tickerSym is None
 #     print lineNo() + " Missing ticker symbol, try Looking it up using the description "
 #     tickerSym = lookupTicker(Description,ScotiaDescTable) # trys to find the ticker in the ScotiaDescTable using the Scotia Description
 #     if tickerSym is None: print lineNo() + "lookupTicker using its Description failed. ticker is still None"

    foundit= False
    if Description in BMOdescTable.BMOdescTable:
        desc2use = Description
        foundit = True
    if foundit == False:
        print lineNo() + Description + " not in the descTablen trying startwith"
        for key in BMOdescTable.BMOdescTable: # need to scan the table
            if Description.startswith(key):     # don't need to slice the line up
              foundit = True
              desc2use = key
              print lineNo() + " Description starts with key: " + key
              break # Exit the loop once a match is found
    if foundit == False and len(tickerSym) > 0:
        print lineNo() + Description +" startswith Failed trying the ticker"
        for outer_key , inner_dict in BMOdescTable.BMOdescTable.items(): # worked great
           if inner_dict.get('Symbol') == tickerSym:
               print lineNo() + " Found the ticker in the descTable" # it printed this twice .. so its in the dict twice
               foundit = True
               desc2use = outer_key
               print outer_key  # prints the found description
               print inner_dict # prints all the inner dictionaries  with out the outer_key
               break # we only need the first one
    if foundit == True: # we can use desc2use now
        tickerSym = BMOdescTable.BMOdescTable[desc2use]['FIXED_Symbol'] # this should never fail
        if BMOdescTable.BMOdescTable[desc2use]['FIXED_Activity'] == 'BANK':
          print lineNo() + "Its a BANK transaction"
          global XferCategory
          XferCategory = BMOdescTable.BMOdescTable[desc2use]['XferCategory']
          memo = "Changing Action "+Action+" to BANK" + memo
          Action = 'BANK'
#          print lineNo() + "XferCategory " + XferCategory
        if Action == '' or Action == ' ' or Action is None:
          print lineNo() + " Action is missing", Description
          if BMOdescTable.BMOdescTable[desc2use]['FIXED_Activity'] == 'ROC':
             print lineNo() + "its an ROC ",desc2use
             Action = 'ROC'
          else:
             memo = 'Action WAS BLANK using Interest' + memo
             Action = 'Interest' # taking a wild guess
             print lineNo() + "FAKING an Interest ACTION " + tickerSym
    else:
        print lineNo() + Description + " still not found in the descTable FAKEing it"
        tickerSym = 'FAKE-T'
        memo = 'Symbol '+ tickerSym + ' changed ticker to FAKE-T' + memo


#................................................................................
# have moved some of the simple Action remapping to here
# and take it out of the processTxnBMO function
#................................................................................

    Action = remapActions(Action)

    print lineNo() + "tickerSym is now " + tickerSym
    print lineNo() + "Action is now " + Action

#    if tickerSym != '':
##    else: # its not None but will be missing the -T
##      ok so we got a ticker ,lets see if its a Bond , Mutual fund or not on the TSX , check the ticker against the Bond Table first
## the try: below works because the BondTable is indexed by ticker.. you need to use the lookup functions to do the reverse ..
#      try:
#        desc2 = BondTable[tickerSym]['desc'] # try to get the Bond desc using the tickerSym  .. doesn't really do anything '
#        print lineNo() + "its in the BondTable" , desc2
#        # BondTable is a dictionary of dictionaries
#        # example   '5VJYFL0':{'desc':'ZAG BANK MONTHLY INTEREST GIC','coupon':2.95,'date':'2023-03-15','accrued':0,'fee':0},
#      except KeyError as e:
##	print "we got a KeyError"
#	print lineNo() +" Its not in the BondTable",Description
#        try: #       check if its a mutual fund ticker use the StockwatchMutualFundSymbols table its a dictionary of globe.mutualfund symbols verses stockwatch.mutuafund symbolsl
##	  print "test.. ",tickerSym
##	  print len(tickerSym)
#	  symbol2 = definitions.StockwatchMutualFundSymbols[tickerSym] # example 'TML202-T':'BIF*CDN' .. should return BIF*CDN if TML202-T is in the dictionary
#	  print linNo() + "its a mutual fund StockwatchMutualFundSymbols table " + tickerSym + ' : ' + symbol2
#	except KeyError as e:
#	  print lineNo() + "its not a mutual fund ",tickerSym
	                                                             # so its not a Bond or a Mutual Fund its time to glue on the -T""
#          tickerSym = tickerSym.replace('.','-')
#          tickerSym = tickerSym+"-T"
##          print lineNo() + "cleaned up the ticker ", tickerSym
#          try: #  check to see if its on a different exchange
#	    NYXSym = definitions.ExchangeTable[tickerSym] # Example this will return  KBM-N given KBM-T
#            print lineNo() + "its on a different Exchange ", NYXSym
#            print lineNo() + "its not on the TSX ",NYXSym
#	    tickerSym = NYXSym                                                                       # swap the symbol
#	  except KeyError as e:
##	    print "is not in the Symbol table so it must be on the TSX"
#	    fudge = 'Ticker Passed all the tests' # got an error without a line here

	    
#          for tsxSym ,NYXSym in ExchangeTable.items():  #check to see if this symbol is on a different stock exchange
##            print "tsxSym=",tsxSym 
##            print "NYXSym=",NYXSym
##            print len(NYXSym)
#	    if len(NYXSym) <= 0: break
#	    if  tsxSym.count (tickerSym) > 0:
#	      print "Found it. its Not on the TSX", tsxSym ,NYXSym
#	      tickerSym = NYXSym
# #             print "new tickerSym=",tickerSym
#	      break  
	          
#    print lineNo() + 'ticker ',tickerSym
 #   print lineNo() + 'ticker len',len(tickerSym) # says 0
 #   print lineNo() + 'ticker ',lst[1]
 #   print lineNo() + 'ticker len',len(lst[1]) # says 1
 #   if tickerSym is None: print "ticker is None"
 #   else: print 'ticker is Not None' # says this
 #   if tickerSym != ' ': print "ticker is not a single blank char" # says this
 #   else: print "ticker is a blank char"
 #   print(type(tickerSym)) # says <type str>
 #   print(type(lst[1]))    #  says <type str>
 #   print tickerSym.encode('hex') # says nothing
 #   print lst[1].encode('hex')    # says 20
 #   print tickerSym.isspace() # says False
 #   print lst[1].isspace()    # says True all chars must be 0x20
 #   byte_Sym = tickerSym.encode( encoding="utf-8")
 #   print list(byte_Sym)          # []
 #   byte_lst1 = lst[1].encode (encoding = "utf-8")
 #   print list(byte_lst1)                        # ['']
#    if ( tickerSym == '' ): print lineNo() + "We still have a missing Ticker "    # says True..........................................
    # conclusion: the single blank char 0x20 in lst[1] got eaten by tickerSym.strip

#    if tickerSym != '':  # we got a ticker
#      print "ticker4 ",tickerSym
    secAcct = getSecurityAcct(root, invAcct, tickerSym) # this also fails if the ticker has not been added to the Account'
    if secAcct is None: # we have a ticker but its no good
         print lineNo() + "Maybe this security needs to be added to the account " , tickerSym
# so we found it in the DescTable but its not in the Account
         print lineNo() + "The ticker we have is no good will use FAKE-T"
         secAcct = getSecurityAcct(root,invAcct,"FAKE-T") # just fake it
         if secAcct is None:
             raise Exception (lineNo() + 'Security FAKE-T is missing, Please add it to your account')

#       Not doing this any more .. too much trouble keeping the desc table up to date
#	tickerSym = lookupTicker(Description,DescTable) # maybe its the wrong ticker on the record see if we can find the right one.
#	secAcct = getSecurityAcct(root, invAcct, tickerSym)
#        if secAcct is None: # the ticker is still no good
#          secAcct = getSecurityAcct(root,invAcct,"FAKE-T") # just fake it
#          if secAcct is None:
#             print lineNo() + "FAKE-T is Missing, Maybe you should Add it to your Account" # this shows up on the Jython Console
#	     raise Exception ('FAKE-T missing') # this shows up on the Moneydance Console
#          memo = 'BAD Ticker '+ str(tickerSym) +' ' + memo
#	  print lineNo() + "BAD Ticker getSecurityAcct Failed for",tickerSym
#	  print lineNo() + "Maybe you should Add it to your Account"
#    else: # tickerSym is Empty
#      tickerSym= lookupBondTicker(Description,BondTable) # bonds never have tickers
#      print lineNo() + "lookupBondTicker returned ticker " , tickerSym
#      memo = ' ' + str(tickerSym) + ' ' + memo
#      secAcct = getSecurityAcct(root, invAcct, tickerSym)
#      if secAcct is None: # the ticker is still no good
#	print lineNo() + "lookupBondTicker Failed faking it ",tickerSym
#        secAcct = getSecurityAcct(root,invAcct,"FAKE-T") # just fake it  .. its not a Bond , its not a mutual fund , its not on the NYSE
#        if secAcct is None:
#          print lineNo() + "FAKE-T is Missing, Maybe you should Add it to your Account" # this shows up on the Jython Console
#	  raise Exception ('FAKE-T missing')
#        memo = ' Ticker Missing ' + memo
 
#    decimals = secAcct.getCurrencyType().getDecimalPlaces() # securities (stocks) are stored with 4 decimal places
#    userRate = secAcct.getCurrencyType().getUserRate()
#    print 'decimals used for Stock Quantity' ,decimals
#    print 'UserRate used for Stock Quantity' ,userRate
#  dateInt = mdDate(row['Date'])

    Amount = long(mdQty(str(lst[9]), 2)) # in AT file, buy is > 0, sell is < 0 . This is the "Settlement Amount" csv file it only has 2 decimal places * 100
    Quantity = long(mdQty(lst[6], 4 ))  # in AT file, buy is > 0, sell is < 0  #number of stocks , 4 decimal places * 1000
#    if Quantity < 0:
#      Quantity = Quantity * (-1.0)      # let the BUY / SELL action decide on the + or - sign
#    if Amount < 0:
#      Amount = Amount * (-1.0) 
#    print "price1=",lst[8]
    Price = float(mdQty(lst[8], 4 ))  # the price could have up to 4 decimal places in the csv file. returns a long *1000
#    print "price2=",Price
    Price = float(Price / 100.0 )  # md wants it as a float. md seems to handle the posible 2 decimals here * 100
#    print "price3=",Price 
    if Price < 0:           #  Scotia is the problem only has 3 decimal places on price in the CSV .. should have 4 .The error shows up in the broker fee 
      Price = Price * (-1.0)
      
      
# try to figure out what the fee for the transaction was since its not included in the csv file data 
    AmountCalc = (float(Quantity)/10000) * (float(Price))  #Amount is the "Settlement Amount"
#    print 'AmountCalc' , AmountCalc
#    print 'Amount' , Amount
    BrokerFee = 0.0
    if Amount < 0:
	BrokerFee =  AmountCalc + float(Amount) # its a BUY
    else:
	BrokerFee =  float(Amount) + AmountCalc # its a SELL the quanity is negative on a sell
	
    if AmountCalc == 0.0:	
      BrokerFee = 0.0	
    if BrokerFee < 0.0:
      BrokerFee = BrokerFee * (-1.0)
      
#    print "Price amount Units Fee=",Price,Amount,Quantity,BrokerFee  
#    Price amount Units Fee= 1295.0 -1295999 10000000 999.0      ... Price=float(12.95*100) Amount=long(12959.99*100) Units=long(1000*1000) Fee=float(9.99*100) 
    if BrokerFee/100  > 1000.0: # >Bond Buys are a pain in the ass . the Desc doesn't have much info in it and there is no Symbol . this code helps a bit.
      print lineNo() + "This looks Like a Bond or GIC BrokerFee=",BrokerFee
#      Quantity = long(Quantity/100) # fix the quantity
#      AmountCalc = (float(Quantity)/10000) * (float(Price))  #Amount is the "Settlement Amount"
#      BrokerFee = 0.0
#      if Amount < 0: # The BrokerFee will contain the Accrued Interest on a BUY . The fee is 24.99 on a Bond Buy at Scotia
#	BrokerFee =  AmountCalc + float(Amount) # its a BUY Amount is negative
#      else:
#	BrokerFee =  float(Amount) + AmountCalc # its a SELL the quanity(stocks) are negative on a sell
#      if AmountCalc == 0.0:
#        BrokerFee = 0.0
#      if BrokerFee < 0.0:
#        BrokerFee = BrokerFee * (-1.0)
#      tickerSym= lookupBondTicker(lst[0],BondTable) # bonds may no have tickers
#      memo = tickerSym + memo
#      if tickerSym is None:
#	print lineNo() + "ticker sym missing ",lst[0]
#      secAcct = getSecurityAcct(root, invAcct, tickerSym)
#      if secAcct is None: # the ticker we have is no good
#          secAcct = getSecurityAcct(root,invAcct,"FAKE-T") # just fake it
#          if secAcct is None:
#             print lineNo() + "FAKE-T missing"
#	     raise Exception ('FAKE-T missing')
#          memo = 'BAD BOND Ticker' + memo
#	  print lineNo() + "BAD BOND Ticker getSecurityAcct Failed for",tickerSym
#      elif lst[5] == 'BUY': # we just bought a bond
#          accrued = BondTable[tickerSym]['accrued']*100.0
##          print accrued
#          BrokerFee = BrokerFee - float(accrued)
#          if accrued != 0.0:
#            processTxn(root,     invAcct ,   secAcct, transdate ,lst[0],'accrued interest','MiscExp',long(accrued*-1.0),long(0),float(0),float(0),tickerSym) #need extra record for accrued interest at purchase.

#    print 'calling processTxn',lst[0],lst[5]   
#    print 'Price 2 decimals' ,Price 
#    print 'Stock Quantity 4 decimals' ,Quantity # shares
#    print 'Transaction Amount 2 decimals' ,Amount # total $
#    print 'transdate' , transdate
#    print 'BrokerFee 2 decimals' , BrokerFee
#    processTxn(root,     invAcct ,   secAcct, transdate ,desc,       memo,action,   long2 Amount$*100  ,long4 shares Quantity*10000,float2 Price or rate*100 ,float2 BrokerFee*100)
    processTxn(root,     invAcct ,   secAcct, transdate ,Description, memo, Action, long(Amount),        long(Quantity),            float(Price) ,            float(BrokerFee), tickerSym)

 
#######  root.refreshAccountBalances()  #not in 2015
  fin.close()
  import os
  os.rename(csvfile, csvfile + '-done')
  AcctBook = root.getBook() 
  AcctBook.refreshAccountBalances()
  print lineNo() + "Done Scotia-Inv-new.py"
#................................................................................script execution ends here

#................................................................................script execution starts here
if  __name__ == '__main__': # was started with execfile
  print "Scotia_Inv_new.py executed by execfile"
  main()
else:   # was started by import
  print ("__name__" , __name__)
  print "Scotia_Inv_new.py loaded by import"

