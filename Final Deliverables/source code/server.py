from flask import Flask, render_template,request,redirect,url_for,session,flash
import ibm_db
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests

app = Flask(__name__)
app.secret_key='a'
try:
   conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=kcf08623;PWD=8himlHEH6rDcSV2i",'','')
except:
    print("Unable to connect: ",ibm_db.conn_error())

@app.route('/')
def home():
  return render_template('home.html')

@app.route("/register",methods=['GET','POST'])
def register():
    error = None 
    if request.method=='POST':
           username=request.form['username']
           email=request.form['email']
           phonenumber=request.form['phonenumber']
           password=request.form['password']
           sql="SELECT * FROM user WHERE phonenumber=?"
           prep_stmt=ibm_db.prepare(conn,sql)
           ibm_db.bind_param(prep_stmt,1,phonenumber)
           ibm_db.execute(prep_stmt)
           account=ibm_db.fetch_assoc(prep_stmt)
           print(account)
           

# SENDGRID_API_KEY='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'
# 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
           message = Mail(
               from_email='skilljob007@gmail.com',
               to_emails=email,
               subject='Hello there! Welcome to Skill And Job Recommender',
               html_content='<strong>SJR warmly welcomes YOU!!!,Thanks for taking the time to apply for our position.we appreciate your interest in SJR.COM</strong</strong>')
           try:
              sg = SendGridAPIClient('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')
              response = sg.send(message)
              print(response.status_code)
              print(response.body)
              print(response.headers)

           except Exception as e:
             print(str(e))
             
           if account:
               error="Account already exists! Log in to continue !"
           else:
               insert_sql="INSERT INTO user values(?,?,?,?)"
               prep_stmt=ibm_db.prepare(conn,insert_sql)
               ibm_db.bind_param(prep_stmt,1,email)
               ibm_db.bind_param(prep_stmt,2,username)
               ibm_db.bind_param(prep_stmt,3,phonenumber)
               ibm_db.bind_param(prep_stmt,4,password)
               ibm_db.execute(prep_stmt)
               flash(" Registration successfull. Log in to continue !")
    else:
        pass
    return render_template('register.html',error=error)

@app.route('/signup',methods=['GET','POST'])
def signup():
    error = None
    if request.method=='POST':
        username=request.form['email']
        password=request.form['password']
        sql="SELECT * FROM user WHERE username=? AND password=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['Loggedin']=True
            session['id']=account['EMAIL']
            session["email"]=account["EMAIL"]
            flash("Logged in successfully!")
            return render_template('applyjob.html')
        else:
            error="Incorrect username / password"
            return render_template('signup.html',error=error)
    return render_template('signup.html',error=error)

@app.route('/applyjob')
def applyjob():
    return render_template('applyjob.html')

@app.route('/skill')
def skill():
  return render_template('skill.html')

@app.route('/aboutus')
def aboutus():
  return render_template('aboutus.html')
  
if __name__=='__main__':
   app.run(host='0.0.0.0',port=5000,debug=True)