from flask import Flask ,request, redirect, url_for, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
import datetime
from sqlalchemy import Integer, String

app = Flask(__name__)
app.config["UPLOAD_FOLDER"]= "static/uploads/station_image"
# TODO: THIS APP SHOULD BE LOCKED UNLESS ACCESSED WITH THE VALID AUTH TOKEN
# create a database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI",'sqlite:///labs.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Station(db.Model):
    __tablename__ = "Stations"
    id: Mapped[int] = mapped_column(Integer ,primary_key=True)
    station_name: Mapped[str] = mapped_column(String(250),unique=True,nullable =False)
    description: Mapped[str]=mapped_column(String(250) ,nullable =False)
    year:Mapped[int] =mapped_column(nullable =False)
    day:Mapped[int] =mapped_column(nullable =False)
    month:Mapped[int] =mapped_column(nullable =False)
    img_url:Mapped[str]=mapped_column(String(250) ,nullable =False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Station).order_by(Station.id))
        all_stations = result.scalars().all()
    #return render_template("all_stations.html",all_stations = all_stations)
    return render_template("stations1.html")
@app.route("/station_form")
def show_form():
    return render_template("station_form.html")


@app.route("/add",methods=["POST"])
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
    return redirect(url_for('home'))

@app.route("/visual_inspection")
def station_1():
    return render_template("station1.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)
