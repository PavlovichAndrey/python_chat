# -*- coding: utf-8 -*-
import socket
import threading
from collections import deque
class Client:
    
    def __init__(self, host,port, name):
        self.__host = host
        self.__port = port
        self.__name = name
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__input_buffer = deque()
        self.__output_buffer = deque()
        self.__output_buffer_appand(name)
    
    def run(self):
        try:
            self.__socket.connect((self.get_host,self.get_port))
        except:
            pass
        threading.Thread(target = self.__receiv_msg).start()
        self.__send_msg()        
    
    def __send_msg(self):
        while True: 
            msg = self.__get_output_buffer()
            if msg is not None:
                self.__socket.send(str.encode(msg))        

    def __receiv_msg(self):
        while True:
            try:
                msg = self.__socket.recv(1024).decode("utf8")
                self.__input_buffer_appand(msg)
            except:
                self.__log("msg recvest error")

    
    def __input_buffer_appand(self, msg):
        self.__input_buffer.append(msg)   
        self.log(" i_b_a: "+ str(msg))
    
    def __output_buffer_appand(self, msg):
        self.__output_buffer.append(msg)   
        self.log(" o_b_a: " + str(msg))
        
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
        print("Client.log: ",msg)

c = Client("",777,"andrei")
c.get_host
c.get_port
c.log('test')
c.run()