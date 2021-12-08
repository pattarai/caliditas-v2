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
        
        _fname = _form['fname']
        _lname = _form['lname']
        _regno = _form['regno']
        _timestamp = _form['timestamp']
        _deviceId = _form['deviceId']
        _temp = _form['temp']
        

        if  _fname and _lname and _regno and _timestamp and _deviceId and _temp and request.method == 'POST':
            # insert record in database
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO users(f_name,l_name,reg_no,timestamp,dev_id,temp) VALUES('{_fname}', '{_lname}','{_regno}','{_timestamp}','{_deviceId}','{_temp}')")
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
