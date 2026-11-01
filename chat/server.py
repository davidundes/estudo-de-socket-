
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

Clients = []

print(f"Server is running on {HOST}:{PORT}")

def broadcast(conn):
    while True:
        message = conn.recv(1024).decode('utf-8')
        for client in Clients:
            if client != conn:
                client.sendall(message.encode('utf-8'))


while True:
    conn, addr = s.accept()
    if conn not in Clients: 
        Clients.append(conn)
        print(f"Connected by {addr}")
        
    thread = threading.Thread(target=broadcast, args=(conn,))
    thread.start()
