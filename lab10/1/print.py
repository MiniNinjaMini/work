import psycopg2
from config import load_config
config = load_config()

def print_whole_phone_book():
    
    query = "SELECT * FROM phone_book ORDER BY person_id"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                print("Phone Book:")
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")

print_whole_phone_book()
