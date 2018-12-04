# -*- coding: utf-8 -*-
from core.Client import *
import view.view as v

host = '127.0.0.1'
port = 33222


if __name__ == "__main__":
    cl = Client(host,port,"nikita")
    #threading.Thread(target = cl.run()).start()                
    #cl.run()
    v = v.ChatWindow("py_chat")
    v.set_send_function(cl.msg_sendler)
    v.set_get_msg_function(cl.get_input_buffer)
    cl.run()
    v.run()
    cl.stop()    
