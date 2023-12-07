import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from wtforms import validators
from flask_mail import Mail

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'bb2252a3b6b33d49406470cd5fbe80a1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'azainab390@gmail.com'
app.config['MAIL_PASSWORD'] = 'rtey qcoa ufle fgos'
mail = Mail(app)
app.app_context().push()

from techblog import routes