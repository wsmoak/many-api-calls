# tasks.py

from celery import Celery

# Create Celery instance
celery = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672', backend=None)
#celery.config_from_object('celeryconfig')

@celery.task
def add(x, y):
    print(f"ADDING {x} and {y}")
    return x + y

@celery.task
def multiply(x, y):
    print(f"MULTIPLYING {x} and {y}")
    return x * y
