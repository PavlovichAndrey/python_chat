# -*- coding: utf-8 -*-
from core import *
from view import *

host = '127.0.0.1'
port = 33222


if __name__ == "__main__":
    v = ChatWindow("py_chat")
    cl = Client(host,port,"andrei")
    cl1.stop()
