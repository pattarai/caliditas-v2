import requests

def request(filename):
    url = ''
    files = {'media': open('filename', 'rb')}
    return requests.post(url, files=files)

request('pattarai.png')