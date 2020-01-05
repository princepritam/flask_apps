import datetime, code
from flask import Blueprint, flash, request, jsonify, session, render_template, redirect
from sqlalchemy.orm import sessionmaker
from app.models.user import *
from app.db.database import db_session, engine
import code

main = Blueprint('user', __name__)

Session = sessionmaker(bind=engine)

@main.route('/')
def home():
	# code.interact(local=dict(globals(), **locals()))
	if not session.get('logged_in'):
		return render_template('signup.html')
	else:
		# return "Hello Boss! <a href="/logout">Logout</a>"
		return  "hello"
		pass

@main.route('/accounts/signup', methods=['POST'])
def create_user():
	create_params = request.form
	try:
		user = User(
				create_params['first_name'],
				create_params['last_name'],
				create_params['email'],
				create_params['password'])
		db_session.add(user)
		db_session.commit()
	except Exception as e:
		return jsonify({"message": str(e)}), 422
	return jsonify({"message": "User created successfully."}), 201

@main.route('/accounts/login', methods=['POST'])
def login():
	login_params = request.form
	try:
		# code.interact(local=dict(globals(), **locals()))
		if not session.get('logged_in'):
			email = login_params["email"]
			password = login_params["password"]
			session_instance = Session()
			is_user_present = session_instance.query(User).filter(User.email == email, User.password == password).first()
			if is_user_present:
				session['logged_in'] = True
			else:
				session['logged_in'] = False
				flash("Invalid email or password.")
				return home()
				# raise Exception("Invalid email or password.")
		else:
			raise Exception("User already logged in.")
		
	except Exception as e:
		return jsonify({"message": str(e)}), 422
	return jsonify({"message": "User successfully logged in."}), 201

@main.route('/accounts/logout')
def logout():
	session['logged_in'] = False
	return jsonify({"message": "Successfully logged out."})


@main.route('/users', methods=['GET'])
def get_all_users():
	users = User.query.all()
	users_list = []
	for user in users:
		users_list.append({
				"id": user.id,
				"first_name": user.first_name,
				"last_name": user.last_name,
				"email": user.email})
	return jsonify({"users": users_list})