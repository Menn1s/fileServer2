import socket

port = 5000
s = socket.socket()             #creating socket object
host = socket.gethostname()     #gets local machine name
s.bind((host, port))            #bind to port
s.listen(5)                     #start listening for client
print("Server is listening...")

while True:
    (conn, address) = s.accept() #Establish connection with client
    print("Got connection from" + str(address))
    file = input("Enter the name of the file: ")     #get name of file in same directory

    f = open(file, 'rb')			     #open the file under the read bits option
    l = f.read(1024)				     #read 1024 bytes to a variable
    while (l):
        conn.send(l)				     #send data
        print('Sent ',repr(1))			     #confirm variable data is sent
        l = f.read(1024)
    f.close()					     #read next 1024 bytes	
    
    print('Done sending')
    conn.close()

