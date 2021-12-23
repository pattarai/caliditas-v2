from importlib.metadata import files
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
        #_imageBytes = request.form['imageBytes']

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
                #file = request.files['image']
                #file.save('buffer.jpg')
                #image = {"photo": open("./buffer.jpg", "rb")}
                bot_token = os.environ['BOT_TOKEN']
                chat_id = os.environ['CHAT_ID']
                imgFile = open("buffer.jpg", "wb+")
                imageB = "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"
                imgFile.write(imageB)
                imgFile.close()
                image = {"photo": open("./buffer.jpg", "rb")}
                response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Roll%20No:%20{_rollno}%0D%0ADevice%20ID:%20{_deviceId}%0D%0ATemperature:%20{_temp}", files=image)
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
