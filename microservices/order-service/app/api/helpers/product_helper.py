import os
import httpx

PRODUCT_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/products/'
url_product = os.environ.get('PRODUCT_SERVICE_HOST_URL') or PRODUCT_SERVICE_HOST_URL

def is_product_id_valid(id: int):
    r = httpx.get(f'{url_product}{id}')
    return True if r.status_code == 200 else False