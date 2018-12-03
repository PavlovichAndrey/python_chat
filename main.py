# -*- coding: utf-8 -*-
from core.Client import *
import view.view as v

host = '127.0.0.1'
port = 33222


if __name__ == "__main__":
    cl = Client(host,port,"andrei")
    #threading.Thread(target = cl.run()).start()                
    #cl.run()
    v = v.ChatWindow("py_chat", cl)
    v.run()
    cl.stop()    
