from flask import Flask, render_template
from wtforms import StringField,PasswordField,SubmitField # it will be used to create the form fields in the form class below
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,Length # it will be used to validate the form fields in the form class below
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "Hitesh@123"

bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email(message='Invalid email address')])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8,message='Must be atleast 8 '
                                                                                              'characters')])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST','GET']) # we are using both the methods POST and GET
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@example.com' and form.password.data=='12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
# create an instance of the form class LoginForm and store it in the variable form
    return render_template('login.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)
