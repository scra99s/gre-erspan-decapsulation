#!/usr/bin/env python3
import os
import subprocess
import ipaddress
from pyroute2 import IPDB
from pyroute2 import IPRoute

class greauto:

  def __init__(self):
    self.ipdb = IPDB(mode='explicit')
    self.interfaceList = self._Get_Interfaces()
    #self.inputInterface = self._Set_Input_Interface()
    #self.localHostAddress = self._Set_Local_Host_Address()
    #self.localGateway = self._Set_Local_Gateway()
    #self.ouputInterface = self._Set_Output_Interface()


  def Clear_Interfaces(self):
    #Disable all interfaces and clear
    for interface in self.ipdb.by_name.keys():
      if interface != 'lo':
        self.ipdb.interfaces[interface].begin()
        self.ipdb.interfaces[interface].down()
        for ip in self.ipdb.interfaces[interface]['ipaddr']:
          print('Deleting ' + ip[0] + ' on ' + interface)
          self.ipdb.interfaces[interface].del_ip(ip[0], ip[1])
        self.ipdb.interfaces[interface].commit()
    self.ipdb.release()


  def _Set_Local_Gateway(self):
    while True:
      try:
        ip = ipaddress.ip_address(input('What is your gateway address: '))
        if ip in ipaddress.ip_network(self.localHostAddress):
          return ip
        else:
          print('%s is not in the %s range!' % (ip, self.localHostAddress))
      except ValueError:
        print('Invalid IP address!')


  def _Set_Local_Host_Address(self):
    while True:
      try:
        ip = ipaddress.ip_network(input('What is the IP address of the input interface (ip/cidr): '), strict=False)
        print('%s is a valid IP%s address.' % (ip, ip.version))
        return ip
      except ValueError:
        print('Invalid IP address!')


  def _Set_Input_Interface(self):
    while True:
      for num, name in enumerate(self.interfaceList):
        print(" %d) %s" % (num, name))
      try:
        interfaceNum = int(input('Please select the input interface: '))
        if interfaceNum >= 0 and interfaceNum <= len(self.interfaceList):
          print('You selected interface: ' + self.interfaceList[interfaceNum])
          return self.interfaceList[interfaceNum]
        else:
          print('Invalid input!')
      except:
        print('Invalid input!')


  def _Set_Output_Interface(self):
    while True:
      for num, name in enumerate(self.interfaceList):
        if name != self.inputInterface:
          print(" %d) %s" % (num, name))
      try:
        interfaceNum = int(input('Please select the output interface:'))
        if interfaceNum >= 0 and interfaceNum <= len(self.interfaceList):
          print('You selected interface: ' + self.interfaceList[interfaceNum])
          return self.interfaceList[interfaceNum]
        else:
          print('Invalid input!')
      except:
        print('Invalid input!')


  def _Get_Interfaces(self):
    interfaceList = os.listdir('/sys/class/net/')
    interfaceList.remove('lo')
    return interfaceList


if __name__ == "__main__":
  grespan = greauto()
  grespan.Clear_Interfaces()

