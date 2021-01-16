from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'hiw'

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/login',methods =['GET','POST'])
def login():
    error = None
    if request.method == "Post":
        if request.form['username'] != 'admin' or   request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            return redirect(url_for('home'))
    return render_template('login.html',error = error)

if __name__ == "__main__":
    app.run(debug=True)