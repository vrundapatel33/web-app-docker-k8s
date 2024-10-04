import os
import psycopg2  # For PostgreSQL
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection details
DB_NAME = "mydb"
DB_USER = "vrunda"
DB_PASS = "Server@123"
DB_HOST = "34.121.195.226"  # or "your_instance_connection_name" if using Cloud SQL

# Establish the database connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST
)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    value1 = data.get('value1')
    value2 = data.get('value2')

    if value1 and value2:
        # Insert data into the database
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)", (value1, value2))
            conn.commit()
        return jsonify({"message": "Data submitted successfully!"}), 200
    else:
        return jsonify({"error": "Missing data"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
