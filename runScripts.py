#!/usr/bin/env jython
# coding: utf8
# version 2/17/2025
# this is a Java Swing program
from java.lang import System
import sys
#  define some globals
# you need a global statement to write to these
def lineNo():  return (str(sys._getframe(1).f_lineno) + ' ')
mframe = None # for WindowClose and showMessage .. maybe should be inside the class

#  sys.stdout = open ('/dev/pts/3', 'w')  #says <filewriter object at 0x3>) this goes to the JConsole2026
#  sys.stderr = open ('/dev/pts/3', 'w')  #says <filewriter object at 0x2>) this goes no where
#  print("sys.stderr ",sys.stderr)
#  print("sys.stdout ",sys.stdout)
#  sys.stderr.write("This goes to the  stderr stream.\n")  # this didn't print anything
#  sys.__stderr__.write("This goes to the  __stderr__ stream.\n") # this went to the moneydance console

#sys.stderr = sys.stdout
#sys.stderr.write("RunScripts stderr Version 3 starting.\n")
# sys.stderr.flush() # didn't help
#sys.stdout.write("RunScripts stdout Version 3 starting.\n")
#def main():




#sys.stderr = sys.__stderr__ # put stderr back to where it belongs .. this worked

class runScripts:




  #from javax.swing import *
  #from java.awt import *
  from javax.swing.tree import DefaultMutableTreeNode
###  from com.moneydance.apps.md.model import AbstractTxn
###  from com.moneydance.apps.md.model import ParentTxn
###  from com.moneydance.apps.md.model import SplitTxn
  from com.infinitekind.moneydance.model import AbstractTxn
  from com.infinitekind.moneydance.model import ParentTxn
  from com.infinitekind.moneydance.model import SplitTxn

  from javax.swing import Timer
  from java.awt.event import ActionListener
  from javax.swing import JFrame
  from java.awt import BorderLayout
  from javax.swing import JTree
  from javax.swing import JScrollPane
  from java.awt import Dimension
  from javax.swing import JPanel
  from javax.swing import JButton
  from javax.swing import JLabel
  from javax.swing import WindowConstants


  import os
  os.chdir('/opt/moneydance/scripts')

#  execfile("AccountNames.py") # defines ScotiaAccounts and BMOAccounts.. Investment accounts
  import AccountNames
      
  class WindowClose(ActionListener):
    def __init__(self):
        from javax.swing import Timer
        self.timer = Timer(5000, self)
        self.timer.start()
    def actionPerformed(self, e):
        self.timer.stop()
        mframe.dispose()  

  def showMessage (self,message) : 
    global mframe  # need this for WindowClose() to work
#    mframe = self.JFrame("Message")
    mframe = self.JFrame(message)
#    mframe.setSize(1000, 100)
    mframe.setSize(1000, 50)
    mframe.setDefaultCloseOperation(self.WindowConstants.DISPOSE_ON_CLOSE)
    mpnl = self.JPanel()
    mframe.add(mpnl)
    mlabel = self.JLabel(str(message))
    mpnl.add(mlabel)
    mlabel.setVisible(True)
    mframe.setVisible(True)
    self.WindowClose()

  def addLevel2Items(self,branch, branchData=None):
    '''  add data to tree branch
         requires branch and data to add to branch
    '''
    # this does not check to see if its a valid branch
    if branchData == None:
        branch.add(DefaultMutableTreeNode('No valid data'))
    else:
        for item in branchData:
          # add the data from the specified list to the branch
          branch.add(self.DefaultMutableTreeNode(item))

  def ItemSelect(self, event):
    import sys
    import scriptsIPC
    selected = self.tree.getLastSelectedPathComponent()
    if selected == None:
      self.xlabel.text = 'You Need to Pick a Script'
      mess = "Error Please Open a Branch on the Tree Below"
      self.showMessage(mess)
    else:
      self.xlabel.text = str(selected)
      print lineNo() + "RunScripts Selected ", selected
      if str(selected).count("Misc Scripts"):
          mess = "Error Please Open a Branch on the Tree Below"
          self.showMessage(mess)
      elif str(selected).count("Jython Scripts"):
          mess = "Error Please Open a Branch on the Tree"
          self.showMessage(mess)
      elif str(selected).count("Run Stockwatch Update Scripts"): 
          mess = "Error Please Select a Stockwatch Update Script From the list below"
          self.showMessage(mess)
      elif str(selected).count("Import BMO csv file"):
          mess = "Error Please Select an Investment Account From the list below"
          self.showMessage(mess)
      elif str(selected).count("updateDaylyStockwatch.py"):
          mess = "getting todays close prices"
          self.showMessage(mess)
          import updateDaylyStockwatch
          updateDaylyStockwatch.main()
      elif str(selected).count('updateHistoryStockwatch.py'):
          mess = 'importing updateHistoryStockwatch'
          self.showMessage(mess)        
	  import updateHistoryStockwatch
	  updateHistoryStockwatch.main()
