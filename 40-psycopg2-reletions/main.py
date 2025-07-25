import psycopg2
from psycopg2.extras import DictCursor

db_config = {
    'host': 'localhost',
    'port': '5432',
    'user': 'lesson3',
    'password': 'lesson3',
    'database': 'lesson3'
}

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor(cursor_factory=DictCursor)

    query = "select * from staff"
    cursor.execute(query)
    result = cursor.fetchall()

    for employee in result:
        print(dict(employee))
    conn.close()

except Exception as error:
    print(error)