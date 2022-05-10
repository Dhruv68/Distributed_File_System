#!/usr/bin/env python
# coding: utf-8

# Server Side implementation

# In[1]:


import os
import sys
import socket as s
import threading
import traceback
from socketserver import ThreadingTCPServer


#IP_address = socket.gethostbyname(socket.gethostname)
IP_address = '127.0.0.1'
port = 8088
buffer = 1024
max_connections = 1000
encoding_format = 'utf-8'


#IP_address = sys.argv[1]
#port = sys.argv[2]

def perform_operation(conn, addr):
    print(f'[Connected] Connection Established with {addr}')
    conn.send("ACK@Welcome to File Server\n".encode(encoding_format))
    
    while True:
        data = conn.recv(buffer).decode(encoding_format)
        data = data.split("@")
        
        operation = data[0]
        
        if operation.lower().strip() == "logout":
            threading.activeCount() +1
            break
        elif operation.lower().strip() == "help":
            data = "ACK@"
            data += "Logout: Disconnect from the server\n"
            data += "Help: Lists all supported operations"
            
            conn.send(data.encode(encoding_format))
            
         
    #conn.sendall(f"Hello from server\n".encode('utf-8'))
    print(f"[Disconnect] Disconnected {addr} client")
    conn.close()


def create_server():
    #creating a new socket
    #socket functions takes as argument the socket family and socket type
    with s.socket(s.AF_INET, s.SOCK_STREAM) as server:
        server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        try:
            server.bind((IP_address, port))
        except:
            print("Error in binding the socket")
            sys.exit()
        thread_list = []
        server.listen(max_connections) #queues upto 10 requests
        print(f"Server listening upto {max_connections - (threading.activeCount()-1)} connections\n")
        while True:
            connection, client_addr = server.accept()
            try:
                conn_thread = threading.Thread(target=perform_operation, args=(connection, client_addr))
                conn_thread.start()
                #thread_list.append(conn_thread)
                print(f"Total Active connections {threading.activeCount()-1}")
            except:
                print("Error in starting the thread")
                traceback.print_exc()
        '''if len(thread_list) >0:
            for t in thread_list:
                 t.join()'''


if __name__ == "__main__":
    create_server()
    