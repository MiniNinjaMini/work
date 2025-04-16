import psycopg2
from config import load_config
config = load_config()

def insert_or_update(name, second_name, last_name, phone):
    config = load_config()
    query = "CALL insert_or_update_user(%s, %s, %s, %s)"
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, second_name, last_name, phone))

if __name__ == "__main__":
    insert_or_update("Miron", "Miron", "Miron" ,"88008008080")