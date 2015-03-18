from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
import sqlite3
import os

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'static/starlordsdb.sqlite')
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
    	print("I am here")
    	g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def homepage():
	return render_template("index.html");

if __name__ == "__main__":
	with app.app_context():
		cur = get_db().execute("select * from constellation")
		entries = cur.fetchall()

		for i in entries:
			print(i['name']);

	app.run()