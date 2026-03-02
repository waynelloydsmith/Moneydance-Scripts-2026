#!/usr/bin/env jython
# coding: utf8
# configConsole.py
# this script is started using execfile() in JConsole2026.java and jython270.main.java
# JConsole2026 also does import sys , import os , os.chdir('/opt/moneydance/scripts , and sets the local moneydance to context
# because the sitecustomize.py file is useless
# sitcustomize.py is useless because it is started by site.py using import sitcustomize
# don't use the print command in this script it will crash java
# use the java System.err.println instead  it prints to the moneydance console
# I have no idea where System.out.println shows up ????
# I have no idea why ?????
# there was a lot of crap in this file
# it all has to do with trying to get import to work the way I wanted it to.
# I moved the end result to the script CleanOut_sys_modules.py
# decided that the logger was not useful for managing the command history files
# now we just clean out duplicate and anything that says CRITICAL (old logger stuff)



import sys  # is also done in jython270.main.java and JConsole2026
import os
from java.lang import System
import time
#from java.util.logging import Logger, FileHandler, SimpleFormatter
import logging
from logging.handlers import RotatingFileHandler # there is also a TimedRotatingFileHandler and WatchedFileHandler
import javax.swing.SwingUtilities as SwingUtilities
import java.lang.Runnable as Runnable



sys.path.append('/opt/moneydance/scripts/')
#sys.path.append('/opt/moneydance/scripts/jython270/' #  moved this back to jython270.main.java

os.chdir('/opt/moneydance/scripts')

System.err.println("configConsole.py Started")

# it would be nice to have the logger running prior to starting the stuff below



#............................................................................................................ Set up the logger

jython270_LOG_FILENAME = System.getProperty("user.home")+ "/.jythonconsole.log"
jython270_COMMAND_FILENAME = System.getProperty("user.home") + "/.jythonconsole.save"
JConsole2026_LOG_FILENAME = System.getProperty("user.home")+ "/.JConsole2026.log"
JConsole2026_COMMAND_FILENAME = System.getProperty("user.home")+ "/.JConsole2026.save"
DEBUG = False # we can't use the logger yet

class CustomPrintHandler(logging.Handler):
    """
    A custom logging handler that outputs log records directly using the
    Python/Jython print function to stdout.
    doesn't use Streams ..just uses "print" to put the message on the users console.
    """
#   Override
    def emit(self, record):
        """
        Overrides the abstract emit method to handle log records.
        """
        # Formats the record using the handler's formatter if available,
        # otherwise uses a simple format.
#        if self.formatter:
        msg = self.format(record)
#        else:
#            # Basic fallback format
#            msg = f"{record.levelname}: {record.getMessage()}"

        # Use the print function for output
        # Using sys.stdout.write and flush might be more robust in some environments
        # but a simple print also works.
        try:
           sys.stdout.write(msg)
#            print(msg) # this works
            # Ensure the output is immediately visible
#            sys.stdout.flush()
        except Exception:
            self.handleError(record)

def cleanOutCommandFile (filename):
  if DEBUG: System.err.println ("checking file:"+ filename)
  with open(filename, 'r') as fin:
#    count = sum(1 for line in fin)
    data = fin.readlines()
    if DEBUG: System.err.println ("number of lines read:"+ str(len(data)))

# Write the file back starting from line 21 (index 20)
# could filter out all the logger messages in it too.
# would be nice to remove all the duplicates too
  unique_data = list(set(data))
  if DEBUG: System.err.println ("number of unique lines:" + str(len(unique_data)))
  dups = len(data) - len(unique_data)
  if DEBUG: System.err.println ("number of duplicate lines:" + str(dups))
  fin.close()

  with open(filename, 'w') as fout:
     count = 0
     skipped = 0
     for line in unique_data:
##        if DEBUG: System.err.println("line:" + line)
#     for line in data:         # look at all of  them
#     for item in my_list[20:]: # to skip the first 20
     # Example filter: skip all lines that contain 'CRITICAL'
        if 'CRITICAL' in line:
#            print ('skipping:',line)
            skipped = skipped + 1
            continue
        else:
            if DEBUG: System.err.println("writeing Command")
            fout.write(line)
            count = count + 1
     if DEBUG: System.err.println("Done")
