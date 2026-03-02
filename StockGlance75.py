#!/usr/bin/env python
# coding: utf8
""" j2py StockGlance72.java >> StockGlance72.py """
#  StockGlance.java
# 
#  Copyright (c) 2015-16, James Larus
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are
#   met:
# 
#   1. Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# 
#   2. Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# 
#   3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# package: com.moneydance.modules.features.stockglance
#.............................................................................................................
# there is no __init__ for this class
# I (waynelloydsmith) modified this script to provide sorting of the columns which was missing
# and converted it to jython

from synchronize import make_synchronized
import java.lang.Double as Double


import java.lang.Math as Math

import com.moneydance.apps.md.view.gui.MoneydanceLAF as MoneydanceLAF
from com.infinitekind.moneydance.model import *
import com.infinitekind.moneydance.model.CurrencyListener as CurrencyListener
import com.infinitekind.moneydance.model.AccountListener as AccountListener
import com.infinitekind.moneydance.model.CurrencyType as CurrencyType
import com.infinitekind.moneydance.model.Account.AccountType as AccountType
#import com.infinitekind.moneydance.model. 
import com.infinitekind.util.DateUtil as DateUtil
import com.infinitekind.util.StringUtils as StringUtils
import com.infinitekind.moneydance.model.AccountUtil as AccountUtil
import com.infinitekind.moneydance.model.AcctFilter as AcctFilter
from com.moneydance.apps.md.view import HomePageView
import com.moneydance.awt.CollapsibleRefresher as CollapsibleRefresher
from com.moneydance.apps.md.view.gui.MoneydanceLAF import *

from java.util import *
import java.util.Vector as Vector
import java.util.Arrays as Arrays
import java.util.Calendar as Calendar
import java.util.Date as Date
import javax.swing.JLabel as JLabel
from java.text import *
import java.text.NumberFormat as NumberFormat
from java.awt import *
import java.awt.Color as Color
from java.util.List import *
#from javax.swing import *
import javax.swing.event.ChangeEvent
#import javax.swing.table
import javax.swing.table.DefaultTableModel as DefaultTableModel
import javax.swing.table.AbstractTableModel as AbstractTableModel
import javax.swing.table.TableModel as TableModel
import javax.swing.table.TableRowSorter as TableRowSorter
import javax.swing.table.DefaultTableCellRenderer as DefaultTableCellRenderer
import javax.swing.JTable as JTable
import javax.swing.JPanel as JPanel
import javax.swing.JFrame as JFrame
import javax.swing.JLabel as JLabel
import javax.swing.BoxLayout as BoxLayout
import java.awt.GridLayout as GridLayout
import javax.swing.BorderFactory as BorderFactory
import java.util.HashMap as HashMap
from javax.swing import WindowConstants as WindowConstants
from javax.swing import JScrollPane as JScrollPane
from java.awt import Dimension as Dimension
from java.awt import BorderLayout
import javax.swing.border.CompoundBorder as CompoundBorder
import javax.swing.border.MatteBorder as MatteBorder
import javax.swing.border.EmptyBorder as EmptyBorder
import javax.swing.event.TableColumnModelListener as TableColumnModelListener

#print "DOne Importing"
global AAA  # holds the instance of StockGlance75()
AAA = None
#from javax.swing import Vector

#  Home page component to display active stock prices and returns.
#class StockGlance(HomePageView):
class StockGlance75():
    print "StockGlance75"
    import java.awt.Color as Color
    import java.util.Vector as Vector
    import java.util.Arrays as Arrays
    import javax.swing.table.DefaultTableModel as DefaultTableModel
    import javax.swing.JTable as JTable
    
    
    book = None # AccountBook()
    table = None # StockGlance75.SGTable()
    tableModel = None  # StockGlance75.SGTableModel
    tablePanel = None # SGPanel()
    footerTable = None # StockGlance75.SGFooterTable
    footerModel = None # StockGlance75.SGFooterModel
#    scrollPane = None
    totalBalance = None # total of all Stock.Securities in all Accounts 