#	  execfile(str(selected))  # should be changed to import
#      elif str(selected) in BMOAccounts:
      elif str(selected) in self.AccountNames.BMO.Accounts: # an account name was selected from a list of names
          mess = "Updating BMOAccount "+ str(selected)
          self.showMessage(mess)
          scriptsIPC.accountName = str(selected) # this will be read by BMO_Inv_new
          import BMO_Inv_new
          BMO_Inv_new.main()
##          sys.argv = ['','runScripts',str(selected)]  # not sure why I was doing this
#          sys.argv = ['runScripts',str(selected)]      # this is needed by BMO_Inv_new.py ..its the moneydance account name
#	  execfile("/opt/moneydance/scripts/BMO_Inv_new.py")
      elif str(selected).count('jython_info.py'):
          mess = 'importing jython_info.py'
          self.showMessage(mess)
	  import jython_info
	  jython_info.jython_info() # all the code is in __init__
	  raise TypeError,'jython_info'
      elif str(selected).count('StockGlance75.py'):
          mess = 'importing StockGlance75.py'
          self.showMessage(mess)
          import StockGlance75
          StockGlance75.AAA = StockGlance75.StockGlance75()
          StockGlance75.StockGlance75.createAndShowGUI(StockGlance75.AAA)
	  raise TypeError, 'StockGlance75'
      else: # this is the catch all should only be test.py and dev.py left
          mess = "execfile(Script) "+ str(selected)
          self.showMessage(mess)
#          import test
          execfile(str(selected))

  def __init__(self):
      
    import sys
    from javax.swing import JEditorPane
    from javax.swing import JFrame
    from javax.swing import JPanel
    from javax.swing import JScrollPane
    from javax.swing import JSplitPane

    from java.awt import Color
    from javax.swing import ImageIcon
    from javax.swing.tree import DefaultTreeCellRenderer
    from javax.swing import JTree
    from javax.swing.tree import DefaultMutableTreeNode
    from javax.swing.tree import TreeSelectionModel
    from javax.swing.event import TreeSelectionEvent
    from javax.swing.event import TreeSelectionListener
    from javax.swing.plaf.metal import MetalIconFactory
    logger.info("Runscripts Starting up")
# for debugging stderr troubles
#    sys.stdout.write("1 runScripts.py sys.stdout "+ str(sys.stdout) +"\n")
#    sys.stderr.write("2 runScripts.py sys.stderr "+ str(sys.stderr) +"\n")
#    System.err.println("3 runScripts.py System.err " + str(System.err) )
#    System.out.println("4 runScripts.py System.out " + str(System.out) )
#    System.err.println("5 runScripts.py System.err showing System.out " + str(System.out) )
#    System.err.println("6 runScripts.py System.err showing sys.stdout " + str(sys.stdout) )
#    System.err.println("7 runScripts.py System.err showing sys.stderr " + str(sys.stderr) )

# the list of Misc Scripts test.py and dev.py are just for playing with
    mMiscData = ["StockGlance75.py","jython_info.py" ,"test.py","dev.py"]
# the scripts below process csv files downloaded from www.stockwatch.com and manually placed in
# /opt/moneydance/tmp/Stockwatch (maybe a years history in each file , a separate file for each symbol)
#  StockwatchDay(fetches the days closing prices for that exchange and updates Moneydance automatically)
    sStockwatchData = ["updateDaylyStockwatch.py" ,"updateHistoryStockwatch.py"]

    upBMOInvestmentPyData = self.AccountNames.BMO.Accounts

    xframe = self.JFrame("runScripts.py")
