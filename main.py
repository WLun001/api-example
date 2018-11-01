from flask import Flask
from flask import jsonify
import json
import mysql.connector
import random

app = Flask(__name__)

def selectAllItem():
    db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="testuser",
    passwd="123",
    database="testdb"
)
    cursor = db.cursor()
    cursor.execute("select itemName from item")
    result = get_rows_as_dicts(cursor)
    db.close()
    return result

# return json: [{"key": "value"}]
def get_rows_as_dicts(cursor):
    # cursor description is [('itemName', 253, None, None, None, None, 1, 0)]
    # d[0] is itemName
    columns = [d[0] for d in cursor.description]
    # cursor.fetchall() will return
    # [('fish',), ('shark',)]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_random_num')
def getUser():
    arr = random.randint(0,100)
    return jsonify(num=arr)

@app.route('/get_all_item')
def getAllItem():
    return jsonify(selectAllItem())

@app.route('/get_rand_item')
def getRandItem():
    rand = random.randint(0,10)
    items = selectAllItem()
    return jsonify(items[rand])


if __name__ == '__main__':
    app.run(host= '0.0.0.0')