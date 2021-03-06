from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging


# app init and setup
app = Flask(__name__)
app.config.from_object(Config)

# database init and setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# LoginManager redirect users to login page until they log-in
# the 'login' is view function name in 'routes.py' to handle it
login = LoginManager(app)
login.login_view = 'login'

# logger
logging.basicConfig(filename='requests.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


from app import routes, models