#     count = sum(1 for line in fout) # says bad file descriptor
     if DEBUG: System.err.println ("number of lines written:" + str(count))
     if DEBUG: System.err.println ("number of lines skipped:"+ str(skipped))


#logging.shutdown() # jan 27 2026 .. trying to get rid of hanging streams to stdout didn't work
logger = logging.getLogger("JythonLogger")
#reset_logger_handlers("JythonLogger")
logger.setLevel(logging.DEBUG)  # Set the minimum logging level# messages below this level are ignored
                                   # Set the threshold level for this logger can be DEBUG INFO WARNINg ERROR CRITICAL
class MyLogger :

        if DEBUG: System.err.println("configConsole.py class MyLogger running")
#        logger_cmd = logging.getLogger("JythonLogger_cmd")
#        logger_cmd.setLevel(logging.CRITICAL)  # Set the minimum logging level .. we will never log to this logger its only for file management

#        for handler in list (logger.handlers):
#                if isinstance(handler, logging.StreamHandler):
#                        logger.removeHandler(handler)
#                        handler.close() # Close the stream properly
#                        if DEBUG: System.err.println("configConsole.py Closed a stream" + str(handler))


#        for handler in list (logger_cmd.handlers):
#                if isinstance(handler, logging.StreamHandler):
#                        logger.removeHandler(handler)
#                        handler.close() # Close the stream properly
#                        if DEBUG: System.err.println("configConsole.py Closed a stream" + str(handler))

        # get rid of any old handlers that are hanging around.
        for handler in list(logger.handlers):
                if isinstance(handler, logging.StreamHandler):
                        handler.flush()
                handler.close()
                logger.removeHandler(handler)
                if DEBUG: System.err.println("configConsole.py Killed a logger Handler")

#        for handler in list(logger_cmd.handlers):
#                if isinstance(handler, logging.StreamHandler):
#                        handler.flush()
#                handler.close()
#                logger_cmd.removeHandler(handler)
#                if DEBUG: System.err.println("configConsole.py Killed a logger_cmd Handler")


        #formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s(%(lineno)d) %(message)s')

        if Java_Parent == "jython270": # Java_Parent is set by the console when it starts up .. should be in global namespace
                # Create some rotating log file handlers
                file_handler_J270_LOG = RotatingFileHandler(
                        jython270_LOG_FILENAME,
                        mode='a',
                        maxBytes=1024*1024, # Max size of log file (e.g., 1MB),
                        backupCount=5 # Number of backup files to keep
                        )
                file_handler_J270_LOG.setFormatter(formatter)
                logger.addHandler(file_handler_J270_LOG)

#                file_handler_J270_CMD = RotatingFileHandler(
#                        jython270_COMMAND_FILENAME,
#                        mode='a',
#                        maxBytes=1024*100, # Max size of log file (e.g., 100k),
#                        backupCount=5 # Number of backup files to keep
#                        )
#                file_handler_J270_CMD.setFormatter(formatter)
#                logger_cmd.addHandler(file_handler_J270_CMD)
                cleanOutCommandFile (jython270_COMMAND_FILENAME)

        elif Java_Parent == "JConsole2026":
                file_handler_JC2026_LOG = RotatingFileHandler(
                        JConsole2026_LOG_FILENAME,
                        mode='a',
                        maxBytes=1024*1024, # Max size of log file (e.g., 1MB),
                        backupCount=5 # Number of backup files to keep
                        )
                file_handler_JC2026_LOG.setFormatter(formatter)
                logger.addHandler(file_handler_JC2026_LOG)

#                file_handler_JC2026_CMD = RotatingFileHandler(
#                        JConsole2026_COMMAND_FILENAME,
#                        mode='a',
#                        maxBytes=1024*100, # Max size of log file (e.g., 100k),
#                        backupCount=5 # Number of backup files to keep
#                        )
#
#                file_handler_JC2026_CMD.setFormatter(formatter)
#                logger_cmd.addHandler(file_handler_JC2026_CMD)
                cleanOutCommandFile (JConsole2026_COMMAND_FILENAME)
        else:
                System.err.println("Java_Parent is wrong")
                raise TypeError,'Java_Parent is Wrong'


        # set up logger handler for System.err messages to the moneydance console
        System_err_handler = logging.StreamHandler(System.err)
        System_err_handler.setLevel(logging.WARNING) # Log WARNINg and above to System.err too
        System_err_handler.setFormatter(formatter) # use same format as the file_handler
        logger.addHandler(System_err_handler) # only for the LOGs not for the command files

