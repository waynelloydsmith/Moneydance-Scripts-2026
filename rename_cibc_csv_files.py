#!/usr/bin/env python
# coding: utf8
# fix the CIBC downloaded  file names
# started by selectCIBCcsvfile.py using python .. not jython
# jython tried to start a new java JVM session .. moneydance got pissed off


import os
import sys
import re

def lineNo():  return (str(sys._getframe(1).f_lineno) + ' ')

def is_8_digit_number(s):
  return len(s) == 8 and s.isdigit()

def contains_8_digits(input_str):
    # \d{8} looks for exactly 8 consecutive digits
    if re.search(r'\d{8}', input_str):
        return True
    return False

# Define the directory path where your CSV files are located.
# You can change this to your specific path, or use '.' for the current directory.
directory_path = '/home/wayne/Downloads/'

# Change the current working directory to the target directory for simplicity
try:
    os.chdir(directory_path)
except OSError as e:
    print lineNO() +" Error changing directory:" + e
    sys.exit(1)

print lineNo() + " Current directory:", os.getcwd()

# Iterate over all files in the current directory
for filename in os.listdir('.'):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        if contains_8_digits(filename): # it already has an account number in the filename
           print lineNo() + "Skipping FileName that already has an account# in it ", filename # maybe BMO or one we already did
           continue

        fin = open( filename ,'r') # this is the csv file we are going to rename
        sym = fin.readline()
        sym = sym[4:] # remove the 4 Byte Order Mark bytes at the beginning of the file
        sym = sym.lstrip().rstrip() # remove trailing and proceeding garbage (\n, \r, \t, \f, \v)' ' and spaces)
        print lineNo() +" HEADER1",sym       # the account number .. we can get the Account Number here
        sym = sym.replace('"', '').replace("'", '').replace(",",'') # there are 17 ,'s and 34 quotes
        lst = sym.split() # default uses any sequence of whitespace characters (spaces, tab, Vtab, Linefeed , Formfeed , Carriage Return .) as the separator
        print lineNo() + " lst", lst
        print lineNo() + " We Found the Account Number in lst[0]", lst[0] # could check to see if it matches AccountName
#        print lineNo() + " lst[0]", lst[0]
#        print lineNo() + " lst[1]", lst[1]
        if not is_8_digit_number(lst[0]):
            print lineNo() + "Skipping file " + filename
            print lineNo() + "Its Not a CIBC csv file"
            continue
        # Construct the new filename
        # This example adds '_renamed' before the extension
        new_filename = filename.replace('.csv','-' + lst[0] + '-' + lst[1] + '.csv')
        print lineNo() + " newfilename: ", new_filename

#        raise Exception (lineNo() + "Take a Break")

        # Rename the file
        try:
            os.rename(filename, new_filename)
            print lineNo() + "Renamed:" + filename + "->" + new_filename
        except OSError as e:
            print lineNo() + "Error renaming file:" , filename, e

print("Renaming process complete.")
