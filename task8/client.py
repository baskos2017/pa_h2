import requests

def send_http_request(url, method='GET', data=None):
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, data=data)
        elif method == 'PUT':
            response = requests.put(url, data=data)
        elif method == 'DELETE':
            response = requests.delete(url, data=data)
        else:
            print("Непідтримуваний метод HTTP-запиту.")
            return

        print("Статус-код:", response.status_code)
        print("Заголовки:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("Тіло відповіді:", response.text)

    except requests.exceptions.RequestException as e:
        print("Помилка під час виконання HTTP-запиту:", e)

url = input("Введіть URL ресурсу: ")
method = input("Введіть метод HTTP-запиту (GET, POST, PUT, DELETE): ").upper()
data = None

if method in ['POST', 'PUT']:
    data = {}
    while True:
        key = input("Введіть назву поля: ")
        value = input("Введіть значення поля: ")
        data[key] = value
        more_data = input("Бажаєте ввести ще дані? (yes/no): ").lower()
        if more_data != 'так':
            break

send_http_request(url, method, data)
