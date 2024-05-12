import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

server_socket.listen(1)
print("Сервер запущено. Чекаю на з'єднання...")

while True:
    connection, client_address = server_socket.accept()
    print(f"З'єднання від {client_address}")

    try:
        data = connection.recv(1024).decode()
        numbers = data.split(',')
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        result = num1 + num2
        
        connection.sendall(str(result).encode())
        print("Результат відправлено клієнту.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        connection.close()