#    currencyTableCallback = None # currencyCallback(self)
#    allAccountsCallback = None # accountCallback(self)
#    refresher = None # CollapsibleRefresher()
    lightLightGray = Color(0xDCDCDC)
    rowCurrencies = Vector()   #  list of security names in the rows (like a row header)
    footer = Vector() # one row of footer data
    data = Vector() # the data retrieved from moneydance
    #  Per column metadata
    names = ["Symbol", "Stock", "Price", "Change", "Balance", "Day", "7 Day", "30 Day", "365 Day", "Accounts"]
    columnNames = Vector(Arrays.asList(names))
#    footerNames = ["", "", "", "", "Total", "", "", "", "", ""]
#    FooterNames = Vector(Arrays.asList(footerNames))
    
    columnTypes = ["Text", "Text", "Currency2", "Currency2", "Currency0", "Percent", "Percent", "Percent", "Percent", "Text"]

    #  Returns a short descriptive name of this view.
    def __str__(self):
        """ generated source for method toString """
        return "Stock Glance"

    # Returns a GUI component that provides a view of the info pane for the given data file.
    # w.s. must be called by Moneydance .. seems like this is how "book" gets set
#    @make_synchronized
#    def getGUIView(self, book): # replaced by createAndShowGUI(self):
#        print("getGUIView") 
#        if self.tablePanel == None:
#            self.book = book
#            self.tableModel = self.getTableModel(book)
#            print "table before",self.table
#            self.table = self.SGTable(self.tableModel)
#            self.scrollPane = JScrollPane(self.table)         
##            self.scrollPane = self.SGScrollPane(self.table)         
##            self.tablePanel = self.SGPanel(self.table)
##        return self.tablePanel
#        return self.scrollPane

    #  Sets the view as active or inactive. When not active, a view should not have any registered listeners
    #  with other parts of the program. This will be called when an view is added to the home page,
    #  or the home page is refreshed after not being visible for a while.
#    def setActive(self, active):
#        print 'setActive'
#        """ generated source for method setActive """
##        if self.book != None:
##            self.book.getCurrencies().removeCurrencyListener(self.currencyTableCallback)
##            #  At most one listener
##            self.book.removeAccountListener(self.allAccountsCallback)
##            if active:
##                self.book.getCurrencies().addCurrencyListener(self.currencyTableCallback)
##                self.book.addAccountListener(self.allAccountsCallback)

    #  Forces a refresh of the information in the view. For example, this is called after the preferences are updated.
    #  Like the other home page controls, we actually do this lazily to avoid repeatedly recalculating after stock
    #  price updates.
#    def refresh(self):
#        print("refresh")
#        self.refresher.enqueueRefresh()

    #  Actually recompute and redisplay table.
#    def actuallyRefresh(self):  # this function knocks out the TableRowSorter and messes with the Column Headers (i think)
#        print "actuallyRefresh"
## ?        synchronized (this) {
#        tableModel = self.getTableModel(self.book)
#        if self.table != None:
#            self.table.setModel(tableModel)
#            self.table.fixColumnHeaders()
#            self.fixTheRowSorter()
#        # ?        }
#        if self.tablePanel != None:
#            self.tablePanel.setVisible(True)
#            self.tablePanel.validate()

    #  Called when the view should clean up everything. For example, this is called when a file is closed and the GUI
    #  is reset. The view should disconnect from any resources that are associated with the currently opened data file.
#    def reset(self):
#        print "reset"
#        self.setActive(False)
#        if self.tablePanel != None:
#            self.tablePanel.removeAll()
#        self.tablePanel = None
#        self.table = None

    # 
    #  Implementation:
    #  pulls the data from moneydance into data Vector , returns an SGTableModel
    def getTableModel(self, book):
#        print "getTableModel book",book
        import java.util.Vector as Vector
        import java.util.Arrays as Arrays
        import java.util.Calendar as Calendar
        import com.infinitekind.moneydance.model.CurrencyType as CurrencyType
        import java.lang.Double as Double

        ct = book.getCurrencies()
        allCurrencies = ct.getAllCurrencies()
        data = Vector()
        today = Calendar.getInstance()
        balances = self.sumBalancesByCurrency(book) # HashMap<CurrencyType, Long>  contains no account info
        accounts = self.getCurrencyAccounts(book) # HashMap<CurrencyType, Accounts>
        self.totalBalance = 0.0
