import pymysql
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request


@app.route('/scan', methods=['POST', 'GET'])
def insert_cars():
    # Sample route with a method handlers and a view function
    try:
        _form = request.form
        _name = _form['name']
        _rollno = _form['rollno']
        _timestamp = _form['timestamp']
        _temp = _form['temp']

        if _name and _rollno and _timestamp and _temp and request.method == 'POST':
            # insert record in database
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO temperature(name,rollno,timestamp,temp) VALUES('{_name}', '{_email}',')")
            conn.commit()
            cursor.close()
            conn.close()
            res = jsonify('success')
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)
