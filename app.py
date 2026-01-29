from flask import Flask, render_template , request, redirect, url_for, session


app=Flask(__name__)

@app.route("/")
def home():
   return render_template("login.html")

@app.route("/about")
def info():
   return render_template("info.html")