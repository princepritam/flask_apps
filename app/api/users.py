import datetime, code
from flask import Blueprint, flash, request, jsonify, session, render_template, redirect
from sqlalchemy.orm import sessionmaker
from app.models.user import *
from app.db.database import db_session, engine
import code

main = Blueprint('user', __name__)

Session = sessionmaker(bind=engine)

@main.route('/accounts/signup')
def signup():
	return render_template('signup.html')

@main.route('/signup', methods=['POST'])
def create_user():
	create_params = request.form
	try:
		user = User(
				first_name=create_params['first_name'],
				last_name=create_params['last_name'],
				email=create_params['email'],
				phone_number=create_params['phone_number'],
				password=create_params['password'])
		db_session.add(user)
		db_session.commit()
		return render_template('welcome.html', name= user.first_name)
	except Exception as e:
		# code.interact(local=dict(globals(), **locals()))
		return render_template('error.html', error=str(e.args[0]))

@main.route('/accounts/login', methods=['GET', 'POST'])
def login_user():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		try:
			login_params = request.form
			email = login_params["email"]
			password = login_params["password"]
			session_instance = Session()
			is_user_present = False
			fetch_details = session_instance.query(User.email, User.first_name).filter(User.email.in_([ email]), User.password.in_([password])).first()
			# code.interact(local=dict(globals(), **locals()))
			if fetch_details :
				is_user_present = True if (fetch_details[0] == email) else False
			if is_user_present:
				return render_template('welcome.html', name = fetch_details[1])
			else:
				raise Exception("Invalid email or password.")
		except Exception as e:
			return render_template('error.html', error=str(e))


@main.route('/users', methods=['GET'])
def get_all_users():
	users = User.query.all()
	users_list = []
	for user in users:
		users_list.append({
				"id": user.id,
				"first_name": user.first_name,
				"last_name": user.last_name,
				"email": user.email,
				"password":user.password})
	return jsonify({"users": users_list})