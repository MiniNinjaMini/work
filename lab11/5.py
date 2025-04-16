import psycopg2
from config import load_config

def delete_single_user_by_name(del_name):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Вызываем процедуру через оператор CALL
                cur.execute("CALL delete_single_user_by_name(%s);", (del_name,))
            # Фиксируем изменения
            conn.commit()
            print(f"Удалена одна запись с именем: {del_name}")
    except Exception as e:
        print("Ошибка при удалении записи:", e)

if __name__ == "__main__":
    # Пример вызова – если в таблице несколько записей с именем "John", удалится только одна из них
    delete_single_user_by_name("John")
