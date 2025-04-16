import psycopg2
from config import load_config

def search_by_pattern(pattern):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_phone_book(%s);", (pattern,))
                results = cur.fetchall()
                for row in results:
                    print(row)
                return results
    except Exception as e:
        print("Ошибка при поиске:", e)

# Пример использования
if __name__ == "__main__":
    search_by_pattern("john")
