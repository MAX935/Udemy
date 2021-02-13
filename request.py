import requests

url = "https://yandex.ru"
responce = requests.get(url)
responce.status_code
x = responce.text
