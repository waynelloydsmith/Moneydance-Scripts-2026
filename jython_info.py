#!/usr/bin/env python
# coding: utf8

#def main():
class jython_info:

   def __init__(self):
        import sys
        from java.lang import System

        print "jython sys.version =", sys.version
        print "sys.builtin_module_names=", sys.builtin_module_names
        print "sys.exec_prefix=",sys.exec_prefix
        print "sys.prefix=",sys.prefix

        print "sys.path ="
        for val in sys.path:
                print val

        print "sys.registry['java.class.path']= "
        for val in sys.registry['java.class.path'].split(':'):
                print val

        print "sys.registry['java.library.path']= "
        for val in sys.registry['java.library.path'].split(':'):
                print val

        #print "sys.registry['java.ext.dirs']= "
        #for val in sys.registry['java.ext.dirs'].split(':'):
        #  print val

        #print "sys.cachedir=",sys.cachedir
        print "sys.registry['key'] = value -----------------------"
        r = sys.registry
        names = []
        for name in r.keys():
                names.append(name)
        names.sort() # now you can list the keys in alpha order
        for name in names:
                print name,' = ' , r [name]

        #for k in r.keys():
        #  print k,' = ',r[k]


        #  from java.lang import System
        #  >>> System.getProperty("user.dir")
        # '/home/wayne/source/Moneydance'
        # This is the cwd of java . i.e where is was launched

        #>> import os
        #>>> print os
        #org.python.modules.os
        #>>> dir(os)
        #['File', '__depends__', '_exit', 'curdir', 'environ', 'error', 'getcwd',
        #'initModule', 'java', 'javapath', 'listdir', 'makedirs', 'mkdir', 'name',
        #'pardir', 'path', 'pathsep', 'remove', 'rename', 'rmdir', 'sep', 'stat', 'unlink']
        #>>>
        import os      # everything in os appears to work
        print "dir(os)",dir(os)
        #print "os.File",os.File              # java.io.File
        print "os.curdir",os.curdir          # '.'

        print "os.error",os.error            #exceptions.OSError
        print "os.getcwd()",os.getcwd()      # works '/home/wayne/source/Moneydance'
        #print "os.initModule",os.initModule  # needs two arguments
        #print "dir(os.java)",dir(os.java)    #  >>> dir(os.java) ['__name__', 'applet', 'awt', 'beans', 'io', 'lang', 'math', 'net', 'nio',
        #'rmi', 'security', 'sql', 'text', 'util']
        #print "dir(os.javapath)",dir(os.javapath)      # >>> dir(os.javapath) ['File', 'System', '__doc__', '__file__',
        #'__name__', 'abspath', 'basename', 'commonprefix', 'dirname', 'exists', 'expanduser', 'gethome', 'getsize', 'getuser',
        # 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'java', 'join', 'normcase', 'normpath', 'os', 'samefile', 'split',
        #'splitdrive', 'splitext', 'walk']
        #print "os.javapath.getuser()",os.javapath.getuser() # os.javapath.getuser() >>>'wayne' looks like the same list of commands as os.path.*
        print "os.listdir()",os.listdir        # works like an ls command os.listdir("/home")
        print "os.makedirs()",os.makedirs      # needs one argument
        print "os.mkdir()",os.mkdir            # os.mkdir("junk") worked created a dir off /home/wayne/source/Moneydance os.curdir ??
        print "os.name",os.name                  # java
        print "os.pardir",os.pardir              # ".."
        print "dir(os.path)",dir(os.path)
        # >>> dir (os.path) ['File', 'System', '__doc__', '__file__', '__name__', 'abspath', 'basename', 'commonprefix',
        #'dirname', 'exists', 'expanduser', 'gethome', 'getsize', 'getuser', 'isabs', 'isdir', 'isfile', 'islink', 'ismount',
        # 'java', 'join', 'normcase', 'normpath', 'os', 'samefile', 'split', 'splitdrive', 'splitext', 'walk']
        #print "os.path.gethome()",os.path.gethome() # bunch of interesting functions in os.path
        print "os.pathsep",os.pathsep            # ":"
        print "os.remove()",os.remove          # needs one argument
        print "os.rename()",os.rename          # needs two aruments
        print "os.rmdir()",os.rmdir            # works on cwd
        print "os.sep",os.sep                    # "/"
        print "os.stat('test.py')",os.stat("test.py")     # os.stat("test.py") >>>(0, 0, 0, 0, 0, 0, 1343L, 1355972142000L, 1355972142000L, 0)
        print "os.unlink()",os.unlink          # needs one argument same as remove

        print "os.environ['key']="
        r = os.environ
        names = []
        for name in r.keys():
                names.append(name)
        names.sort()
        for name in names:
                print name,' = ' , r [name]

if  __name__ == '__main__': # script was started with execfile
  print ("__name__ is", __name__)
  print "jython_info.py executed by execfile"
  jython_info()
else:   # script was started by import
  print "jython_info.py was loaded by import"
  print ("__name__ is", __name__)
#import jython_info ... worked nothing got executed but it got loaded
#>>> jython_info.jython_info() # because everthing is in __init__ this works .. like runScripts.py



"""
        print "System.getProperties()['key'] = value  ------------------------------"

        props = System.getProperties()
        names = []
        for name in props.keys():
                names.append(name)
        #  print name,' = ' , props [name]
        names.sort() # now you can list the keys in alpha order
        for name in names:
                print name,' = ' , props [name]

        print "System.getProperties()['java.class.path'] is -----------------"
        for val in props['java.class.path'].split(':'):
                print val
        print "System.getProperties()['java.library.path'] is -----------------"
        for val in props['java.library.path'].split(':'):
                print val

"""  
