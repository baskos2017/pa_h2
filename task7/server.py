import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

clients = []

def handle_client(client_socket, client_address):
    try:
        print(f"Новий клієнт приєднався: {client_address}")
        client_socket.sendall("Вітаю! Ви приєдналися до чату.".encode())

        while True:
            message = client_socket.recv(1024).decode()

            for c in clients:
                if c != client_socket:
                    c.sendall(message.encode())

    except Exception as e:
        print(f"Сталася помилка з клієнтом {client_address}: {e}")
    finally:
        client_socket.close()
        clients.remove(client_socket)
        print(f"З'єднання з клієнтом {client_address} закрите.")

server_socket.listen(5)
print("Сервер запущено. Чекаю на з'єднання...")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
