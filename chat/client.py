import socket
import threading 

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server = input("Enter the server IP address: ")
CLIENT.connect((Server, 12345))
nickname = input("Choose a nickname: ")
CLIENT.send(nickname.encode('utf-8') + " Join in chat!".encode('utf-8'))

def receive():
    while True:
        message = CLIENT.recv(1024).decode('utf-8')
        print(message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:
    message = f'{nickname}:{input("")}'
    CLIENT.send(message.encode('utf-8'))
