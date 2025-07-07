import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return f"<h1>DB Connected. Time: {result[0]}</h1>"
    except Exception as e:
        return f"<h1>DB Connection Failed</h1><p>{e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

