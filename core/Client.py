# -*- coding: utf-8 -*-
import socket
import threading

class Client:
    
    def __init__(self):
        self.__host
        self.__port
        self.__socket
        self.__input_buffer
        self.__output_buffer
    
    def run(self):
        pass        
    def sendMsg(self):
        pass
    def receivMsg(self):
        pass
    def get_input_buffer(self):
        pass
    def get_output_buffer(self):
        pass
    def get_port(self):
        pass    
    def get_host(self):
        pass
    def log(self, msg):
        print(msg)
