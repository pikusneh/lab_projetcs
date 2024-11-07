import os
import datetime
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['STATIONS_APP_URL'] = 'http://127.0.0.1:5001/'  # Set the URL of the second app
# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE USER TABLE IN DB
class User(UserMixin ,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# Flask log-in
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User ,user_id)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register',methods =['GET','POST'])
def register():
    if request.method == "POST":
        with app.app_context():
            new_user = User(email =request.form["email"] ,password =generate_password_hash(request.form.get("password"),method='pbkdf2:sha256',salt_length=8),name=request.form["name"] )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template("secrets.html",name = request.form.get("name"))
    return render_template("register.html")

@app.route('/login',methods =["GET","POST"])
def login():
    if request.method =="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user and check_password_hash(user.password ,password):
            login_user(user)
            # return redirect(url_for('secrets'))
            return redirect(app.config['STATIONS_APP_URL'])
        else:
            flash("User : " + email + " does not exist", 'danger')
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)