#!/usr/bin/env python
import requests
import Access
TOKEN = Access.TOKEN
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

playload={
    'chat_id': 333003124,
    'text': 'test',
    'reply_to_message_id': 309
}
#r = requests.get(f'{MAIN_URL}/getUpdates')
r = requests.get(f'{MAIN_URL}/offset')
r = requests.get(f'{MAIN_URL}/sendMessage', data = playload)
r = requests.get(f'{MAIN_URL}/getUpdates', data = playload)

print(r.json())