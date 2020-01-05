from app import app
from app.db.database import init_db, db_session
import os

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
	init_db()
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='localhost', port=3000)