import socket

PORT = 5050
SERVER = "localhost" # Or socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE ="!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


client = connect()
send(client, "Testing")
input()
send(client, DISCONNECT_MESSAGE)


