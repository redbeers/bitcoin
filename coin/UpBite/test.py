import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = os.environ['Nxt7RzoXxXkjD1ZZrkSrlx5Bs9sGYZxC3kx2bERI']
secret_key = os.environ['qpdOHHx20MoRof6Rs0MoxTaNDzxcRUPACkMKdwMD']
server_url = os.environ['https://api.upbit.com/v1/order']

query = {
    'uuid': '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
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

res = requests.get(server_url + "/v1/order", params=query, headers=headers)

print(res.json())