import requests

temp = 99.5
url = 'http://caliditas.herokuapp.com/scan'
data = {"rollno": "20IT055", "deviceId": "1", "temp": str(temp)}
file = {'image': open('pattarai.png', 'rb')}
response = requests.post(url, data=data, files=file)