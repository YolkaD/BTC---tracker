import requests
import json


def make_request(start, end):
    print(f'Запрос к API: c {start} по {end}')
    responce = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?',
                            params={'start': start, 'end': end})
    btc = {}
    resp = json.loads(responce.content)
    for k, v in resp["bpi"].items():
        btc[k] = v
    return btc
