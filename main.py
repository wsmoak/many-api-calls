# main.py

from tasks import add, multiply
import time

time.sleep(20)

# Run Celery tasks asynchronously
result_add = add.delay(4, 5)  # Add numbers 4 and 5
result_multiply = multiply.delay(3, 7)  # Multiply numbers 3 and 7

