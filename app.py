from flask import Flask, render_template, request, jsonify
from dbfunctions import *

app = Flask(__name__)


@app.route("/")
def login():
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        result = create_user(name, email, password)

        return render_template('register.html', result=result )

    return render_template('register.html')

@app.route("/home")
def home():
    return render_template('home.html')

# @app.route("/login", methods=['POST'])
# def login():
#     email=request.form.get('email')
#     password=request.form.get('password')

#     cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE {} AND `password` LIKE {}"""
#                    .format(email, password))
#     users = cursor.fetchall()
#     return users

if __name__ == "__main__":
    app.run(debug=True)
