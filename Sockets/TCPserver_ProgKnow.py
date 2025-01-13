'''Programming Knowledge  this is the server program for the TCP protocol
judsonbelmont@Judsons-MacBook-Pro Shared_Folders % ipconfig getifaddr en0
192.168.1.11
'''
import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # af_Net is ipv4 protocl and sock stream is TCP

# server_socket.bind(('192.168.1.11',9999))
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5) ## 5 means that the server will wait and if a 6th tries to connect, it is refused

while True:
    print('Server waiting for connection')
    client_socket,addr=server_socket.accept()
    print('client connected from ',addr)
    while True:
        data=client_socket.recv(1024)
        if not data or data.decode('utf-f')=='END':
            break
        print('received frm client : %s' % data.decode('utf-8'))
        try:
            client_socket.send(bytes('Hey Client','utf-8'))
        except:
            print('Exited by the user')
    client_socket.closed()
server_socket.closed()        