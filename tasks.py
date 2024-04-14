# tasks.py

from celery import Celery
import requests
import base64
import os

celery = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672', backend=None)
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

def encode_api_credentials(api_key, password):
    api_key_password = f"{api_key}:{password}"
    encoded_credentials = base64.b64encode(api_key_password.encode()).decode()
    authorization_header = f"Basic {encoded_credentials}"
    return authorization_header

headers = {
    'Authorization': encode_api_credentials(api_key, 'x'),
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

@celery.task(bind=True, max_retries=3, default_retry_delay=5)
def process_row(self, row_dict):
    print(f"...PROCESSING ROW {row_dict}")
    component_id = row_dict['item_id']
    subscription_id = row_dict['subscription_id']
    qty = row_dict['quantity']
    payload_type = row_dict['payload_type']
    memo = row_dict['memo']

    url = f"{base_url}/subscriptions/{subscription_id}/components/{component_id}/{payload_type}s"

    payload = {
        payload_type: {
            'quantity': qty,
            'memo': memo
        }
    }

    try:
        response = requests.request('POST', url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        raise self.retry(exc=exc)


def health_check():
    print("Checking RabbitMQ Status")
    try:
        response = requests.request('GET', 'http://rabbitmq:15672')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False
