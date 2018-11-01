from flask import Flask, request
import json
import datetime
import pymysql

app = Flask(__name__)

# return json: [{"key": "value"}]
def get_rows_as_dicts(cursor):
    columns = [d[0] for d in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# forgot what purpose le (for date)
date_handler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, (datetime.datetime, datetime.date))
    else None
)

#Create
@app.route("/create/<type>", methods = ['POST'])
def create(type):
	cnx = pymysql.connect(user='root', password='123456', database='cocurriculum', host='127.0.0.1', port=3306)
	cursor = cnx.cursor()

	data = request.form.to_dict()
	print("post data: ")
	print(data)

	if type == "newsfeeds":
		t = (data['ownerId'], data["name"], data["category"], data["desc"], data["dateCreate"], data["type"])
		query = ("INSERT INTO SocietyNewsfeed VALUES (null, %s, %s, %s, %s, %s, %s)")
		
	cursor.execute(query, t)
	insertedId1 = cursor.lastrowid
	print(insertedId1)
	
	cnx.commit()

	cursor.close()
	cnx.close()

	return str(insertedId1)

# Retrieve
@app.route("/get/<type>/<int:id>", methods=['GET'])
def getOne(type, id):
	cnx = pymysql.connect(user='root', password='123456', database='cocurriculum', host='127.0.0.1', port=3306)
	cursor = cnx.cursor()

	print("type: ")
	print(type)
	
	if(type == "society"):
		query = ("SELECT * FROM Society WHERE societyId=%d" % id)

	cursor.execute(query)
	result = get_rows_as_dicts(cursor)

	cursor.close()
	cnx.close()

	print("userEvents/eventCrews selected: ")
	print(json.dumps(result, default = date_handler))

	return json.dumps(result, default = date_handler)

# Update
@app.route("/update/<type>/<int:id>", methods = ['POST'])
def update(type, id):
	cnx = pymysql.connect(user='root', password='123456', database='cocurriculum', host='127.0.0.1', port=3306)
	cursor = cnx.cursor()

	data = request.form.to_dict()
	print("post data: ")
	print(data)

	query = ("UPDATE Event SET name='{0}', category='{1}', eventDateTime='{2}', description='{3}', venue='{4}', fee='{5}', ssPoint='{6}', chairperson='{7}', contact='{8}' WHERE eventId='{9}'".format(data["name"], 
		data["category"], data["startDate"], data["desc"], data["venue"], data["fee"], data["ssPoint"], data["chairperson"], data["contact"], id))
	
	cursor.execute(query)
	
	cnx.commit()

	cursor.close()
	cnx.close()

	return "true"

# Delete
@app.route("/delete/<type>/<int:id>", methods = ['DELETE'])
def delete(type, id):
	cnx = pymysql.connect(user='root', password='123456', database='cocurriculum', host='127.0.0.1', port=3306)
	cursor = cnx.cursor()

	if(type == "event"):
		query = ("DELETE FROM Event where id=%d" % id)
	elif(type == "society"):
		query = ("DELETE FROM Society where id=%d" % id)
	
	cursor.execute(query)
	
	cnx.commit()

	cursor.close()
	cnx.close()

	return "true"

