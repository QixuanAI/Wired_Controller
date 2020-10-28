#! /usr/bin/env python
'''
Description: Communication Core, support COM, MTP.
FilePath: /wired_controller/core.py
Author: qxsoftware@163.com
Date: 2020-10-28 09:52:38
LastEditTime: 2020-10-28 17:40:44
Refer to: https://github.com/QixuanAI https://pythonhosted.org/pyserial
'''
import config
import serial

Availabel={
    "baudrate":[1200,4800,9600,19200,38400,57600,115200,'custom'],
    "databits":[5,6,7,8,],

}
class COM:
    """
    A class for COM (Cluster Communication Port) data trasfer.
    """
    port = 'COM1'
    baudrate = 9600
    databits = 8
    parity = None
    stopbits = 1
    cmd_type = hex

    def __init__(self, port=0):
        pass

    def open(self, port):
        pass

    def send(self, msg):
        pass

    def close(self):
        pass

    def read(self):
        pass

class MTP:
    def __init__(self, port=0):
        pass

    def open(self, port):
        pass

    def send(self, msg):
        pass

    def close(self):
        pass

    def read(self):
        pass
