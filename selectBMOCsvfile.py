#!/usr/bin/env python
# coding: utf8
# select a csv file to import
# was spawned by BMO_Inv_new.py  with ... subprocess Popen,PIPE
# now its just execfile()
# started by BMO_Inv_new.py

#class selectBMOCsvfile:
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
  frame = JFrame("Pick a csv File")
  frame.setSize(200, 225)
  frame.setLayout(BorderLayout())
  panel = JPanel()

  frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)

  chooseFile = JFileChooser("/home/wayne/Downloads") # where the csv files are saved using BMO csv export tool
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
    print "64 Selected:",path2 #
  else:
    print "66 No Selection Made"   # if I cancel or close the window .. I get this .. end up with some white space around it
    path2 = "none"
  import scriptsIPC
  scriptsIPC.csvFile = path2
  logger = scriptsIPC.logger
  logger.info("Finished")
#  file2 = open('/opt/moneydance/scripts/tmp/selectBMOCsvfile.txt', 'wb')
#  print "53 Opened", file2
#  file2.write(path2)
#  file2.close()
  print "56 Done selectBMOCsvfile.py"

if  __name__ == '__main__': # was started with execfile
  print "selectBMOCsvfile.py executed by execfile"
  main()
else:   # was started by import
  print ("import passed __name__" , __name__)
  print "selectBMOCsvfile.py was imported"

##  exit(0) crashes moneydance
# this program freezes everything in moneydance while the JFileChooser is up
#The freezing issue with JFileChooser is a well-known problem in Swing applications,
#often caused by the Event Dispatch Thread (EDT) being blocked while the file chooser accesses the file system,
# network drives, or interacts with specific operating system components
# see Alternatives2JFileChooser.txt
# I tried running this in a terminal with jython and it didn't freeze moneydance
# it must be messing with the moneydance java EDT thread while its running


