from flask import Flask, render_template,flash,logging,redirect,session,request
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form,StringField,validators,PasswordField,TextAreaField,TextField
from passlib.hash import sha256_crypt

app = Flask(__name__)

Articles = Articles()
@app.route('/articles')
def articles():
    return render_template('articles.html',articles = Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html',id=id)

@app.route('/about_us')
def about():
    return render_template('about_us.html')
@app.route('/')
def index():
    return render_template('home.html')

class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=4,max=20)])
    username = StringField('Username', [validators.Length(min=5,max=20)])
    email = StringField('Email',[validators.Length(min=5,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message='passwords do not match')
    ])
    confirm = PasswordField('confirm Password')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        return render_template('register.html')
    return render_template('register.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
