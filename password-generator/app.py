import string,random
from flask import Flask,url_for,render_template,redirect,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField,IntegerField
from wtforms.validators import DataRequired,Length,NumberRange
from logic import generate_password

app = Flask(__name__)
app.config['SECRET_KEY'] = '6a239f110bd3d9297a68618cf18e510c'

class InfoForm(FlaskForm):
    fullname = StringField('Your Full name',validators=[DataRequired(),Length(min=2,max=30)])
    dateofbirth = DateField('Enter your DOB',validators=[DataRequired()])
    length = IntegerField('Password Length',validators=[DataRequired(),NumberRange(min=8,max=15)])
    submit = SubmitField('Generate Password')

@app.route("/",methods = ['GET','POST'])
def home():
    form = InfoForm()

    if form.validate_on_submit():
        passwords = []
        for _ in range(5):
            passwords.append(generate_password(form.fullname.data,form.dateofbirth.data,form.length.data))
            session['passwords'] = passwords
        return redirect(url_for('home'))
    
    passwords = session.pop('passwords',None)
    return render_template('home.html',form = form,passwords = passwords)

if __name__ == '__main__':
    app.run(debug=True)