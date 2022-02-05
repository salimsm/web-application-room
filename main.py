
from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')




@app.route('/login')
def register():
	return render_template('login.html')


@app.route('/register')
def login():
	return render_template('register.html')

app.run()
