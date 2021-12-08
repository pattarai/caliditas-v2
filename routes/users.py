import pymysql
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request


@app.route('/scan', methods=['POST'])
def insert_temp():
    # Sample route with a method handlers and a view function
    try:
        _form = request.form
        _deviceId = _form['deviceId']
        _name = _form['name']
        _regno = _form['regno']
        _temp = _form['temp']
        _timestamp = _form['timestamp']
        

        if _deviceId and _name and _regno and _temp and _timestamp and request.method == 'POST':
            # insert record in database
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO student(deviceId,name,regno,timestamp,temp) VALUES('{_deviceId}','{_name}', '{_regno}','{_temp}','{_timestamp}')")
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
