from flask import Blueprint
from app.api.users import main as user
from app.api import app

app.register_blueprint(user) # For registering User APIs.