#!/usr/bin/env python
# coding: utf8
# select a csv file to import
# spawned by ScotiaInvnew.py  with ... subprocess Popen,PIPE

#class selectScotiaBankCsvfile:
def main():

  import sys
  from java.awt import BorderLayout
  from javax.swing import BorderFactory
  from javax.swing import JFileChooser
  from javax.swing import JTextArea
  from javax.swing import JScrollPane
  from javax.swing import JButton
  from javax.swing import JToolBar
  from javax.swing import JPanel
  from javax.swing import JFrame
  from javax.swing.filechooser import FileNameExtensionFilter
  import javax.swing as swing
  import java.awt as awt
  import subprocess
  import time

#  raise Exception ("Exception selectScotiaCsv")
  def setFileChooserFont(comp, font):
    """Recursively sets the font for all components within a container."""
    for x in range(comp.getComponentCount()):
        child = comp.getComponent(x)
        if isinstance(child, awt.Container):
            setFileChooserFont(child, font)
        try:
            child.setFont(font)
        except Exception, e:
            # Handle components that do not support setFont
            pass

  custom_font = awt.Font("Arial", awt.Font.PLAIN, 18)


#  frame = JFrame(runScripts.accountName)
  frame = JFrame("pick a file")
  frame.setSize(200, 225)
  frame.setLayout(BorderLayout())
  panel = JPanel()

  frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)

  chooseFile = JFileChooser("/home/wayne/Downloads") # where the csv files are saved using ScotiaBank csv export tool
  setFileChooserFont(chooseFile, custom_font) # jan 11 2026
  filter = FileNameExtensionFilter("csv files", ["csv"])
  chooseFile.setFileFilter(filter)
  ret = chooseFile.showDialog(frame,"Import Selected File")
 
  if ret == JFileChooser.APPROVE_OPTION:
    file = chooseFile.getSelectedFile() # file is a list of strings
    desc = chooseFile.getDescription(file) # just get the file name with no path
    curdir = chooseFile.getCurrentDirectory() # says it returns a file .. just get the directory /home/wayne/Downloads
    path = file.getAbsolutePath()     # /home/wayne/Downloads/transactionHistory.csv
    canpath = file.getCanonicalPath() # /home/wayne/Downloads/transactionHistory.csv
    path2 = file.getPath()            # /home/wayne/Downloads/transactionHistory.csv
#    print chooseFile.getName(file) # just the file name
#    print file # printed the entire path plus filename ... this is a list of two strings
#    print desc # just get the file name with no path
    print path2 #
  else:
    print "63 No Selection Made"   # if I cancel or close the window .. I get this .. end up with some white space around it
    path2 = "none"
  import scriptsIPC
  scriptsIPC.csvFile = path2 # put the selected file name in scriptsIPC
  logger = scriptsIPC.logger
  if logger != None:
        logger.info("Finished")
#  file2 = open('/opt/moneydance/scripts/tmp/selectScotiaBankCsvfile.txt', 'wb')
#  print file2
#  file2.write(path2)
#  file2.close()
  print "Done selectScotiaBankCsvfile.py"
  frame.dispose()

if  __name__ == '__main__': # was started with execfile
  print "selectScotiaBankCsvfile.py executed by execfile"
  main()
else:   # was started by import
  print ("import passed __name__" , __name__)
  print "selectScotiaBankCsvfile.py was imported"

