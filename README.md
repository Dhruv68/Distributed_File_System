# Distributed_File_System  
  
#### Group 6  
  
## Introduction to the Project:

This project will help you to create a distributed file system in which one user can access the server and operate the functions in the server like:       
  1 Create Directory   
  2 Create File   
  3 Write File   
  4 Read File   
  5 Rename File   
  6 Delete File   
  7 Get the List of File   

## Implementation:

This distributed file system has three-level architecture:  
Level 1: All Clients (Authentic/Random users)   
Level 2: Master Node    
Level 3: Servers   

![IMG_20220318_154632__01__01](https://user-images.githubusercontent.com/34422998/159078539-618bda95-6b7f-4ae1-9d2e-1dd066d6c133.jpg)

#### Level 1: All Client  
The client node needs to connect with the master node, they are directly not able to connect to the server.   
The client needs to validate themselves to access the server at the master node.  

#### Level 2: Master Node   
The master node is connected to all the servers and it validates the client after validation it forwards the client's request to the server to perform the requested task.   

#### Level 3: Servers  
The server gets the request of the client through the master node and performs that task and sends the feedback to the client back through the Master node.


## Steps to Implement this project.  
  
Step 1:  
Install the jupyter in your System.  
        Here is the link to download Jupyter lab: https://jupyter.org/    
            
Step 2:   
Install following libraries:   
  Socket:   To provide the socket values like IP address and port number to create no overlapping connection between clients and server    
	Socketserver:  	To implement a server-client environment (the connection between server and client)    
	ThreadingTCPServer:   To implement the multithreading for multiple client connections at the same time. Also, to implement thread-locking for no overlapping write or edit operation    
	OS and SYS:   OS to get access to the directory and file path to implement all the changes    
	Pandas:   To access and update the excel sheet for permission and validation of clients    
	Pickle and Jason:   These libraries are used as the temporary storage unit while sending or fetching the data to the server or from the server.    
	Logging:   To configure the logger file to keep track of all the changes made by the client on the server    
	Traceback:   To print or retrieve the stack created to keep track of any update made by the client in the logger text file    
	Base64:   This library is used to implement encryption on data at the client-side to keep data secure at the server end     
	Pyaes, pbkdf2, binascii and secret:  pyaes to implement AES encryption method, pbkdf2 is a library to implement simple cryptography key derivation function, binascii to convert between binary and ASCII and secret to generate secure random numbers for managing secrets    
	Tkinter:  To implement the pop-up notification which will indicate whether any file is deleted physically or not    
	Time:   To implement the time loop for executing the scheduler function to search for a malicious attack    
 	Getpass:  To implement the hide input feature for passwords    
If you lack any single library from above, then install it before performing or implementing this project.      
    
        
Step 3:  
Download this project or clone it in your device.  
    
Step 4:  
Open this project then run the all server program (server1, server2, server3).
         Get the Ip address that you will get after executing the second cell.(output will be the Ip address like: 192.168.2.64)
           
Step 5:  
Copy that Ip address and write it inside the IP_address variable that you will find it in the master node in second cell.  
        Enter the IP address in sequance like: IP_address = ["Server1 IP", "Server2 IP", "Server3 IP"]
        Then run the master node.  
          
Step 6:  
Before running the client node, please enter you user name and password into the validation excell sheet.  
        
Step 7:  
Run the Client Node and enter the operation that you want to perform.  




