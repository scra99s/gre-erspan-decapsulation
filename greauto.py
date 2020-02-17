#!/usr/bin/env python3

import subprocess
import os

interfaceList = os.listdir('/sys/class/net/').splitlines()
interfaceList.remove('lo')
print(interfaceList)


#result = subprocess.run(['ip -br addr|cut -d" " -f1'], stdout=subprocess.PIPE)

#interfaceList = result.stdout.decode('utf-8').splitlines()
#interfaceList.remove('lo')

#print(interfaceList)