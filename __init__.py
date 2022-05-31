from flask  import Flask, redirect, url_for
from flask.templating import render_template
from flask import request
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
# 

app = Flask(__name__)
#@app.route("/name")

conn = sqlite3.connect('database.db')
print("opened db")

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("table created")

conn.close()

@app.route("/home")
def home():
    
    return render_template("index.html", title='home')

@app.route("/database")
def database():

    return ("You're at database")

if __name__ == "__main__":
    app.debug = True
    app.run()
   