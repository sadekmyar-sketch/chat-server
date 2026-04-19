import socket
import os


PORT = int(os.environ.get("PORT", 8080))
HOST = "0.0.0.0" 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server is online and waiting on port {PORT}...")

while True:
    conn, addr = server.accept()
    print(f"Connected by: {addr}")
    
    try:
        while True:
            
            data = conn.recv(1024).decode('utf-8')
            
            if not data:
                break 
                
            print(f"Client says: {data}")
            
    
            response = f"Server received: {data}"
            conn.send(response.encode('utf-8'))
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed. Waiting for new connection...")
