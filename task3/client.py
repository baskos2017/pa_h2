import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, SERVER_PORT))

try:
    message = f"{num1},{num2}"
    client_socket.sendall(message.encode())

    result = client_socket.recv(1024).decode()
    print(f"Сума чисел: {result}")
except Exception as e:
    print(f"Сталася помилка: {e}")
finally:
    client_socket.close()
