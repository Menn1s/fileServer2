import socket

s = socket.socket()
host = input('Enter the host IP: ')     #request server IP
port = 5000

s.connect((host, port))

with open('received_file', 'wb') as f:  #create file and its object
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)             #receive data to the data variable
        print('data=%s', (data))        #print the data being received
        if not data:
            break                       #break when done
        f.write(data)                   #write data to file object

    
f.close()
print('Successfully got the file')
s.close()
print('connection closed')
