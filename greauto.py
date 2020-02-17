#!/usr/bin/env python3
import os
import subprocess

def Print_Interfaces(interfaceList):
  for num, name in enumerate(interfaceList):
    print("%d) %s" % (num, name))

interfaceList = os.listdir('/sys/class/net/')
interfaceList.remove('lo')
Print_Interfaces(interfaceList)