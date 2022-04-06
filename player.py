from OSC import OSCServer,OSCClient, OSCMessage
from playsound import playsound
import time
import os
import signal
import sys

server = OSCServer(("0.0.0.0",9527))
counter = 0
def msg_callback(path, tags, args, source):
    print(int(args[0]))
    playsound('VAL.wav')
    counter+=1
    counter%=3
    time.sleep(30)

server.addMsgHandler("/msg",msg_callback)
while True:
    server.handle_request()
