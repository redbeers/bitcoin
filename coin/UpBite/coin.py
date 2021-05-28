import os
import requests
# import pyupbit
import time
import datetime
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import telegram
import requests


#조회
def search_all():
    #종목조회
    url = "https://api.upbit.com/v1/candles/days"
    querystring = { "market":   "KRW-BTT", "count" :   "1"}
    response = requests.request("GET", url, params=querystring)
    #시가, 현재가 불러오기
    open_price = response.json()[0]['opening_price']
    now_price = response.json()[0]['trade_price']

    return open_price, now_price


def search_now_price():
    url = "https://api.upbit.com/v1/candles/days"
    querystring = { "market":   "KRW-BTT", "count" :   "1"}
    response = requests.request("GET", url, params=querystring)
    now_price = response.json()[0]['trade_price']
    search_now = {'open_price':open_price, 'now_price':now_price}
    return now_price


#조건
def compare(open_price, now_price):
    return open_price * 0.95 > now_price


#주문
def buy():
    server_url = 'https://api.upbit.com'
    query = {
    'market': 'KRW-BTT',
    'side': 'bid',
    'volume': '1200',
    'price': now_price,
    'ord_type': 'limit',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    print(res.json())

#텔레그램
def telegram_sms(time_now):
    telgm_token = '1799768876:AAE-r9m6KcI4TCmBtG1zgXWArF_44mZSQ_U'
    bot = telegram.Bot(token = telgm_token)
    bot.send_message(chat_id = '1698877958', text=time_now)

if __name__ == '__main__':
    access_key = 'aiRwRxSCAV0ILVkjIxRSLFQk8vxlyphFcKAG2MgX'
    secret_key = 'yy1z0AmgZUmw8OO57TTKvFuP8tTqKZsMMiHshhJ7'

    open_price, now_price = search_all()

    print(datetime.datetime.today())
    print('프로그램 시작')
    print(f'시작가 : {open_price}')
    print(f'현재가 : {now_price}')
    print('----------')

    while 1:
        print(datetime.datetime.today())
        now_price = search_now_price()
        if compare(open_price, now_price):
            print(f'시작가 : {open_price}')
            print(f'현재가 : {now_price}')
            time_now = (f'현재가 : {now_price}')
            open_price = now_price
            buy()
            telegram_sms(time_now)
            print("구매 후 시작가 변경", open_price)
        print(f'시작가 : {open_price}')
        print(f'현재가 : {now_price}')
        print('----------')
        time.sleep(60)
