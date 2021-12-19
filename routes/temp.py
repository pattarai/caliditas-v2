import pymysql
import requests
import os
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request
from pytz import timezone
from datetime import datetime


@app.route('/scan', methods=["POST"])
def insert_temp():
    local_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')
    local_date = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
    try:
        _rollno = request.form['rollno']
        _deviceId = request.form['deviceId']
        _temp = request.form['temp']

        if _rollno and _deviceId and _temp:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO users(roll_no,date,time,dev_id,temp) VALUES('{_rollno}','{local_date}','{local_time}','{_deviceId}','{_temp}')")
            conn.commit()
            cursor.close()
            conn.close()
            try:
                # Send user data to management through Telegram
                file = request.files['image']
                file.save('buffer.jpg')
                image = {"photo": open("./buffer.jpg", "rb")}
                bot_token = os.environ['BOT_TOKEN']
                chat_id = os.environ['CHAT_ID']
                response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={chat_id}&caption=Roll%20No:%20{_rollno}%0D%0ADevice%20ID:%20{_deviceId}%0D%0ATemperature:%20{_temp}", files=image)
            except Exception as e:
                print("Data not sent")

            res = jsonify({"message": 'success'})
            res.status_code = 200
            return res
        else:
            return jsonify({"message": 'failed'})

    except Exception as e:
        print(e)
        return jsonify({"message": 'failed in exception'})


@app.route("/ledger")
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
        return jsonify({"users": data})
    except Exception as e:
        print(e)
        return jsonify({"message": 'failed in exception'})
