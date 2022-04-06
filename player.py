from OSC import OSCServer,OSCClient, OSCMessage
server = OSCServer(("0.0.0.0",9527))
def msg_callback(path, tags, args, source):
    print(int(args[0]))
server.addMsgHandler("/msg",msg_callback)
while True:
    server.handle_request()