#        StockGlance75.totalBalance = 0.0
        for curr in allCurrencies:
            if not curr.getHideInUI() and curr.getCurrencyType() == CurrencyType.Type.SECURITY:
                price = self.priceOrNaN(curr, today, 0)
                price1 = self.priceOrNaN(curr, today, 1)
                price7 = self.priceOrNaN(curr, today, 7)
                price30 = self.priceOrNaN(curr, today, 30)
                price365 = self.priceOrNaN(curr, today, 365)
	      
                if not Double.isNaN(price) and (not Double.isNaN(price1) or not Double.isNaN(price7) or not Double.isNaN(price30) or not Double.isNaN(price365)):
		    entry = Vector(len(self.names))
                    bal = balances.get(curr)
                    balance = (0.0 if (bal == None) else curr.getDoubleValue(bal) * price)
# ?                    Double balance = (bal == null) ? 0.0 : curr.getDoubleValue(bal) * price;		        
                    self.totalBalance += balance
#                    StockGlance75.totalBalance += balance
                    entry.add(curr.getTickerSymbol())
                    entry.add(curr.getName())
                    entry.add(price)
                    entry.add(price - price1)
                    entry.add(balance)
                    entry.add((price - price1) / price1)
                    entry.add((price - price7) / price7)
                    entry.add((price - price30) / price30)
                    entry.add((price - price365) / price365)
                    entry.add(accounts.get(curr))
                    data.add(entry)
                    self.rowCurrencies.add(curr)
#                    print curr.getTickerSymbol(),balance # if balance is zero it should not be displayed on StockGlance
#                    StockGlance75.rowCurrencies.add(curr)
        self.data = data            
#        StockGlance75.data = data            
        return self.SGTableModel(self.data, self.columnNames, self.rowCurrencies)
#        return StockGlance75.SGTableModel(StockGlance75.data, self.columnNames, self.rowCurrencies)

    def getFooterModel(self):
#        print "getFooterModel "
        import java.util.Vector as Vector
        import java.util.Arrays as Arrays

        entry = Vector(len(self.names)) # its 10 columns
        entry.add("Total")
        entry.add(None)
        entry.add(None)
        entry.add(None)
#        entry.add(StockGlance75.totalBalance)
        entry.add(self.totalBalance)
        entry.add(None)
        entry.add(None)
        entry.add(None)
        entry.add(None)
        entry.add(None)
        self.footer.clear()
        self.footer.add(entry) # needs to be an list of lists (Vector of Vectors)
        return self.SGFooterModel(self.footer,self.columnNames)
#        StockGlance75.footer.clear()
#        StockGlance75.footer.add(entry) # needs to be an list of lists (Vector of Vectors)
#        return StockGlance75.SGFooterModel(StockGlance75.footer,StockGlance75.columnNames)


    def priceOrNaN(self, curr, date, delta):
        import java.lang.Double as Double
        try:
	    backDate = self.backDays(date, delta)
            if self.haveSnapshotWithinWeek(curr, backDate):
                return 1.0 / curr.adjustRateForSplitsInt(backDate, curr.getUserRateByDateInt(backDate))
            else:
                return Double.NaN
        except ZeroDivisionError as e: 
	              return Double.NaN
        except IndexError as e: 
                      return Double.NaN

    #  Return the date that is delta days before startDate
    def backDays(self, startDate, delta):
        import java.util.Calendar as Calendar     
        import com.infinitekind.util.DateUtil as DateUtil
        
        newDate = startDate.clone()
        newDate.add(Calendar.DAY_OF_MONTH, -delta)
        return DateUtil.convertCalToInt(newDate)

    #  MD function getRawRateByDateInt(int dt) returns last known value, even if wildly out of date.
    #  Return true if the snapshots contain a rate within a week before the date.
    def haveSnapshotWithinWeek(self, curr, date):
        import com.infinitekind.util.DateUtil as DateUtil
        snapshots = curr.getSnapshots()
        for snap in snapshots:
            if DateUtil.calculateDaysBetween(snap.getDateInt(), date) <= 7:
                #  within a week
                return True
        return snapshots.isEmpty()
        #  If no snapshots, use fixed rate; otherwise didn't find snapshot

    def sumBalancesByCurrency(self, book):
