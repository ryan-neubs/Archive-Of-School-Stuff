#!/usr/bin/env python3

from socket import *
import time

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

with socket(AF_INET, SOCK_STREAM) as s:
    handler, addr = s.accept()
    s.sendall(b'Hello, world')
    data = handler.recv(1024)

print('Received', repr(data))