#    xframe.setSize(500, 350)
    xframe.setSize(800, 350)
    xframe.setLayout(self.BorderLayout())

    # add level 0 items
    treeRoot = self.DefaultMutableTreeNode('Jython Scripts')
    
    mMisc = self.DefaultMutableTreeNode('Misc Scripts')
    sStockwatch = self.DefaultMutableTreeNode('Run Stockwatch Update Scripts')
    upBMOInvestmentPy = self.DefaultMutableTreeNode('Import BMO transaction from ~/Downloads/*.csv to the selected Investment Account')
    
    # add the level 1 items
    treeRoot.add(mMisc)
    treeRoot.add(sStockwatch)
    treeRoot.add(upBMOInvestmentPy)

    #add the level 2 items to level 1
    self.addLevel2Items(mMisc, mMiscData)
    self.addLevel2Items(sStockwatch, sStockwatchData)
    self.addLevel2Items(upBMOInvestmentPy, upBMOInvestmentPyData)
    
    #build the tree
    self.tree = self.JTree(treeRoot)

    leafIcon = MetalIconFactory.getTreeLeafIcon()    
    openIcon = MetalIconFactory.getFileChooserNewFolderIcon()
    closedIcon = MetalIconFactory.getTreeFolderIcon()

    renderer = DefaultTreeCellRenderer()
    renderer.setLeafIcon(leafIcon)
    renderer.setOpenIcon(openIcon)
    renderer.setClosedIcon(closedIcon)
    self.tree.setCellRenderer(renderer)
   
        
    scrollPane = self.JScrollPane()  # add a scrollbar to the viewport
    scrollPane.setPreferredSize(self.Dimension(700,250))
    scrollPane.getViewport().setView(self.tree)

    xpanel = self.JPanel()
    xpanel.add(scrollPane)
    xframe.add(xpanel, self.BorderLayout.CENTER)

    btn = self.JButton('Run Script', actionPerformed = self.ItemSelect)
    xframe.add(btn,self.BorderLayout.SOUTH)
    self.xlabel = self.JLabel('Select Script')
    xframe.add(self.xlabel, self.BorderLayout.NORTH)
    xframe.setDefaultCloseOperation(self.WindowConstants.DISPOSE_ON_CLOSE)
    xframe.setVisible(True)
    self.addLevel2Items # initalize the addLevel2Items function

#from javax.swing import SwingUtilities
#print("Is Event Dispatch Thread says ",SwingUtilities.isEventDispatchThread())
#import threading
#current_thread = threading.current_thread()
#print("Current thread name:", current_thread.name)
if  __name__ == '__main__': # was started with execfile
  import scriptsIPC
  logger = scriptsIPC.logger
  print "runScripts.py executed by execfile"
  logger.info("runScripts.py loaded by execfile")
#  main()
  runScripts()
else:   # was started by import
  import scriptsIPC
  logger = scriptsIPC.logger
  print "runScripts.py loaded by import" # this shows on the console
  logger.info("runScripts.py loaded by import")
#  logger.warning("runScripts.py loaded by import") # test stdout to console
#  import runScripts
#  runScripts.runScripts() will start it

#if __name__ == '__main__':  # means script was started with execfile .. otherwise it must be import
#  runScripts()
#else:                       # must be an import
#  import java.lang.Runnable
#  from javax.swing import SwingUtilities
#  runScripts()
#  SwingUtilities.invokeLater(runScripts()) # error TypeError: invokeLater(): 1st arg can't be coerced to java.lang.Runnable
#  SwingUtilities.invokeLater(jake) # TypeError: invokeLater(): 1st arg can't be coerced to java.lang.Runnable
#  print("Is Event Dispatch Thread says ",SwingUtilities.isEventDispatchThread())
#  current_thread = threading.current_thread()
#  print("Current thread name:", current_thread.name)
# I gave up on using the Java EDT see Java-Swing-import.txt

