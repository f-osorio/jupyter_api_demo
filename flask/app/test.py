# TODO: Connet to MySQL databse
# Build and populate database with information - possible to do with docker
import json
from flask import Flask, request
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

app.config['SQLALCHEMY_DATABASE_USER'] = 'root'
app.config['SQLALCHEMY_DATABASE_PASSWORD'] = 'root'
app.config['SQLALCHEMY_DATABASE_DB'] = 'metrics'
app.config['SQLALCHEMY_DATABASE_HOST'] = 'db'

mysql.init_app(app)

@app.route('/')
def index():
    print('????')
    return "Hello?"

@app.route('/<table>/<type>/<value>', methods=['GET'])
def simple_get(table, type, value):
    conn = mysql.connect()
    cur = conn.cursor()
    q = "SELECT * FROM bibliometrics;"
    cur.execute(q)
    r = cur.fetchall()
    cur.close()
    conn.close()

    return r

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
