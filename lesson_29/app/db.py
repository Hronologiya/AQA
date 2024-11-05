import psycopg2

DATABASE_URL = "******://******:******@******:5432/******"

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            value VARCHAR(50)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_data(name, value):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test_table (name, value) VALUES (%s, %s);", (name, value))
    conn.commit()
    cursor.close()
    conn.close()

def get_data():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def update_data(record_id, new_name, new_value):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("UPDATE test_table SET name = %s, value = %s WHERE id = %s;", (new_name, new_value, record_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_data(record_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM test_table WHERE id = %s;", (record_id,))
    conn.commit()
    cursor.close()
    conn.close()