#!/usr/bin/python

import os
import sys
import time
import asciitime
from time import gmtime, strftime
import re

def printtime():
    print strftime("%a, %d %b %Y %H:%M:%S", gmtime())

def cls():
    os.system('clear')

def setwindowsize(x, y):
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=x, cols=y))

def printasciitime():
    asciitime.main('')

def printweather():

    os.system('curl -s wttr.in -o wttr && head -7 wttr')
    time.sleep(5)

def printsysinfo():
    print strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    print "\t\t\t  ===============\n\t\t\t    System info\n\t\t\t  ==============="
    print "Logged in as: "
    os.system('whoami')
    print "OS/Kernel:"
    os.system('uname -a' 'r')
    print "RAM:"
    os.system('head --line 2 /proc/meminfo')
    print "CPU:"
    cpuinfo = os.popen("cat /proc/cpuinfo").read().split('\n')

    cpu = []
    for s in cpuinfo:
        if("MHz" in s or "model name" in s):
            cpu.append(s)

    print cpu[0] + "\n" +  cpu[1]



    print "=" * 73
    time.sleep(5)

cls()



while(True):
    os.system('tput civis')
    setwindowsize(20, 73)
    printtime()
    printweather()
    cls()
    printasciitime()
    cls()
    printsysinfo()
    cls()
