#!/usr/bin/env python
# coding: utf8
# version 2/17/2025
# started with execfile("ScotiaPicker.py") on a jthonConsole
# you then select a Scotia Investment account from the the Account list
# it then starts Scotia_Inv_new passing the accountName to it as an argument.. fixed
# Scotia_Inv_new starts selectScotiaBankCSVfile.py which saves the csv file name in .. fixed
# /opt/moneydance/scripts/tmp/selectScotiaBankCsvfile.txt
# Scotia_Inv_new uses the argument and retrieves the csv file name from the tmp file. .. fixed
# its all done with scriptsIPC now, both accoutName and csvfilename

from __future__ import absolute_import

import java.awt
import java.awt.event
import javax.swing
import javax.swing.event
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JTextField
from javax.swing import JLabel
from javax.swing import JButton
from javax.swing import JList
from javax.swing import JScrollPane

from javax.swing import DefaultListModel
from java.awt.event import ActionListener
from javax.swing.event import DocumentListener
from javax.swing.event import ListSelectionListener
from javax.swing import ListSelectionModel
from java.lang import Runnable
from java.awt import Dimension
from java.awt import GridLayout
from java.awt import BorderLayout
from java.awt import Toolkit
from javax.swing import BoxLayout
from javax.swing import Box
from javax.swing import JSeparator
from javax.swing import SwingConstants
from javax.swing import BorderFactory
from javax.swing import UIManager

#    execfile("AccountNames.py")
import AccountNames

#  ListDemo.java requires no other files. 
class ScotiaPicker(JPanel, ListSelectionListener):
    import sys
#    sys.stdout = open ('/dev/pts/3', 'w')
#    sys.stderr = open ('/dev/pts/3', 'w')
    global lineNo
    def lineNo():  return (str(sys._getframe(1).f_lineno) + ' ')

    print lineNo() + "ScotiaPicker"
    global list_
    list_ = None #JList()
    global listModel
    listModel = None #DefaultListModel()
    global pickButton
    pickButton = None #JButton()




    importString = "Import CSV"
    pickString = "Pick an Account"
    global accountNameDisplay
    accountNameDisplay = None #JTextField()
#    global accountSelected
#    print"locals1", locals()
#    print"globals1", globals()

    def __init__(self):
#        print "__init__"
        global list_
        global listModel
        global pickButton
        global accountNameDisplay
        super(ScotiaPicker, self).__init__(BorderLayout())
#        UIManager.getLookAndFeel().provideErrorFeedback(None) # should beep .. not wise with moneydance
        listModel = DefaultListModel()
        i = 0
        for i in xrange(0,len(AccountNames.Scotia.Accounts)): # list of all Known Scotia Accounts
           listModel.addElement(AccountNames.Scotia.Accounts[i])

        # Create the list and put it in a scroll pane.
        list_ = JList(listModel)
        list_.setSelectionMode(ListSelectionModel.SINGLE_SELECTION)
        list_.setSelectedIndex(0)
        list_.addListSelectionListener(self)
        list_.setVisibleRowCount(5)
        listScrollPane = JScrollPane(list_)
        importButton = JButton(self.importString)
        importListener = self.ImportListener(importButton)
        importButton.setActionCommand(self.importString)
        importButton.addActionListener(importListener)
        importButton.setEnabled(False)
        pickButton = JButton(self.pickString)
        pickButton.setActionCommand(self.pickString)
        pickButton.addActionListener(self.PickListener())
        
        accountNameDisplay = JTextField(10)
        accountNameDisplay.addActionListener(importListener)
        accountNameDisplay.getDocument().addDocumentListener(importListener)
        name = listModel.getElementAt(list_.getSelectedIndex()).__str__()
#        print "name",name
#        name = listModel.getElementAt(list_.getSelectedIndex()).toString()
        # Create a panel that uses BoxLayout.
        buttonPane = JPanel()
        buttonPane.setLayout(BoxLayout(buttonPane, BoxLayout.LINE_AXIS))
        buttonPane.add(pickButton)
        buttonPane.add(Box.createHorizontalStrut(5))
        buttonPane.add(JSeparator(SwingConstants.VERTICAL))
        buttonPane.add(Box.createHorizontalStrut(5))
        buttonPane.add(accountNameDisplay)
        buttonPane.add(importButton)
        buttonPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5))
        self.add(listScrollPane, BorderLayout.CENTER)
        self.add(buttonPane, BorderLayout.PAGE_END)
#        print "Done init"

    class PickListener(ActionListener):
        def actionPerformed(self, e):
#            print"PickListener action"
	    global pickButton
            global list_
            global listModel
            a = list_
            # This method can be called only if
            # there's a valid selection
            # so go ahead and remove whatever's selected.
            index = list_.getSelectedIndex()
#            print "PL index",index
#            print "picked Account" ,ScotiaAccounts[index]
            accountNameDisplay.setText(AccountNames.Scotia.Accounts[index])
#            accountSelected = ScotiaAccounts[index]
#            listModel.remove(index)
            size = listModel.getSize()
#            print "PickListener list size",size
            if size == 0:
                print "PickListener No Accounts in List, disable firing"
                pickButton.setEnabled(False)
            else:
#                print"PickListener Select an Account"
                if index == listModel.getSize():
#                    # removed item in last position
                    index -= 1
                list_.setSelectedIndex(index)
                list_.ensureIndexIsVisible(index)
#            print "Done PickListener actionPerformed"

    # This listener is shared by the text field and the import button. why ??
    # the Import Button is passed as an Argument and stored locally as button2
    class ImportListener(ActionListener, DocumentListener):
