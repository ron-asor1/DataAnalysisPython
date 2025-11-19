import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()

#local PostgreSQL connection
# conn = psycopg2.connect(
#     dbname=os.getenv("DB_NAME"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT")
# )

#snowflake connection
# Create a connection object using your Snowflake credentials and config
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cursor = conn.cursor()

cursor.execute("SELECT CURRENT_VERSION()")
version = cursor.fetchone()
print("Snowflake version:", version[0])
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
