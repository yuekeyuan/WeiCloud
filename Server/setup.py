import sys
import core.server
from core.server import *
#start the server

if __name__ == "__main__":

    #start checker

    #start communication

    # start server
    sv = Server(sys.argv)
    sv.start()
    print("OK")