#        print "ImportListener"
        alreadyEnabled = False
        button2 = None # JButton()

        def __init__(self, button):
            """ generated source for method __init__ """
#            super(ImportListener, self).__init__()
#            print("DL init")
            self.button2 = button

        # Required by DocumentListener for  ActionListener.
        def actionPerformed(self, e):
	    global list_
	    global listModel
#	    global accountNameDisplay
#	    nonlocal accountNameDisplay # doesn't work SyntaxError: no viable alternative at input 'accountNameDisplay'
#            print "DL actionPer"
#            name = accountNameDisplay.getText()
#            print "DL User didn't type in a unique name..."
#            if name == "" or self.alreadyInList(name):
#	        print "HL calling Toolkit"
#                Toolkit.getDefaultToolkit().beep()
#                accountNameDisplay.requestFocusInWindow()
#                accountNameDisplay.selectAll()
#                return
            index = list_.getSelectedIndex()
#            print "DL get selected index",index
 #           print "importing csv file into Account  ", ScotiaAccounts[index]
#            import os
#            command = "jython Scotia-Inv-new.py " + "\"" + ScotiaAccounts[index] + "\"" # the account names have spaces in them
#            print "command ", command
#            ret = os.system(command) # started /bin/sh .. this works but not under a moneydance console
            import scriptsIPC
            scriptsIPC.accountName = AccountNames.Scotia.Accounts[index]
            import Scotia_Inv_new
            Scotia_Inv_new.main()
#            sys.argv = ['ScotiaPicker.py',AccountNames.Scotia.Accounts[index]]
#            execfile ("Scotia_Inv_new.py")
#            got a nice error message .... jython: can't open file 'Scotia-Inv-new.py': java.io.FileNotFoundException: Scotia-Inv-new.py (No such file or directory)
#            print "os.system ret ", ret
#            if ret == 127: print "command not found"
#            elif ret == 3: print "No such process"

#            execfile("Scotia-Inv-new.py")
#            if index == -1:
#                print "DL no selection, so insert at beginning"
#                index = 0
#            else:
#                print"DL add after the selected item"
#                index += 1
#            listModel.insertElementAt(accountNameDisplay.getText(), index)
            # If we just wanted to add to the end, we'd do this:
            # listModel.addElement(accountNameDisplay.getText());
#            print "DL Reset the text field"
#            accountNameDisplay.requestFocusInWindow()
#            accountNameDisplay.setText("")
            # Select the new item and make it visible.
#            list_.setSelectedIndex(index)
#            list_.ensureIndexIsVisible(index)

        # This method tests for string equality. You could certainly
        # get more sophisticated about the algorithm.  For example,
        # you might want to ignore white space and capitalization.
        def alreadyInList(self, name):
            print "DL alreadyInList"
            return listModel.contains(name)

        # Required by DocumentListener.
        def insertUpdate(self, e):
#            print "DL insertUpdate"
            self.enableButton()

        # Required by DocumentListener.
        def removeUpdate(self, e):
#            print "DL removeUpdate"
            self.handleEmptyTextField(e)

        # Required by DocumentListener.
        def changedUpdate(self, e):
            print "DL changedUpdate"
            if not self.handleEmptyTextField(e):
                self.enableButton()

        def enableButton(self):
#            print "DL enableButton"
            if not self.alreadyEnabled:
                self.button2.setEnabled(True)

        def handleEmptyTextField(self, e):
#            print "DL handleEmptyText"
            if e.getDocument().getLength() <= 0:
                self.button2.setEnabled(False)
                self.alreadyEnabled = False
                return True
            return False

    # This method is required by ListSelectionListener.
    def valueChanged(self, e):
        global list_
        global pickButton
#        print "valueChanged",list_.getSelectedIndex()
#        print "valueChangedC first" ,e.getFirstIndex()
#        print "valueChanged last" ,e.getLastIndex()
        #print "VC source",e.getSource() # javax.swing.JList ....
        if e.getValueIsAdjusting() == False:
            if list_.getSelectedIndex() == -1:
 #               print "No selection, disable pick button."
                pickButton.setEnabled(False)
            else:
 #               print "Selection, enable the pick button."
                pickButton.setEnabled(True)

    # 
    #      * Create the GUI and show it.  For thread safety,
    #      * this method should be invoked from the
    #      * event-dispatching thread.
    #      
    @classmethod
    def createAndShowGUI(cls):
#        print "createAndShowGUI"
        # Create and set up the window.
        frame5 = JFrame("ScotiaPicker")
        frame5.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)

        # Create and set up the content pane.
        newContentPane = ScotiaPicker()
        newContentPane.setOpaque(True)
        # content panes must be opaque
        frame5.setContentPane(newContentPane)
        # Display the window.
        frame5.pack()
        frame5.setSize(800, 350)
        frame5.setVisible(True)
#        print "Done createAndShowGUI"
        
#    class FunctionCaller(Runnable):
#       print "FunctionCaller"
#       def __init__(self, callback):
#           Runnable.__init__(self)
#           self._f = callback
#       def run(self):
#           self._f()

#    @classmethod
#    def main(cls, args):
#        print "main"
        # Schedule a job for the event-dispatching thread:
        # creating and showing this application's GUI.
###        javax.swing.SwingUtilities.invokeLater(Runnable())
#        javax.swing.SwingUtilities.invokeLater(ScotiaPicker.FunctionCaller(ScotiaPicker.createAndShowGUI))
# the above seems to break the stdout connection to the console


if __name__ == '__main__':
    import sys
    ScotiaPicker.createAndShowGUI()
#    ScotiaPicker.main(sys.argv)

