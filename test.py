#!/usr/bin/env python
# coding: utf8
#global memo
#memo = 'global'
#print "running test.py"
#import scriptsIPC
#scriptsIPC.accountName ="jackTHEbear"
#scriptsIPC.csvFile = "CSVfile"
#raise Exception ("fuck you")
#sys.stderr = sys.stdout
import sys
from java.lang import System


#sys.stderr = sys.__stderr__

#sys.stderr = sys.__stderr__
# sys.stderr.flush() # didn't help

#sys.stderr = sys.__stderr__ # put it back to where it belongs .. this worked

sys.stdout.write("Test.py sys.stdout "+ str(sys.stdout) +"\n")
sys.stderr.write("Test.py sys.stderr "+ str(sys.stderr) +"\n")
System.err.println("Test.py System.err " + str(System.err) )
System.out.println("Test.py System.out " + str(System.out) )
System.err.println("Test.py System.err showing System.out " + str(System.out) )

print("Test.py print() to stdout")
