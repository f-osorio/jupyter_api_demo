# TODO: Connet to MySQL databse
# Build and populate database with information - possible to do with docker
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'development')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


"""
from flask import Flask
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
"""