#        print "sumBalancesByCurrency "
        import java.util.HashMap as HashMap
        import com.infinitekind.moneydance.model.AccountUtil as AccountUtil
        import com.infinitekind.moneydance.model.AcctFilter as AcctFilter
        import com.infinitekind.moneydance.model.Account.AccountType as AccountType

        totals = HashMap() #  HashMap<CurrencyType, Long> 
        for acct in AccountUtil.allMatchesForSearch(book.getRootAccount(), AcctFilter.ACTIVE_ACCOUNTS_FILTER ): 
	    curr = acct.getCurrencyType()                                      
	    total = totals.get(curr) # this returns None if curr doesn't exist yet
	    if acct.getCurrentBalance() != 0 and acct.getAccountType() == AccountType.SECURITY: # we only want Securities with holdings
              pass
	    else:
	      continue # no sense slowing everything down with stuff we don't need 
	    
            total = (0L if (total == None) else total) + acct.getCurrentBalance()            
#?  java      total = ((total == null) ? 0L : total) + acct.getCurrentBalance();
            totals.put(curr, total)
        return totals

    def getCurrencyAccounts(self, book):
#        print "getCurrencyAccounts "
        import java.util.HashMap as HashMap
        import com.infinitekind.moneydance.model.AccountUtil as AccountUtil
        import com.infinitekind.moneydance.model.AcctFilter as AcctFilter
        import com.infinitekind.moneydance.model.Account.AccountType as AccountType
        
        accounts = HashMap()
        for acct in AccountUtil.allMatchesForSearch(book.getRootAccount(), AcctFilter.ACTIVE_ACCOUNTS_FILTER ): 
	    curr = acct.getCurrencyType()                                   
	    account = accounts.get(curr)# this returns None if curr doesn't exist yet
	    if acct.getCurrentBalance() != 0 and acct.getAccountType() == AccountType.SECURITY:
              pass
	    else:
	      continue # no sense slowing everything down with stuff we don't need  . only some BONDS left mixed in with the STOCK
	    if account == None:
	      account = str(acct.getParentAccount())
	    else:  
              account = account + ' : ' + str(acct.getParentAccount()) # concatinate two strings here
            accounts.put(curr,account)
        return accounts



    # 
    #  Private classes:
    # 
    #  CurrencyListener
##    class currencyCallback(CurrencyListener):
##        """ generated source for class currencyCallback """
##        thisSG = self.StockGlance()
##
##        def __init__(self, sg):
##            """ generated source for method __init__ """
##            super(currencyCallback, self).__init__()
##            self.thisSG = sg
##
##        def currencyTableModified(self, table):
##            """ generated source for method currencyTableModified """
##            self.thisSG.refresh()

    #  AccountListener
##    class accountCallback(AccountListener):
##        """ generated source for class accountCallback """
##        thisSG = StockGlance()
##
##        def __init__(self, sg):
##            """ generated source for method __init__ """
##            super(accountCallback, self).__init__()
##            self.thisSG = sg
##
##        def accountAdded(self, parentAccount, newAccount):
##            """ generated source for method accountAdded """
##            self.thisSG.refresh()
##
##        def accountBalanceChanged(self, newAccount):
##            """ generated source for method accountBalanceChanged """
##            self.thisSG.refresh()
##
##        def accountDeleted(self, parentAccount, newAccount):
##            """ generated source for method accountDeleted """
##            self.thisSG.refresh()
##
##        def accountModified(self, newAccount):
##            """ generated source for method accountModified """
##            self.thisSG.refresh()

    #  JPanel
#    class SGPanel(JPanel):
#        def __init__(self, table):
#            """ generated source for method __init__ """
#            super(JPanel, self).__init__()
#            print "SGPanel init "            
#            self.setLayout(BoxLayout(self, BoxLayout.PAGE_AXIS))
#            self.add(table.getTableHeader())
#            self.add(table)
#            self.add(table.getFooterTable())
#            self.setBorder(BorderFactory.createCompoundBorder(MoneydanceLAF.homePageBorder, BorderFactory.createEmptyBorder(0, 0, 0, 0)))


    #  SGTableModel
    class SGTableModel(DefaultTableModel):
