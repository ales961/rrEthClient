import socket

HOST = '169.254.8.45'
PORT = 80


def tcpConnect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.setblocking(True)
    return s
