from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField ,FileField ,DateField , BooleanField , SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = FileField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    date = DateField("Expary Date", format='%Y-%m-%d')
    cooling_point = BooleanField("6 cp" , validators=[DataRequired()])
    cooling_points = SelectField(
        'Cooling Point', 
        choices=[('6 cp', '6 cp'), ('5 cp', '5 cp')],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

# create Station Add forms
class AddStationForm(FlaskForm):
    station_name = StringField("Station Name", validators=[DataRequired()])
    station_img = FileField("Upload the Station Image", validators=[DataRequired()])
    station_comment = CKEditorField("Comment", validators=[DataRequired()])
    submit= SubmitField("Save Station")

# VisualInspectionForm done

class VisualInspection(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment= CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")

# KaptonGluing

class KaptonGluing(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    sensor_type = SelectField(
        'Sensor Type',
        choices=[('Top Sensor', 'Top Sensor'), ('Bottom Sensor', 'Bottom Sensor')],
        validators=[DataRequired()]
    )
    date = DateField("Expary Date", format='%Y-%m-%d')

    cooling_points = SelectField(
        'Cooling Point',
        choices=[('6 cp', '6 cp'), ('5 cp', '5 cp')],
        validators=[DataRequired()]
    )
    part_A_batch_no = StringField("Polytec 601 partA / Batch No :")
    part_A_exp_date = DateField("part A Expiry Date", format='%Y-%m-%d' ,validators=[DataRequired()])
    part_B_batch_no = StringField("Polytec 601 partB / Batch No :")
    part_B_exp_date = DateField("part B Expiry Date", format='%Y-%m-%d', validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")

#date = DateField("Expary Date", format='%Y-%m-%d' ,validators=[DataRequired()])
# HV and IV Test

class HvIvForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")

#SensorGluing

class SensorGluing(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")
#Needle Metrology

class NeedleMetrologyForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    x_coordinate = StringField("Delta x", validators=[DataRequired()])
    y_coordinate = StringField("Delta y", validators=[DataRequired()])
    del_theta = StringField("Rotation", validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")

# Skeleton test

class SkeletonTestForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")
# Hybrid Gluing

class HybridGluingForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")

#Wire Bonding

class WireBondingForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")

#NoiseTest

class NoiseTestForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit= SubmitField("Save")
#BufNim Test

class BufNimForm(FlaskForm):
    check_id = StringField("Check ID", validators=[DataRequired()])
    receiver_name= StringField("Receiver Name ", validators=[DataRequired()])
    shipment_info = StringField("Shipment Info ", validators=[DataRequired()])
    image = FileField("Upload Image" ,validators=[DataRequired()])
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Save")
