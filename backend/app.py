from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions (name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"message": "Name and email are required"}), 400
    
    # Insert data into the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO submissions (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data submitted successfully"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
