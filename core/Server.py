# -*- coding: utf-8 -*-
import socket
import threading
import sys
class Client:
    
    def __init__(self,host,port):
        self.__host = host
        self.__port = port
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clients = []
        
    def run(self):
        try:
            self.__socket.bind((self.__host,self.__port))
        except:
            self.log("Bind failed. Error : " + str(sys.exc_info()))
            sys.exit(1)
        self.__socket.listen(10)
        self.log('server start...')
        while True:                
            conn, addr = self.__socket.accept()
            user = {'conn':conn,'addr':addr}
            threading.Thread(target = self.connect_client,args=(user)).start()                
        
    def stop(self):
        pass
    def connect_client(self):
        pass
    def start_communication(self):
        pass
    def broadcust(self):
        pass
    def get_port(self):
        pass
    def get_host(self):
        pass
    def log(self, msg):
        print(msg)

