import socket
import uuid

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

device_id = str(uuid.uuid4())

client_socket.sendto(device_id.encode(), (SERVER_IP, SERVER_PORT))

print("Ідентифікатор пристрою відправлено на сервер.")
