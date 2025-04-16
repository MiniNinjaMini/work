import psycopg2
from config import load_config

config = load_config()
conn = psycopg2.connect(
    **config
)
cur = conn.cursor()

#1

cur.execute(r"""
CREATE OR REPLACE FUNCTION search_phone_book(pattern TEXT)
RETURNS TABLE (
    person_id INT,
    name TEXT,
    second_name TEXT,
    last_name TEXT,
    phone_number TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.person_id, pb.name::TEXT, pb.second_name::TEXT, pb.last_name::TEXT, pb.phone_number::TEXT
    FROM phone_book pb
    WHERE pb.name ILIKE '%' || pattern || '%'
       OR pb.second_name ILIKE '%' || pattern || '%'
       OR pb.last_name ILIKE '%' || pattern || '%'
       OR pb.phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

""")




#2

cur.execute(r"""
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    in_name TEXT,
    in_second_name TEXT,
    in_last_name TEXT,
    in_phone TEXT
)
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phone_book
        WHERE name = in_name AND second_name = in_second_name AND last_name = in_last_name
    ) THEN
        UPDATE phone_book
        SET phone_number = in_phone
        WHERE name = in_name AND second_name = in_second_name AND last_name = in_last_name;
    ELSE
        INSERT INTO phone_book(name, second_name, last_name, phone_number)
        VALUES (in_name, in_second_name, in_last_name, in_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

""")



cur.execute("""
    DROP PROCEDURE IF EXISTS insert_many_users(TEXT[], TEXT[], TEXT[], TEXT[]);
""")

#3
cur.execute(r"""
DROP FUNCTION IF EXISTS insert_many_users_fn(TEXT[], TEXT[], TEXT[], TEXT[]);

CREATE OR REPLACE FUNCTION insert_many_users_fn(
    names TEXT[],
    second_names TEXT[],
    last_names TEXT[],
    phones TEXT[]
) RETURNS TEXT AS $$
DECLARE
    invalid_entries TEXT := '';
    i INTEGER;
BEGIN
    FOR i IN 1 .. array_length(names, 1) LOOP
        -- Пример проверки: номер должен начинаться с "870" и содержать ровно 11 символов (870 + 8 цифр)
        IF phones[i] ~ '^870\d{8}$' THEN
            INSERT INTO phone_book(name, second_name, last_name, phone_number)
            VALUES (names[i], second_names[i], last_names[i], phones[i]);
        ELSE
            invalid_entries := invalid_entries ||
               names[i] || ' ' || second_names[i] || ' ' || last_names[i] ||
               ': ' || phones[i] || E'\n';
        END IF;
    END LOOP;
    RETURN invalid_entries;
END;
$$ LANGUAGE plpgsql;

""")


#4

cur.execute(r"""
CREATE OR REPLACE FUNCTION get_paginated_users(lim INT, off INT)
RETURNS TABLE (
    person_id INT,
    name VARCHAR,
    second_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phone_book
    ORDER BY person_id
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;


""")



# 5
cur.execute(r"""
DROP PROCEDURE IF EXISTS delete_single_user_by_name(TEXT);

CREATE OR REPLACE PROCEDURE delete_single_user_by_name(
    del_name TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    WITH cte AS (
        SELECT person_id
        FROM phone_book
        WHERE name = del_name
        ORDER BY person_id  -- можем выбрать по любому критерию, здесь — по порядку добавления
        LIMIT 1
    )
    DELETE FROM phone_book
    WHERE person_id IN (SELECT person_id FROM cte);
END;
$$;


""")









conn.commit()
cur.close()
conn.close()
