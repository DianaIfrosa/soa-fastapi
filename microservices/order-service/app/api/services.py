import os
import httpx

USER_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/users/'
url_user = os.environ.get('USER_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL

def is_user_present(id: int):
    r = httpx.get(f'{url_user}{id}')
    return True if r.status_code == 200 else False

#todo: separate in dif files

PRODUCT_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/products/'
url_product = os.environ.get('PRODUCT_SERVICE_HOST_URL') or PRODUCT_SERVICE_HOST_URL

def is_product_present(id: int):
    r = httpx.get(f'{url_product}{id}')
    return True if r.status_code == 200 else False