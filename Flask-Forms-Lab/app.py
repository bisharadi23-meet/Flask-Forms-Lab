from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "bishara"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
		print("get")
	if request.method == 'POST':
		name = request.form['username']
		passw = request.form['password']
		print("we are inside post")
		print(name)
		print(passw)
		if name == username and passw == password:
			return redirect(url_for('home'))
		else :
			return render_template('login.html')
	
@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html' , friends = facebook_friends)
	
@app.route('/friend_exists''/<string:name>', methods=['GET', 'POST'])  # '/' for the default page
def friend_exist(name):
	return render_template('friend_exists.html' , n = name, facebook_friends = facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
	debug=True
	)