#        print "SGTableModel "
        import java.awt.Color as Color
        import java.util.Vector as Vector
        import java.util.Arrays as Arrays
        import javax.swing.table.DefaultTableModel as DefaultTableModel

        rowCurrencies2 = Vector()

        def __init__(self, data, columnNames, rowCurrencies):
	    import javax.swing.table.DefaultTableModel as DefaultTableModel
            super(DefaultTableModel, self).__init__(data,columnNames)
            self.rowCurrencies2 = rowCurrencies

        def getRowCurrencies(self):
            return self.rowCurrencies2


    #  SGFooterModel
    class SGFooterModel(DefaultTableModel):      
#        print "SGFooterModel "
        import java.awt.Color as Color
        import java.util.Vector as Vector
        import java.util.Arrays as Arrays
        import javax.swing.table.DefaultTableModel as DefaultTableModel

        footer2 = Vector()
        columnNames2 = []

        def __init__(self, footer, columnNames):
	    import javax.swing.table.DefaultTableModel as DefaultTableModel
            super(DefaultTableModel, self).__init__(footer,columnNames)
            self.footer2 = footer
            self.columnNames2 = columnNames

        def getFooterVector(self):
            return self.footer2

	def isCellEditable(self, row, column):
            return False
	  

    #  SGFooterTable JTable
    
    class SGFooterTable(JTable):

#        print "SGFooterTable "

        def __init__(self, footerModel):
	    import javax.swing.JTable as JTable
            super(JTable, self).__init__(footerModel)

        def getDataModel(self):
	    global AAA 
            return AAA.footerModel
	  
	  
        #  Rendering depends on  column .. this footer only has one row
        def getCellRenderer(self, row, column):
#	    print "footer renderer",row,column
            import javax.swing.table.DefaultTableCellRenderer as DefaultTableCellRenderer
            import javax.swing.JLabel as JLabel
            renderer = None
            global AAA
            if AAA.columnTypes[column]=="Text":
                renderer = DefaultTableCellRenderer()
                renderer.setHorizontalAlignment(JLabel.LEFT)
            elif AAA.columnTypes[column]=="Currency2" or AAA.columnTypes[column]=="Currency0":
	        rowCurrencies = self.getDataModel().getFooterVector() # only diff
	        curr = None
                if 0 <= row and row < len(rowCurrencies):
                    curr = AAA.rowCurrencies.get(row)
                else:
                    curr = self.book.getCurrencies().getBaseType() # Footer reports base currency
                renderer = AAA.CurrencyRenderer(curr, AAA.columnTypes[column] == "Currency0")
                renderer.setHorizontalAlignment(JLabel.RIGHT)
            elif AAA.columnTypes[column]=="Percent":
                renderer = AAA.PercentRenderer()
                renderer.setHorizontalAlignment(JLabel.RIGHT)
            else:
                renderer = DefaultTableCellRenderer()
            return renderer

	  
    class SGTable(JTable): # (JTable)
      
        def __init__(self, tableModel):
#            print "SGTable init"
            import javax.swing.JTable as JTable
            super(JTable, self).__init__(tableModel)