#        logger_cmd.critical("Checking") # this worked it created a new log file because the one there was too big :)
                                               # if you want your history back you have copy it from the jconsole.save.1 back to jconsole.save
                                               # I did get a message on the moneydance console saying the jython270 command file  was too big.
        # set up logger handler for sys.stdout messages to somewhere when critical .. sys.err just showed up same as System.err
        # get this error AttributeError: StdOutRedirector instance has no attribute 'flush'
        # I added the flush but still nothing shows up on the console ?? .. I give up on sys.stdout
        # will try System.out .. didn't work either something to do with the StdOutRedirector
#        con_format = logging.Formatter('%(message)s\n') # just the message  with  \n

        sys_out_handler = CustomPrintHandler()
        sys_out_handler.setLevel(logging.WARNING) # Log WARNINg and above to the console too
#        sys_out_handler.terminator = "" # get rid of \n .. didn't help
        con_format = logging.Formatter('%(asctime)s %(levelname)s %(module)s(%(lineno)d) %(message)s\n')
#        con_format = logging.Formatter('%(message)s\n') # just the message
        sys_out_handler.setFormatter(con_format) #
        logger.addHandler(sys_out_handler) # only for the LOGs not for the command file
# finally got this to work .... got rid of the streams ..

#...........end of class MyLogger:

#System.err.println("CHECKING scriptsIPC.MoneyDance")
#System.err.println(scriptsIPC.MoneyDance.DESCRIPTIVE_NAME)   # u'Moneydance 2024.2 (5172)'
#System.err.println(moneydance)                       # com.moneydance.apps.md.controller.Main@71c667eb
#System.err.println("configConsole.py was started by" + Java_Parent ) # determine which console started the configConsole.py script



# ...........................................................................test the logger
#logger.debug("configConsole.py Testing DEBUG")
#logger.info("configConsole.py Testing INFO")
#logger.warn("configConsole.py Testing WARNING")
#logger.error("configConsole.py Testing ERROR")
#logger.critical("configConsole.py Testing CRITICAL")
#logger_cmd.critical("configConsole.py Done") # fails now should go to the command history file



execfile("CleanOut_sys_modules.py") # looks for /opt/moneydance/scripts modules in sys.modules and deletes them .. was wiping out scriptsIPC .. moved it up here  .. maybe import it
#System.out.println(" Testing System.out.println") # doesn't appear anywhere

import scriptsIPC # needs sys.path.append first

scriptsIPC.MoneyDance = moneydance # this makes it available to all programs
scriptsIPC.logger = logger # this makes it available to all programs

# don't send stuff to the console yet it causes issues with plugged up streams . so keep level below WARNINg
logger.info("CHECKING scriptsIPC.MoneyDance")
logger.info(scriptsIPC.MoneyDance.DESCRIPTIVE_NAME)   # u'Moneydance 2024.2 (5172)'
logger.info(moneydance)                       # com.moneydance.apps.md.controller.Main@71c667eb
logger.info("configConsole.py was started by " + Java_Parent ) # determine which console started the configConsole.py script

logger.info("configConsole.py Done")
System.err.println("configConsole.py Done")

# some failed attempts to discover who started this script
#import inspect
#def get_importer_name():
#    # inspect.stack() returns a list of frame records
#    # We start from index 1 to skip the current frame (get_importer_name function's frame)
#    for frame in inspect.stack()[1:]:
#        # In Python 2.7 (common in Jython environments), frame is a tuple
#        # The second element (index 1) of the tuple is the filename
#        # We also check if the filename does not start with '<', which denotes internal libraries/mechanisms
#        if frame[1][0] != '<':
#            return os.path.basename(frame[1])
#    return "Unknown (possibly run as main or embedded)"

#if __name__ != '__main__':
#    importer_script = get_importer_name()
#    System.err.println("configConsole.py was imported by:", importer_script)
#else:
#    System.err.println("configConsole.py was started by __main__ or embedded")
# the above always says configConsole.py was started by __main__ or embedded .. its an engine.exec(execfile)) so it failed

#script_path = sys.argv[0]
#System.err.println("Script path: " + script_path) this failed too


