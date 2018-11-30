# -*- coding: utf-8 -*-
import socket
import threading
from collections import deque
class Client:
    
    def __init__(self, host,port):
        self.__host = host
        self.__port = port
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__input_buffer = deque()
        self.__output_buffer = deque()
    
    def run(self):
        pass        
    def __sendMsg(self):
        pass
    def __receivMsg(self):
        pass
    
    def __input_buffer_appand(self, msg):
        self.__input_buffer.append(msg)   
    
    def __output_buffer_appand(self, msg):
        self.__output_buffer.append(msg)   
        
    def __get_input_buffer(self):
        try:
            return self.__input_buffer.popleft()
        except IndexError:
            return None

    def __get_output_buffer(self):
        try:
            return self.__output_buffer.popleft()
        except IndexError:
            return None

    def get_port(self):
        pass    
    def get_host(self):
        pass
    def log(self, msg):
        print(msg)
