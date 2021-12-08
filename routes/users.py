import pymysql
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request


@app.route('/scan', methods=['POST','GET'])
def insert_temp():
    try:
        _fname = request.args.get('fname')
        _lname = request.args.get('lname')
        _regno = request.args.get('regno')
        _deviceId = request.args.get('deviceId')
        _temp = request.args.get('temp')
        

        if  _fname and _lname and _regno  and _deviceId and _temp and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO users(f_name,l_name,reg_num,dev_id,temp) VALUES('{_fname}','{_lname}','{_regno}','{_deviceId}','{_temp}')")
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