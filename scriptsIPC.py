#!/usr/bin/env jython
# coding: utf8
# scriptsIPC.py
# U should always import this script

accountName = None # used RunSripts writes it and BMO_Inv_new reads it
csvFile = None     # used by BMO_Inv_new and selectBMOCsvfile
IMPORT = None      # used by PreImport
MoneyDance = None  #used by everybody .. set by configConsole
logger = None      # used by many for logging messages
