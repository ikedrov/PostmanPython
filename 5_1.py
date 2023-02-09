import requests

url = 'https://api.chucknorris.io/jokes/random'
result = requests.get(url)
print(f'Статус код: {str(result.status_code)}')
assert result.status_code == 200
print('Success')
result.encoding = 'utf-8'
print(result.text)
