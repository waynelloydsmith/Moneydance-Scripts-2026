#!/usr/bin/env jython
# coding: utf8
# used by BMO_Inv_new

from javax.swing import Timer
from java.awt.event import ActionListener
from javax.swing import JFrame
#from java.awt import BorderLayout
#from javax.swing import JTree
#from javax.swing import JScrollPane
#from java.awt import Dimension
from javax.swing import JPanel
#from javax.swing import JButton
from javax.swing import JLabel
from javax.swing import WindowConstants

# this was is by  BMO_Inv_new.py for error display
def ShowMessage66 (message) :
        #  mframe = JFrame("Message")
        global mframe66    # need this for WindowClose66() to work
        mframe66 = JFrame(message)
        mframe66.setSize(1000, 50)
        mframe66.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
        mpnl66 = JPanel()
        mframe66.add(mpnl66)
        mlabel66 = JLabel(str(message))
        mpnl66.add(mlabel66)
        mlabel66.setVisible(True)
        mframe66.setVisible(True)
        WindowClose66()

class WindowClose66(ActionListener):  # this is used by  BMO_Inv_new.py for error display
    def __init__(self):
        from javax.swing import Timer
        self.timer = Timer(5000, self) # 5 seconds
        self.timer.start()
    def actionPerformed(self, e):
        self.timer.stop()
        mframe66.dispose()

