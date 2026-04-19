import socket
import threading
import os


PORT = int(os.environ.get("PORT", 8080))
HOST = '0.0.0.0'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server is running on port {PORT} and waiting for connections...")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            
            print(f"[{addr}] says: {data}")
            
            
            response = f"Received: {data}"
            conn.send(response.encode('utf-8'))
            
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")


while True:
    conn, addr = server.accept()
    
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
