import os
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL(require_tld=True,message='Invalid URL')])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = StringField('Coffee Rating', validators=[DataRequired()])
    wifi_rating = StringField('Wifi Rating', validators=[DataRequired()])
    power_rating = StringField('Power Outlet Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("coffee_index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(form.cafe.data,
              form.location.data,
              form.open_time.data,
              form.close_time.data,
              form.coffee_rating.data,
              form.wifi_rating.data,
              form.power_rating.data)
        try:
            with open('Cafe/cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
                write_in_csv = csv.writer(csv_file)
                write_in_csv.writerow([
                    form.cafe.data,
                    form.location.data,
                    form.open_time.data,
                    form.close_time.data,
                    form.coffee_rating.data,
                    form.wifi_rating.data,
                    form.power_rating.data
                ])
            return redirect('cafes')
        except Exception as e:
            return str(e)
    try:
        return render_template('add.html', form=form)
    except Exception as e:
        return str(e)


@app.route('/cafes', methods=["GET", "POST"])
def cafes():
    with open('Cafe/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        # print(list_of_rows)
    try:
        return render_template('cafes.html', cafes=list_of_rows)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
