import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = 'Nxt7RzoXxXkjD1ZZrkSrlx5Bs9sGYZxC3kx2bERI'
secret_key = 'VCLoAhrxbvyrukYChbxfxD6O1ESegeckIgbqeiQf'
server_url = 'https://api.upbit.com/v1/accounts'

# payload = {
#     'access_key': 'Nxt7RzoXxXkjD1ZZrkSrlx5Bs9sGYZxC3kx2bERI',
#     'nonce': str(uuid.uuid4()),
# }

jwt_token = jwt.encode('Nxt7RzoXxXkjD1ZZrkSrlx5Bs9sGYZxC3kx2bERI', 'VCLoAhrxbvyrukYChbxfxD6O1ESegeckIgbqeiQf')
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get("https://api.upbit.com/v1/accounts", headers=headers)

print(res.json())