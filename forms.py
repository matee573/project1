from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField, PasswordField, RadioField, DateField, SelectField
from wtforms.validators import DataRequired, length, equal_to

class AddProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი", validators=[ DataRequired() ] )
    price = IntegerField("ფასი", validators=[ DataRequired() ])
    img = FileField("სურათის სახელი",
                     validators=[
                          FileRequired(),
                          FileAllowed([ "jpg", "png"])
                    ])

    submit = SubmitField("დამატება")


class RegisterForm(FlaskForm):
    username = StringField("შეიყვანეთ სახელი")
    password = PasswordField("შეიყვანეთ პაროლი", validators=[length(min=8, max=64)] )
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[equal_to("password", message="პაროლი არ ემთხვევა")] )
    gender = RadioField("მონიშნეთ სქესი" )
    birthday = DateField("დაბადების თარიღი")
    country = SelectField("მონიშნეთ ქვეყანა")
    
    submit = SubmitField("რეგისტრაცია")
 

 
class LoginForm(FlaskForm):
    username = StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired()])
    
    submit = SubmitField("ავტორიზაცია")

