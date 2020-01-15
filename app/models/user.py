from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), unique=False, nullable=False)
    last_name = Column(String(50), unique=False, nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(12), unique=False, nullable=False)
    phone_number = Column(String(10,10), unique=True, nullable=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None, phone_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def __repr__(self):
        return '<User %r>' % (self.name)