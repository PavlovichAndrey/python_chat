# -*- coding: utf-8 -*-
import socket
import threading
import sys
from collections import deque
class Client:
    
    def __init__(self, host,port, name):
        self.__host = host
        self.__port = port
        self.__name = name
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__input_buffer = deque()
        self.__output_buffer = deque()
        #self.output_buffer_appand(name)
        self.msg_sendler = self.__send_msg
        
    def run(self):
        try:
            self.__socket.connect((self.get_host(),self.get_port()))
        except:
            self.log('socket connect error')
            sys.exit(1)
        threading.Thread(target = self.__receiv_msg).start()
        self.__send_msg(self.__name)        
        
    def stop(self):
        self.__socket.close()
        sys.exit(1)
        
    def __send_msg(self, msg):    
        try:
            self.__socket.send(str.encode(msg))        
        except:
            self.log("send_msg_error")
            
    def __receiv_msg(self):
        while True:
            try:
                msg = self.__socket.recv(1024).decode("utf8")
                self.__input_buffer_appand(msg)
            except:
                self.log("msg recvest error")
                self.stop()
                
    def __input_buffer_appand(self, msg):
        self.__input_buffer.append(msg)   
        self.log(" i_b_a: "+ str(msg))
    
    def output_buffer_appand(self, msg):
        self.__output_buffer.append(msg)   
        self.log(" o_b_a: " + str(msg))
        
    def get_input_buffer(self):
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
        return self.__port
    def get_host(self):
        return self.__host
    def log(self, msg):
        print("Client.log: ",msg)

