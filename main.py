# main.py

from tasks import process_row, health_check
import pandas as pd
import time

def process_rows():
    activity_df = pd.read_csv('data/activity.csv')

    for _, row in activity_df.iterrows():
        row_dict = row.to_dict()
        print(f"...SENDING row {row_dict}")
        process_row.delay(row_dict)

if __name__ == "__main__":
    while not health_check():
        print("RabbitMQ is not available yet. Retrying in 5 seconds...")
        time.sleep(5)

    process_rows()
