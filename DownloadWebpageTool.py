import requests

url = 'INSERT_URL_HERE'
response = requests.get(url)

with open('webpage.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
