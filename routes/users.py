import pymysql
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request


@app.route('/scan')
def insert_temp():
    try:
        _rollno = request.args.get('rollno')
        _deviceId = request.args.get('deviceId')
        _temp = request.args.get('temp')
        

        if  _rollno  and _deviceId and _temp and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO users(roll_no,dev_id,temp) VALUES('{_rollno}','{_deviceId}','{_temp}')")
            conn.commit()
            cursor.close()
            conn.close()
            res = jsonify({"message" : 'success'})
            res.status_code = 200
            return res
        else:
            return jsonify({"message" : 'failed'})

    except Exception as e:
        print(e)
        return jsonify({"message" : 'failed in exception'})