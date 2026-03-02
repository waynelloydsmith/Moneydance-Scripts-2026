#!/usr/bin/env python
# coding: utf8
# for some unknown reason sys.module is polluted with old modules from previous jconsole2026 runs
# this script looks for them and deletes them
# this runs this when Jconsole2026 is launched
# configConsole.py starts it with execfile  when Jconsole2026 is launched
# don't use "print" in this script


import importlib
from java.lang import System # for println

'''
unwanted_list = ["runScripts", "AccountNames", "etc"]

found_unwanted = False
for module_name in sys.modules.keys():
    if module_name in unwanted_list:
        found_unwanted = True
        print("[!] Unwanted module found:" ,module_name)
# says it found runScripts and AccountNames
# how about delete all the modules from /opt/moneydance/scripts

'''
#System.err.println("--- CleanOut_sys_modules Identifying garbage in sys.modules ---")
logger.info("--- CleanOut_sys_modules Identifying garbage in sys.modules ---")

for name, module in sys.modules.items():
    # Use getattr to safely access the __file__ attribute, which may not exist for built-ins
    module_path = getattr(module, '__file__', 'Built-in or not found path')
#    print("module_path ",module_path) # this worked prints a large list
    if '/opt/moneydance/scripts' in str(module_path):
#       System.err.println('found one>' + name)
       logger.info('found one>' + name)
       del sys.modules[name] # worked

'''
first run
--- Identifying garbage in sys.modules ---
found one>runScripts
found one>AccountNames
# the second time I ran it both runScripts and AccountNames were gone

'''

