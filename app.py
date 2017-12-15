from flask import Flask, render_template

#, flash, redirect, url_for, session, request, logging
#from data import Articles
#from flask_mysqldb import flask_mysqldb
#from wtforms import Form,  StringField, TextAreaField, PasswordField, validators
#from passlib.hash import sha256_crypt
#pip install flask-mysqldb
#pip install flask-wtf 
#pip install passlib
#
#
app = Flask(__name__)

#Articles = Articles()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

#@app.route('/articles')
#def index():
#	return render_template('articles.html', articles = Articles)

#@app.route('/article/<string:id>/')
#def article(id):
#	return render_template('article.html', id=id)

if __name__ == '__main__':
	app.run(debug=True)


