#!/usr/bin/env python3
import os
import subprocess

def Select_Interface(interfaceList = []):
  interfaceNum = None
  while interfaceNum = None:
    for num, name in enumerate(interfaceList):
      print(" %d) %s" % (num, name))
    interfaceNum = input('Please Select an interface for input:') 
    if isinstance(interfaceNum, int):
      if interfaceNum >= 0 and interfaceNum <= interfaceList.len():
        return interfaceNumber
    else:
      print('Invalid input!')

interfaceList = os.listdir('/sys/class/net/')
interfaceList.remove('lo')
Select_Interface(interfaceList)