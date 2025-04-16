import psycopg2
from config import load_config

def insert_many_users(names, second_names, last_names, phones):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                query = "SELECT insert_many_users_fn(%s, %s, %s, %s);"
                cur.execute(query, (names, second_names, last_names, phones))
                # Функция вернет одну строку с невалидными записями
                result = cur.fetchone()
                invalid_entries = result[0] if result else ''
                if invalid_entries and invalid_entries.strip():
                    print("Некорректные записи:")
                    print(invalid_entries)
                else:
                    print("Все данные успешно добавлены.")
    except Exception as e:
        print("Ошибка при вставке данных:", e)

if __name__ == "__main__":
    # Пример данных:
    names = ['John', 'Alice', 'Bob']
    second_names = ['Doe', 'Liddell', 'Marley']
    last_names = ['Smith', 'Wonderland', 'Brown']
    phones = ['87011234567', 'invalid_phone', '87029876543']  # Вторая запись не пройдет проверку

    insert_many_users(names, second_names, last_names, phones)
