import sqlite3

sql_query = """
    CREATE TABLE IF NOT EXISTS auth(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    );
"""

def execute_query(sql_query):
    with sqlite3.connect("auth.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result

if __name__ == '__main__':
    execute_query(sql_query)