# Distributed_File_System  
  
#### Group 6  
  
## Introduction to the Project:
    
The aim of this project is to build a Distributed File System with security features. The code was implemented in two phases    
    
	Phase 1: Developed a Simple Distributed File System    
	Phase 2: Implemented the security functionality of the Distributed File System
	    
This project will help you to implement an Encrypted distributed file system in which client/user can access the server and operate the functions in the server like:       
  1 Create Directory   
  2 Create File   
  3 Write File   
  4 Read File   
  5 Rename File   
  6 Delete File   
  7 Get the List of File  
  8 Change the permission    
  

## Implementation:

This distributed file system has three-level architecture:  
Level 1: All Clients (Authentic/Random users)   
Level 2: Master Node and Scheduler    
Level 3: Three Server Node.      

![IMG_20220318_154632__01__01](https://user-images.githubusercontent.com/34422998/159078539-618bda95-6b7f-4ae1-9d2e-1dd066d6c133.jpg)

#### Level 1: All Client  
The client is connected to only the master (semi-server) node. The client in the system needs to authenticate themselves in order to access the functionality provided by the server. The client implements the encryption on the data (like the content of the file, file name, and directory name), and validates themselves in order to access the server at the master node.     

#### Level 2: Master Node   
The master node is responsible for establishing the connection between the client and the servers. This acts as an intermediate node between the client and the replica servers. The task of the master node is to provide a link between the client and the server. Before establishing the connection, it will validate the client. The master node will also handle which client will access which file as per the permission provided by the owner. The scheduler will keep track of the files in the directory if any file is physically deleted from the server, it will show the pop-up message.        

#### Level 3: Servers  
All the client requests are processed by the servers that are directed by the master node. The response of each operation is again sent to the master server to be communicated back to the client. The server will have the encrypted data of the client and will not be able to get any information from it.   
    
 The master node is an important part of our architecture which will have the record of the actions made by the client and records of all permission and validation data.       
    
## Steps to Implement this project.  
  
Step 1:  
Install any IDE in which you want to perform this project. (Jupiter is more recommended). Here is the link to download Jupyter lab: https://jupyter.org/
       
            
Step 2:   
Install following libraries:   
  	Socket:	       To provide the socket values like IP address and port number to create no overlapping connection between clients and server 
      
	Socketserver:		To implement a server-client environment (the connection between server and client)    
	    
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
The simple way to install these libraries in your system is to write “pip install ________(library name)” on the anaconda prompt or cmd     
         
Note:     
Change the absolute Path in all server files and the scheduler file to the location of the files directory of each server in your system    
      
Step 3:  
Clone this project from the Github repository in your system.  
        
Step 4:  
Open the project in your IDE or Jupyter notebook and run all three server files. You will get the IP address of that server. Copy that server IP address and paste it into the second cell of the master file in the IP array sequentially. Enter the IP address in sequence like: IP = ["Server1 IP", "Server2 IP", "Server3 IP"]. Then run the master node.    
           
Step 5:  
Before running the “client-dhruv.ipynb” file edit the validation excel sheet in a master folder by adding your username and password.      
          
Step 6:  
After making changes in the validation file, run the “scheduler.ipynb” file present in the master folder. This file will execute continuously until you stop executing this file externally.      
        
Step 7:  
Now you can execute the “client-dhruv.ipynb” file. Initially, it will ask for a username and password. Enter the username and password that you have entered in the validation sheet.    
    
Step 8:     
 After that, you will be able to perform all the operations like creating a directory and file, writing a file, updating the file, deleting a file, renaming a file, listing file names, and a few more operations. All data will be stored in an encrypted format at the server end.    
     
Step 9:     
If you want to see the log of the operations performed by the client. You will find the logger text file in the master folder.     
    
Step 10:    
When you delete any file physically from any of the servers. The pop-up will be displayed automatically and indicates the file which is deleted and the server from which it is deleted.    
