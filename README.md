# Python-Chat-Server-

This project is a simple multi-client chat server and client application built using Python's `socket` and `threading` libraries. It allows multiple users to join a chat room, where they can communicate with each other in real-time.

## Features

- **Real-Time Communication**: The server handles multiple clients concurrently, enabling them to send and receive messages instantly.
- **Broadcasting**: Each message sent by a client is broadcast to all other clients connected to the server.
- **Username Identification**: When a user joins the chat, they provide a username, which is used to identify their messages in the chat.
- **Threading**: The server uses threading to manage multiple client connections simultaneously.

## How It Works

1. The server listens for incoming connections from clients.
2. Once a connection is established, the server spawns a new thread to handle the client, allowing multiple clients to connect concurrently.
3. The client sends its username to the server upon joining.
4. Messages from one client are broadcast to all other clients in real-time.
5. The server handles disconnections gracefully, removing clients that leave the chat.

## Getting Started

### Prerequisites

- Python 3.x
- Basic knowledge of Python and networking

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrsonsare/Python-Chat-Server-.git
