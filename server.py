import socket
import os

# Railway بيحدد البورت تلقائياً، لو مش موجود هيستخدم 55000
PORT = int(os.environ.get("PORT", 55000))
HOST = "0.0.0.0" 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server is waiting for connection on port {PORT}...")

conn, addr = server.accept()
print(f"Connected by: {addr}")

while True:
    try:
        data = conn.recv(1024).decode()
        if not data: break
        print(f"Client: {data}")

        # هنا السيرفر بيرد (لو شغال من الـ Terminal)
        response = "Message Received!" 
        conn.send(response.encode())
    except:
        break
conn.close()