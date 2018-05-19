# coding:utf8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import   os
import pymysql
from flask_redis import FlaskRedis


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/moive2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] ='a4c32d961cae4a5ead659b9faeba42e1'
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["FACE_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/user/")
#app.config["REDIS_URL"] = "redis://:password@127.0.0.1:6379/0"
app.config["REDIS_URL"] = "redis://:@127.0.0.1:6379/0"

app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 404页面定制
@app.errorhandler(404)
def page_not_fond(error):
	return render_template('home/404.html'), 404
