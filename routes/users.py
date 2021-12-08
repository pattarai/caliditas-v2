import pymysql
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request
from pytz import timezone 
from datetime import datetime

@app.route('/scan')
def insert_temp():
    local_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')
    local_date = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
    try:
        _rollno = request.args.get('rollno')
        _deviceId = request.args.get('deviceId')
        _temp = request.args.get('temp')
        

        if  _rollno  and _deviceId and _temp:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO users(roll_no,date,time,dev_id,temp) VALUES('{_rollno}','{local_date}','{local_time}','{_deviceId}','{_temp}')")
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

@app.route("/get_users")
def get_users():
    local_date = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE date='{local_date}'")
        data = cursor.fetchall()
        print(data)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"users" : str(data)})
    except Exception as e:
        print(e)
        return jsonify({"message" : 'failed in exception'})