#            self.fixColumnHeaders()
            self.fixTheRowSorter();

        def getDataModel(self):
	    global AAA
            return AAA.tableModel

        def isCellEditable(self, row, column):
            return False

        #  Rendering depends on row (i.e. security's currency) as well as column
        def getCellRenderer(self, row, column):
	    import javax.swing.table.DefaultTableCellRenderer as DefaultTableCellRenderer
	    import javax.swing.JLabel as JLabel
            renderer = None
            global AAA
            if AAA.columnTypes[column]=="Text":
                renderer = DefaultTableCellRenderer()
                renderer.setHorizontalAlignment(JLabel.LEFT)
            elif AAA.columnTypes[column]=="Currency2" or AAA.columnTypes[column]=="Currency0":
	        rowCurrencies = self.getDataModel().getRowCurrencies()
	        curr = None
                if 0 <= row and row < len(rowCurrencies):
                    curr = AAA.rowCurrencies.get(row)
                else:
                    curr = self.book.getCurrencies().getBaseType() # Footer reports base currency
                renderer = AAA.CurrencyRenderer(curr, AAA.columnTypes[column] == "Currency0")
                renderer.setHorizontalAlignment(JLabel.RIGHT)
            elif AAA.columnTypes[column]=="Percent":
                renderer = AAA.PercentRenderer()
                renderer.setHorizontalAlignment(JLabel.RIGHT)
            else:
                renderer = DefaultTableCellRenderer()
            return renderer

        def columnMarginChanged(self, event):
            eventModel = event.getSource()
            thisModel = self.getColumnModel()
            columnCount = eventModel.getColumnCount()
            i = 0
            while i < columnCount:
                thisModel.getColumn(i).setWidth(eventModel.getColumn(i).getWidth())
                i += 1
            self.repaint()
            
        import java.util.Comparator as Comparator   
        class myComparator (Comparator): 
#	    print("Mycomparator")      # example of jython conditional operator.works like the java ? operator
	    def compare( self, str1 , str2): return 1 if str1 > str2 else 0 if str1 == str2 else -1                
      
#        def fixColumnHeaders(self):  # don't know what this was for
#            cm = self.getColumnModel()
#            i = 0
#            while i < cm.getColumnCount():
#	        col = cm.getColumn(i);
#                col.setHeaderRenderer(StockGlance75.HeaderRenderer())
#                i += 1
#            return
	        
        def fixTheRowSorter(self):    # for some reason everthing was being coverted to strings                                  
	    import javax.swing.table.TableRowSorter as TableRowSorter
	    sorter = TableRowSorter()           
	    self.setRowSorter(sorter)                               
	    sorter.setModel(self.getModel())                          
	    for i in range (0 , self.getColumnCount() ) :                   
                 sorter.setComparator(i,self.myComparator())    
            self.getRowSorter().toggleSortOrder(0) 
	  	  
#        @override ..JTable method . preformance pig	 
        def prepareRenderer(self, renderer, row, column):  # make Banded rows
	    global AAA 
            component = super(AAA.SGTable, self).prepareRenderer(renderer, row, column)
            if not self.isRowSelected(row):
              component.setBackground(self.getBackground() if row % 2 == 0 else AAA.lightLightGray)
            return component

        def getFooterTable(self):
            return self.footerTable

    # Render a currency with given number of fractional digits. NaN or null is an empty cell.
    # Negative values are red.
    import javax.swing.table.DefaultTableCellRenderer as DefaultTableCellRenderer
    class CurrencyRenderer(DefaultTableCellRenderer):
#        print "CurrencyRenderer "
        noDecimals = bool()
        relativeTo = None # CurrencyType()
        decimalSeparator = '.'
        noDecimalFormatter = None # NumberFormat()

        def __init__(self, currency, noDecimals):
	    import java.lang.Double as Double
	    import java.text.NumberFormat as NumberFormat
	    import javax.swing.table.DefaultTableCellRenderer as DefaultTableCellRenderer
	    import com.infinitekind.moneydance.model.CurrencyType as CurrencyType
            super(DefaultTableCellRenderer, self).__init__()
            self.noDecimals = noDecimals
            ct = currency.getTable()
            relativeToName = currency.getParameter(CurrencyType.TAG_RELATIVE_TO_CURR)
            if relativeToName != None:
                self.relativeTo = ct.getCurrencyByIDString(relativeToName)
            else:
                self.relativeTo = ct.getBaseType()
            self.noDecimalFormatter = NumberFormat.getNumberInstance()
            self.noDecimalFormatter.setMinimumFractionDigits(0)
            self.noDecimalFormatter.setMaximumFractionDigits(0)

        def isZero(self, value):
	    import java.lang.Math as Math
            return Math.abs(value) < 0.01

        def setValue(self, value):
	    import java.lang.Double as Double
	    import java.awt.Color as Color
            if value == None:
                self.setText("")
            elif Double.isNaN(float(value)):
                self.setText("")
            else:
                if self.isZero(float(value)):
                    value = 0.0
                if self.noDecimals:
		    # MD format functions can't print comma-separated values without a decimal point so
                    # we have to do it ourselves
                    scaledValue = float(value) * self.relativeTo.getUserRate();		  
                    self.setText(self.relativeTo.getPrefix() + " " + self.noDecimalFormatter.format(scaledValue) + self.relativeTo.getSuffix())
                else:
		    scaledValue = self.relativeTo.convertValue(self.relativeTo.getLongValue(float(value)))
                    self.setText(self.relativeTo.formatFancy(scaledValue, self.decimalSeparator))
                if float(value) < 0.0:
                    self.setForeground(Color.RED)
                else:
                    self.setForeground(Color.BLACK)
                    
    # Render a percentage with 2 digits after the decimal point. Conventions as CurrencyRenderer
    class PercentRenderer(DefaultTableCellRenderer):
