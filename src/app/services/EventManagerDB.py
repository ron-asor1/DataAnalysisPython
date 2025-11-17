import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
from datetime import datetime

unix_ts = event.timestamp   # e.g. 1763381685.198941
dt = datetime.fromtimestamp(unix_ts)

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()

class EventManagerDB:
    def inset_event(self, event):
        sql = """
        INSERT INTO events (event_id, event_type, timestamp, user_id, session_id, product_id, product_name, product_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            event.event_id,
            event.event_type,
            event.timestamp,
            event.user_id,
            event.session_id,
            event.product_id,
            event.product_name,
            event.product_price
        ))
        conn.commit()