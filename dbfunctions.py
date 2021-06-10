import sqlite3

def auth_execute(sql_query):
    with sqlite3.connect("auth.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result

def create_user(name, email, password):
    sql_query = f''' INSERT INTO auth(name, email, password) VALUES("{name}", "{email}", "{password}")'''

    try:
        auth_execute(sql_query)
        return "Sucess"

    except:
        return "Error occured"

def get_all_users():
    sql_query = f''' SELECT * FROM auth '''
    result = auth_execute(sql_query).fetchall()
    print(result)
