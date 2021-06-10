from flask import Flask, render_template, request
import mysql.connector

App = Flask(__name__)

conn = mysql.connector.connect(host="remotemysql.com", username="fYhNVS5Cd0", password="cjNOO4ypPt", database=" fYhNVS5Cd0")
cursor=conn.cursor()

@App.route("/")
def login():
    return render_template('login.html')

@App.route('/register')
def about():
    return render_template('register.html')

@App.route("/home")
def home():
    return render_template('home.html')

@App.route("/login_validation", methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE {} AND `password` LIKE {}"""
                   .format(email, password))
    users = cursor.fetchall()
    return users

if __name__ == "__main__":
    App.run(debug=True)
