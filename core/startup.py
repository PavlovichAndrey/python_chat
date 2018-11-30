# -*- coding: utf-8 -*-
from Client import *
host = '127.0.0.1'
port = 33222
if __name__ == "__main__":
    cl1 = Client(host,port,'cl1')
    cl1.run()
    cl1.stop()