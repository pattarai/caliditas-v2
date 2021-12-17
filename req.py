import requests

def req(filename):
    url = 'https://api.telegram.org/bot5006954790:AAHuvrjOE1I4_k4C54DrTVzfJRVNZbNATYY/sendPhoto?chat_id=1657430402&caption=Caliditas'
    files = {'media': open('filename', 'rb')}
    return requests.post(url, files=files)

req('pattarai.png')