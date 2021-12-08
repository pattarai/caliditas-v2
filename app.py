from flask import Flask
from flask.helpers import send_from_directory
import os

from dotenv import load_dotenv

app = Flask(__name__, static_url_path='', static_folder='.')
app.config['CORS_HEADERS'] = 'Content-Type'

# Load environment variables
load_dotenv()


@app.after_request
def after_request_func(response):
    # CORS section
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
# end CORS section


import error_handles

# Add your API endpoints here
from routes import users
# from routes import cars
# ...


@app.route('/')
def home_page():
    try:
        res = "<h1 style='position: fixed; top: 50%;  left: 50%; transform: translate(-50%, -50%);text-align:center'>FLASK API HOME<p>If you are seeing this page, Good Job. Your Flask app is ready! Add your endpoints in the /routes directory.</p></h1>"
        return res

    except Exception as e:
        print(e)


# Setting Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()
