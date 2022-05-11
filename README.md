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
    



