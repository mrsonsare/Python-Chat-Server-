import socket
import threading

def handle_client(client_socket):
    username = client_socket.recv(1024).decode('utf-8')
    print(f"User {username} has joined the chat.")
    
    welcome_message = f"User {username} has joined the chat."
    broadcast(welcome_message, client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            full_message = f"{username}: {message}"
            broadcast(full_message, client_socket)
        except:
            print(f"User {username} has left the chat.")
            clients.remove(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(5)
print("Server started on port 8080")

clients = []

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr}")
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
