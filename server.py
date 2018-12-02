import socket

while True:
    HOST = ''
    PORT = 12045
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

