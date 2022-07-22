import socket
import threading
import sys

HEADER = 64
PORT = 5050
# SERVER = "172.17.240.1"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) 
FORMAT = 'utf-8'
DISCONNECT_MSG = "!Disconnect!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

def handle_client():
    print(f"[NEW CONECTIONS] {ADDR} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{ADDR}] {msg}") 
            conn.send("Msg received".encode(FORMAT))
            
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING} server is starting...")
start()
