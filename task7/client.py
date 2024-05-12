import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            print(message)
    except Exception as e:
        print(f"Сталася помилка: {e}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, SERVER_PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

try:
    while True:
        message = input()
        client_socket.sendall(message.encode())
except KeyboardInterrupt:
    print("Вихід з чату.")
finally:
    client_socket.close()
