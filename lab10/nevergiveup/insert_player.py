import psycopg2
from config import load_config


def insert_player(username):
    sql = f"""INSERT INTO vendors(vendor_name) 
            VALUES('{username}') RETURNING vendor_id;"""
    
    config = load_config()
    vendor_id = None

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows = cursor.fetchone()
                if rows:
                    vendor_id = rows[0]
                
                connection.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return vendor_id
    

if __name__ == "__main__":
    insert_player(username=input())

