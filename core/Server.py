# -*- coding: utf-8 -*-
import socket
import threading
import sys
class Server:
    
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
            threading.Thread(target = self.__connect_client,args=(client,)).start()                
        
    def stop(self):
        self.__socket.close()
        sys.exit(0)
    def __connect_client(self, client):
        name = client['conn'].recv(1024).decode("utf8")
        client['name'] = name
        self.__clients.append(client)
        self.log(str(client['name']) +" "+str(client['name']) +" is connected\n")
        self.__start_communication(client)
        
    def __start_communication(self,client):
        self.__broadcast(str(client['name']) + " joined the chat\n")                        
        while True:
            try:
                msg = client['conn'].recv(self.__msgsize)                    
            except:
                try:
                    self.__clients.remove(client)
                except:
                    pass
                self.log(str(client['name']) +" "+str(client['name']) +" is disconnected\n")
                if len(self.__clients) == 0:
                    self.stop()            
                break
            self.__broadcast(str(client['name'])+ " "+str(client['addr'])+":  "+ bytes.decode(msg))            
            
            
    def __broadcast(self,msg):
        for client in self.__clients:
            client['conn'].send(str.encode(msg))
 
    def get_port(self):
        return self.__port
    def get_host(self):
        return self.__host
    def log(self, msg):
        print(msg)

if __name__ == "__main__":
    serv = Server("127.0.0.1",33222)
    serv.run()
    serv.stop()