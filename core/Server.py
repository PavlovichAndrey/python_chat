# -*- coding: utf-8 -*-
import socket
import threading
import sys
class Client:
    
    def __init__(self,host,port):
        self.__msgsize = 1024
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
            client = {'conn':conn,'addr':addr}
            threading.Thread(target = self.__connect_client,args=(client)).start()                
        
    def stop(self):
        pass
    def __connect_client(self, client):
        name = client['conn'].recv(1024).decode("utf8")
        client['name'] = name
        self.__clients.append(client)
        self.log(client, "is connected")
        self.__start_communication(client)
        
    def __start_communication(self,client):
        self.__broadcast(client['name'], " joined the chat")                        
        while True:
            msg = client['conn'].recv(self.__msgsize)
            self.__broadcast(bytes.decode(msg))            
            
    def __broadcust(self,msg):
        for client in self.__clients:
            client['conn'].send(client['name'], " ",client['addr'],":  ", msg)
 
    def get_port(self):
        pass
    def get_host(self):
        pass
    def log(self, msg):
        print(msg)

