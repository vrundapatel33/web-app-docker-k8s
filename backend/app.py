import os
import psycopg2  # For PostgreSQL
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS
# from google.cloud import pubsub_v1  # Import the Pub/Sub client


load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

CORS(app)

# Database connection details
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


# Establish the database connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    )


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = "vp33-400500"
topic_id = "ICA3"
# publisher = pubsub_v1.PublisherClient()
# topic_path = publisher.topic_path(project_id, topic_id)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    value1 = data.get('value1')
    value2 = data.get('value2')

    if value1 and value2:
        # Insert data into the database
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO data (value1, value2) VALUES (%s, %s)", (value1, value2))
            conn.commit()
        return jsonify({"message": "Data submitted successfully!"}), 200
    else:
        return jsonify({"error": "Missing data"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

