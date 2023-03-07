from chabella import app
from flask import render_template,redirect,request,session,flash
from chabella.models.user import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/adminlog')
def adminlog():
    return render_template('admin_login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/adminlog')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/adminlog')
    session['idsession'] = user.id
    return redirect('/admin')

@app.route('/admin')
def index():
    if 'idsession' not in session:
        return redirect('/logout')
    data ={
        'id': session['idsession']
    }
    return render_template("admin_index.html",user=User.get_id(data))

@app.route('/adminreg')
def adminregister():
    return render_template('admin_register.html')

@app.route('/admin/new', methods=['POST'])
def adduser():
    if not User.validate_register(request.form):
        return redirect('/adminreg')
    data={
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id =User.save_user(data)
    session['idsession']=id
    return redirect('/admin')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')