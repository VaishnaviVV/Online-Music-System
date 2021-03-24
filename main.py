from flask import Flask, render_template, Response,redirect, request
# from camera import VideoCamera
import os
from gevent.pywsgi import WSGIServer
import mysql.connector
app = Flask(__name__)
conn=mysql.connector.connect(host="remotemysql.com",user="ll32gwnKpe",password="3TMmSIiOZX",database="ll32gwnKpe")
cursor=conn.cursor()
@app.route('/home')
def home():
    return render_template('welcome.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=['GET', 'POST'])
def login():
    return render_template('contact.html')
@app.route('/playlist')
def playlist():
    return render_template('playlist.html')
@app.route('/Albums')
def albums():
    return render_template('album1.html')
@app.route('/login_validation',methods=['POST','GET'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `login` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    login=cursor.fetchall()
   
    
    if len(login)>0:
        return render_template('playlist.html')
    else:
        return render_template('signup.html')

@app.route('/add_user',methods=['POST','GET'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cpassword=request.form.get('ucpassword')
    cursor.execute("""INSERT INTO `sign` (`uname`,`uemail`,`upassword`,`ucpassword`) VALUES 
    ('{}','{}','{}','{}')""".format(name,email,password,cpassword))
    conn.commit()
    return "user registered successfully"

@app.route('/english',methods=['POST','GET'])
def english():
    return render_template('english.html')

@app.route('/kpop',methods=['POST','GET'])
def kpop():
    return render_template('kpop.html')

@app.route('/regional',methods=['POST','GET'])
def regional():
    return render_template('regional.html')



@app.route('/rock',methods=['POST','GET'])
def rock():
    return render_template('rock.html')

@app.route('/melody',methods=['POST','GET'])
def melody():
    return render_template('melody.html')

@app.route('/rap',methods=['POST','GET'])
def rap():
    return render_template('rap.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
    #app.run(host='0.0.0.0', port=8000, debug=True)
