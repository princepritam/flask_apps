from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.models import user
import code

engine = create_engine('sqlite:////tmp/test_1.db', echo=True, connect_args={'check_same_thread': False})
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    user
    Base.metadata.create_all(bind=engine)
