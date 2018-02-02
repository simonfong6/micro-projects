import requests

url = 'http://localhost:8000/data'
payload = {'some': 'data'}

r = requests.post(url, json=payload)
