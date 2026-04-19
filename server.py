import socket
import threading
import os

PORT = int(os.environ.get("PORT", 8080))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', PORT))
server.listen(1)

print(f"Server is waiting for connection...")

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data: break
            print(f"\n[Client]: {data}")
            print("You (Server): ", end="") 
        except:
            break

conn, addr = server.accept()
print(f"Connected to {addr}")


threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()


while True:
    msg = input("You (Server): ")
    if msg.lower() == 'exit': break
    conn.send(msg.encode('utf-8'))

conn.close()
                
           
