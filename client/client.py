
import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
        except:
            print("Connection lost.")
            break

def send_messages(sock):
    while True:
        message = input()
        if message:
            sock.send(message.encode('utf-8'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.19.146.29', 8080))  # Replace with your server's IP address

# Get the username and send it to the server
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Start the thread for receiving messages
receiver_thread = threading.Thread(target=receive_messages, args=(client,))
receiver_thread.start()

# Start sending messages
send_messages(client)