#        print "PercentRenderer "
#        import java.lang.Double as Double
#        import java.lang.Math as Math
        decimalSeparator = '.'
        def __init__(self):
	    import javax.swing.table.DefaultTableCellRenderer as DefaultTableCellRenderer
            super(DefaultTableCellRenderer, self).__init__()

        def isZero(self, value):
	    import java.lang.Math as Math
            return Math.abs(value) < 0.0001

        def setValue(self, value):
	    import java.lang.Double as Double
	    import com.infinitekind.util.StringUtils as StringUtils
	    import java.awt.Color as Color
            if value == None:
                self.setText("")
            elif Double.isNaN(float(value)):
                setText("")
            else:
                if self.isZero(float(value)):
                    value = 0.0
                self.setText(StringUtils.formatPercentage(float(value), self.decimalSeparator) + "%")
                if float(value) < 0.0:
                    self.setForeground(Color.RED)
                else:
                    self.setForeground(Color.BLACK)

    class HeaderRenderer(DefaultTableCellRenderer):
#        print "HeaderRenderer "
        def __init__(self):
            super(DefaultTableCellRenderer, self).__init__()
            self.setForeground(Color.BLACK)
            self.setBackground(Color.lightGray)
            self.setHorizontalAlignment(JLabel.CENTER)
                        

#    def __init__(self): # init for StockGlance class
#        print "StockGlance init"
#        super(StockGlance, self).__init__()
                
#    @classmethod
    def createAndShowGUI(self):
#        print "creatAndShowGUI"
        from javax.swing import JScrollPane as JScrollPane
        import javax.swing.border.CompoundBorder as CompoundBorder
        import javax.swing.border.MatteBorder as MatteBorder
        import javax.swing.border.EmptyBorder as EmptyBorder
        import java.awt.Color as Color
        import javax.swing.JFrame as JFrame
        from javax.swing import WindowConstants as WindowConstants
        from java.awt import BorderLayout
        import javax.swing.JTable as JTable
        from java.awt import Dimension as Dimension
        import scriptsIPC
        root = scriptsIPC.MoneyDance.getRootAccount()
        self.book = root.getBook()

#        StockGlance75.tableModel = self.getTableModel(self.book)
#        StockGlance75.table = self.SGTable(StockGlance75.tableModel)
        self.tableModel = self.getTableModel(self.book)
        self.table = self.SGTable(self.tableModel)
        
        self.footerModel = self.getFooterModel()
        self.footerTable = self.SGFooterTable(self.footerModel)
#        StockGlance75.footerModel = self.getFooterModel()
#        StockGlance75.footerTable = self.SGFooterTable(StockGlance75.footerModel)
        
        self.scrollPane = JScrollPane(self.table, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED)
#        self.scrollPane = JScrollPane(StockGlance75.table, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED)
        self.scrollPane.setBorder(CompoundBorder(MatteBorder(0, 0, 1, 0, Color.gray), EmptyBorder(0, 0, 0, 0)))

        self.footerScrollPane = JScrollPane(self.footerTable, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED)
#        self.footerScrollPane = JScrollPane(StockGlance75.footerTable, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED)
        self.footerScrollPane.setBorder(CompoundBorder(MatteBorder(0, 0, 1, 0, Color.gray), EmptyBorder(0, 0, 0, 0)))
      
        frame_ = JFrame("StockGlance")
        frame_.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE) 
        frame_.add(self.scrollPane, BorderLayout.CENTER)
        
        self.table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF )
