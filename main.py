from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
import os
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from forms import (
    VisualInspection, 
    KaptonGluing, 
    HvIvForm, 
    SensorGluing, 
    NeedleMetrologyForm, 
    SkeletonTestForm, 
    HybridGluingForm, 
    WireBondingForm, 
    NoiseTestForm, 
    BufNimForm
)
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config["UPLOAD_FOLDER"]= "static/uploads/station_image"
ckeditor = CKEditor(app)
Bootstrap5(app)
# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nisers.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin ,db.Model):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

class Station(db.Model):
    __tablename__ = "Stations"
    id: Mapped[int] = mapped_column(Integer ,primary_key=True)
    station_name: Mapped[str] = mapped_column(String(250),unique=True,nullable =False)
    description: Mapped[str]=mapped_column(String(250) ,nullable =False)
    year:Mapped[int] =mapped_column(nullable =False)
    day:Mapped[int] =mapped_column(nullable =False)
    month:Mapped[int] =mapped_column(nullable =False)
    img_url:Mapped[str]=mapped_column(String(250) ,nullable =False)



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
        if check_password_hash(user.password ,password):
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("workflow.html")


@app.route('/stations')
@login_required
def stations():
    with app.app_context():
        result = db.session.execute(db.select(Station).order_by(Station.id))
        all_stations = result.scalars().all()
        return render_template("all_stations.html",all_stations = all_stations)
    #return render_template("stations1.html")
@app.route("/station_form")
@login_required
def show_form():
    return render_template("station_form.html")
@app.route("/add_station",methods=["POST"])
@login_required
def add_station():
    print("we have entered the upload_image")
    image = request.files["image"]
    station_name = request.form["name"]
    description = request.form["comment"]
    date = datetime.datetime.now()
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(file_path)
    print(file_path)
    new_station = Station(station_name = station_name ,year = date.year , day = date.day , month = date.month ,img_url = file_path,description = description)
    db.session.add(new_station)
    db.session.commit()
    return redirect(url_for('stations'))
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")

@app.route('/add_data', methods=["GET", "POST"])
def add_data():
    num = request.args.get('num')    
    step_no = int(num)
    if step_no == 1:
        form = VisualInspection()
    elif step_no == 2:
        form = KaptonGluing()
    elif step_no == 3:
        form = HvIvForm()
    elif step_no == 4:
        form = SensorGluing()
    elif step_no == 5:
        form = NeedleMetrologyForm()
    elif step_no == 6:
        form = SkeletonTestForm()
    elif step_no == 7:
        form = HybridGluingForm()
    elif step_no == 8:
        form = WireBondingForm()
    elif step_no == 9:
        form = NoiseTestForm()
    elif step_no == 10:
        form = BufNimForm()
    if form.validate_on_submit():
        # Handle the form submission logic here
        pass
    return render_template("visual_inspection.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
