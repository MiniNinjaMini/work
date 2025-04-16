import psycopg2
from config import load_config



def get_paginated_users(limit, offset):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_paginated_users(%s, %s);", (limit, offset))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Ошибка при получении данных:", e)

if __name__ == "__main__":
    get_paginated_users(2, 0)  # пример: 3 записи с начала