#        StockGlance75.table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF )
        
        self.footerTable.setColumnSelectionAllowed(False)
        self.footerTable.setRowSelectionAllowed(False)
        self.footerTable.setAutoResizeMode(JTable.AUTO_RESIZE_OFF )
#        StockGlance75.footerTable.setColumnSelectionAllowed(False)
#        StockGlance75.footerTable.setRowSelectionAllowed(False)
#        StockGlance75.footerTable.setAutoResizeMode(JTable.AUTO_RESIZE_OFF )
        

        frame_.add(self.footerScrollPane, BorderLayout.SOUTH)
        
        frame_.setSize(1170,1000)
        
        tcm = self.table.getColumnModel()
#        tcm = StockGlance75.table.getColumnModel()
        tcm.getColumn(0).setPreferredWidth(80)
        tcm.getColumn(1).setPreferredWidth(250)
        tcm.getColumn(2).setPreferredWidth(80)
        tcm.getColumn(3).setPreferredWidth(80)
        tcm.getColumn(4).setPreferredWidth(80)
        tcm.getColumn(5).setPreferredWidth(80)
        tcm.getColumn(6).setPreferredWidth(80)
        tcm.getColumn(7).setPreferredWidth(80)
        tcm.getColumn(8).setPreferredWidth(80)
        tcm.getColumn(9).setPreferredWidth(260)
        
        tcm = self.footerTable.getColumnModel()
#        tcm = StockGlance75.footerTable.getColumnModel()
        tcm.getColumn(0).setPreferredWidth(80)
        tcm.getColumn(1).setPreferredWidth(250)
        tcm.getColumn(2).setPreferredWidth(80)
        tcm.getColumn(3).setPreferredWidth(80)
        tcm.getColumn(4).setPreferredWidth(80)
        tcm.getColumn(5).setPreferredWidth(80)
        tcm.getColumn(6).setPreferredWidth(80)
        tcm.getColumn(7).setPreferredWidth(80)
        tcm.getColumn(8).setPreferredWidth(80)
        tcm.getColumn(9).setPreferredWidth(260)

        self.footerScrollPane.setPreferredSize(Dimension(10,30))# (width,height) width doesn't matter
 
        self.footerTableHeader = self.footerTable.getTableHeader()
#        self.footerTableHeader = StockGlance75.footerTable.getTableHeader()
        self.footerTableHeader.setEnabled(False) # may have worked
        self.footerTableHeader.setPreferredSize(Dimension(0,0)) # this worked no more footer Table header
        
        self.tableHeader = self.table.getTableHeader()
#        self.tableHeader = StockGlance75.table.getTableHeader()
        self.tableHeader.setReorderingAllowed(False) # no more drag and drop columns, it didn't work
                
#        frame_.pack()
        frame_.setVisible(True)

            
#            self.footerTable.setColumnModel(self.getColumnModel())
#            self.getColumnModel().addColumnModelListener(self.footerTable)
#            self.footerTable.getColumnModel().addColumnModelListener(self)
            
                        
#############                   end of class StockGlance(HomePageView):
#print "At the bottom"

if  __name__ == '__main__': # was started with execfile
  print "name is main started by execfile"
#  import sys
  global AAA
  AAA = StockGlance75() # this works here but not in import ??
  StockGlance75.createAndShowGUI(AAA)
else:   # was started by import
  print "loaded by import"
  print ("__name__ is", __name__)

#  global AAA
#  AAA = StockGlance75()
#  StockGlance75.createAndShowGUI(AAA)
# above works on import using this script .. below works if typed into the JConsole2026 console .. modulename.classname
## import StockGlance75 .. just get the above messages
## StockGlance75.AAA = StockGlance75.StockGlance75()
## StockGlance75.StockGlance75.createAndShowGUI(StockGlance75.AAA)
# it works differently when you run it from the console .. you need the module name and the class name
# when  you run from the script you don't need the module name.
# need to use the AAA the script is seeing .  its a global in the script(module)
# AAA has to be an instance of the class


