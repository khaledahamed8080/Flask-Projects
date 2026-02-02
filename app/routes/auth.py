from flask import Blueprint, request ,render_template, session, url_for, flash, redirect 
from app.models import Task

auth_bp=Blueprint('auth',__name__)


USER_CREDENTIALS={
    'username':'admin',
    'password':'1234'
}

@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')

        if username==USER_CREDENTIALS['username'] and password==USER_CREDENTIALS['password']:
            session['user']=username
            flash('LOGIN SUCCESSFUL','success')
            tasks=Task.query.all()
            return render_template('tasks.html',tasks=tasks)
            
        else:
            flash('INVALID CREDENTIALS, CHECK YOUR USERNAME AND PASSWORD','danger')

    return render_template("login.html")

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('LOGOUT SUCCESSFUL','info')
    return redirect(url_for('auth.login'))