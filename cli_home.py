#!/usr/bin/env python

import os,sys,time,asciitime,re,curses,signal
from time import strftime, localtime

def printtime():
    print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

def cls():
    os.system('clear')

def setwindowsize(x, y):
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=x, cols=y))

def printweather():
    os.system('curl -s wttr.in -o wttr && head -7 wttr')
    time.sleep(5)

def printsysinfo():
    print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
    print("\t\t\t  ===============\n\t\t\t    System Info\n\t\t\t  ===============")
    print("Logged in as: ")
    os.system('whoami')
    print("OS/Kernel:")
    os.system('uname -a' 'r')
    print("RAM:")
    os.system('head --line 2 /proc/meminfo')
    print("CPU:")
    try:
        cpuinfo = os.popen("cat /proc/cpuinfo").read().split('\n')
        cpu = []
        for s in cpuinfo:
            if("MHz" in s or "model name" in s):
                cpu.append(s)
        print(cpu[0] + "\n" +  cpu[1])
    except IndexError:
        print("/proc/cpuinfo not found")

    print("=" * 73)
    time.sleep(5)

def Exit_gracefully(signal, frame):
    cls()
    print("Exiting...")
    os.system('tput cnorm')
    sys.exit(1)

cls()

original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, Exit_gracefully)

while True:
    os.system('tput civis')
    setwindowsize(20, 73)
    printtime()
    printweather()
    cls()
    asciitime.main('')
    cls()
    printsysinfo()
    cls()
