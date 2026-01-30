
from flask import Flask, render_template , request, redirect, url_for, session, flash


app=Flask(__name__)
app.secret_key="my_secret_key"

@app.route("/",methods=["GET","POST"])
def form():
     if request.method=="POST":
          name=request.form.get("name")
          if not name:
               flash("Name cannot be empty")
               return redirect(url_for("form"))
          flash(f"Thank you {name}, your feedback is valuable to us")          
          return redirect(url_for("thankyou"))
     return render_template("form.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
