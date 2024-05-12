import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

print("UDP сервер запущено.")

while True:
    data, client_address = server_socket.recvfrom(1024)
    
    print(f"Новий пристрій під'єднався: {data.decode()} з IP-адресою {client_address[0]} та портом {client_address[1]}")
