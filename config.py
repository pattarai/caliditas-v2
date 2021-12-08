from app import app
import os

# MySQL imports
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# Rows from cursors will always be of type dict || cursorclass=DictCursor
mysql = MySQL(cursorclass=DictCursor)

# MySQL configurations and Init
app.config['MYSQL_DATABASE_USER'] = os.environ['DB_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['DB_PASS']
app.config['MYSQL_DATABASE_DB'] = os.environ['DB_NAME']
app.config['MYSQL_DATABASE_HOST'] = os.environ['DB_HOST']
app.config['MYSQL_DATABASE_PORT'] = int(os.environ['DB_PORT'])
mysql.init_app(app)
