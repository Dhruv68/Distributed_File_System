#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import socket as c


#client_IP_address = socket.gethostbyname(socket.gethostname)
client_IP_address = '127.0.0.1'
client_port = 8088
client_buffer = 1024
encoding_format = 'utf-8'

#client_IP_address = sys.argv[1]
#client_port = sys.argv[2]

def create_client():
    with c.socket(c.AF_INET, c.SOCK_STREAM) as client:
        client.connect((client_IP_address, client_port))
        #print(client.recv(client_buffer).decode('utf-8'))
        #client.sendall(b"Hello from client")
        while True:
                data = client.recv(client_buffer).decode(encoding_format)
                operation, msg = data.split("@")
                print(operation, msg)
                if operation.lower().strip() == "disconnect":
                    print(f"{msg}")
                    break
                elif operation.lower().strip() == "ack":
                    print(f"{msg}")
                
                print("Enter the operation to be performed")
                data = input("-> ")
                data = data.split(" ")
                operation = data[0]
                
                if operation.lower().strip() == "help":
                    client.send(operation.encode(encoding_format))
                elif operation.lower().strip() == "logout":
                    client.send(operation.encode(encoding_format))
                    break
                
    print(f"Disconnected from the server")
    client.close()


if __name__ == "__main__":
    create_client()

