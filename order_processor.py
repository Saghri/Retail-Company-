import pandas as pd
import logging

def process_order(file_path):
    try:
        orders = pd.read_csv(file_path)
        logging.info(f"Successfully read orders from {file_path}")
        # Process each order here (e.g., validate, compute, etc.)
        for index, order in orders.iterrows():
            logging.info(f"Processing order {order['order_id']}")
            # Process logic for individual order
    except Exception as e:
        logging.error(f"Failed to process orders from {file_path}: {e}")
