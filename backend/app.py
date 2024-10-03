from flask import Flask, request, jsonify
import pyodbc
import os

app = Flask(__name__)

# SQL Server connection settings (Google Cloud SQL Server)
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.environ.get('SQL_SERVER_HOST')},1433;"
    f"DATABASE={os.environ.get('SQL_SERVER_DB')};"
    f"UID={os.environ.get('SQL_SERVER_USER')};"
    f"PWD={os.environ.get('SQL_SERVER_PASSWORD')};"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='submissions' AND xtype='U')
    CREATE TABLE submissions (name NVARCHAR(50), email NVARCHAR(50))
""")
conn.commit()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"message": "Name and email are required"}), 400

    # Insert data into SQL Server (Google Cloud SQL)
    cursor.execute('INSERT INTO submissions (name, email) VALUES (?, ?)', (name, email))
    conn.commit()

    return jsonify({"message": "Data submitted successfully"})

@app.route('/data', methods=['GET'])
def get_data():
    # Fetch all submissions from SQL Server
    cursor.execute('SELECT name, email FROM submissions')
    rows = cursor.fetchall()

    data = [{"name": row[0], "email": row[1]} for row in rows]

    return jsonify(data)

@app.route('/config', methods=['GET'])
def get_config():
    return jsonify({
        "backend_url": os.environ.get('BACKEND_URL')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
