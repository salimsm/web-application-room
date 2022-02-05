
from flask import Flask,render_template,request
from flask_mysqldb import MySQL





app=Flask(__name__)

#database setting for mysql
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='room_app'

mysql=MySQL(app)

@app.route('/')
def index():
	return render_template('index.html')



# to view login page
@app.route('/login')
def register():
	return render_template('login.html')

# to view register page
@app.route('/register')
def login():
	return render_template('register.html')

@app.route('/doRegister',methods=['POST'])
def doRegister():
	firstname=request.form['fname']
	lastname=request.form['lname']
	address=request.form['address']
	contactnumber=request.form['cnumber']
	email=request.form['email']
	password=request.form['password']
	
	cursor=mysql.connection.cursor()
	cursor.execute(''' insert into users values(null,%s,%s,%s,%s,%s,%s)''',(firstname,lastname,address,contactnumber,email,password))
	mysql.connection.commit()
	cursor.close()
	return render_template('login.html',result="sucessfully registerd, please login to continue")
	
app.run()
