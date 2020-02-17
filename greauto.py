#!/usr/bin/env python3
import os
import subprocess

def Select_Interface(interfaceList):
  interfaceList = os.listdir('/sys/class/net/')
  interfaceList.remove('lo')
  for num, name in enumerate(interfaceList):
    print("%d) %s" % (num, name))
  interfaceNum = input('Please Select an interface for input:') 
  if isinstance(interfaceNum, int):
    if interfaceNum >= 0 and interfaceNum <= interfaceList.len():
      happy
  else:
    print('Invalid input!')

Select_Interface()