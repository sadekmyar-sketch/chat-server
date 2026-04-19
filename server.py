import socket
import threading
import os

PORT = int(os.environ.get("PORT", 8080))
HOST = '0.0.0.0'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

clients = []

def broadcast(message, _conn):
    for client in clients:
        if client != _conn:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients: clients.remove(client)

def handle_client(conn, addr):
    clients.append(conn)
    while True:
        try:
            message = conn.recv(1024)
            if not message: break
            broadcast(message, conn)
        except: break
    conn.close()
    if conn in clients: clients.remove(conn)

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
