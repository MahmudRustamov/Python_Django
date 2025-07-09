from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to RDS PostgreSQL
conn = psycopg2.connect(
    host='mahmud-2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com',
    database='postgres',
    user='postgres',
    password='rustamov'
)

@app.route('/students', methods=['GET'])
def get_students():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
