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
def indexpage():
	return render_template("index.html")

@app.route('/families')
def familiespage():
    return render_template("families.html")
	
@app.route('/constellations')
def constellationspage():
    return render_template("constellations.html")

@app.route('/stars')
def starspage():
    return render_template("stars.html")

@app.route('/planets')
def planetspage():
    return render_template("planets.html")

@app.route('/moons')
def moonspage():
    return render_template("moons.html")
	
@app.route('/aboutus')
def aboutuspage():
	return render_template("aboutus.html")
	
@app.route('/dictionary')
def dictionarypage():
	return render_template("dictionary.html")

@app.route('/ursamajor')
def ursamajorpage():
	return render_template("ursamajor.html")	

@app.route('/home')
def homepage():
	return render_template("home.html")

@app.route('/perseus')
def perseuspage():
	return render_template("perseus.html")

@app.route('/andromeda')
def andromedapage():
	return render_template("andromeda.html")
	
@app.route('/draco')
def dracopage():
	return render_template("draco.html")
	
@app.route('/solarsystem')
def solarsystem_page():
	return render_template("solarsystem.html")

@app.route('/iota-draconis')
def iotadraconispage():
	return render_template("iota-draconis.html")
	
@app.route('/wasp-1')
def wasp1page():
	return render_template("wasp-1.html")
	
@app.route('/sun')
def solarsystempage():
	return render_template("sun.html")	

@app.route('/iota-draconis-b')
def iotadraconisbpage():
	return render_template("iota-draconis-b.html")
	
@app.route('/wasp-1b')
def wasp1bpage():
	return render_template("wasp-1b.html")
	
@app.route('/jupiter')
def jupiterpage():
	return render_template("jupiter.html")	
	
@app.route('/europa')
def europapage():
	return render_template("iota-draconis.html")
	
@app.route('/io')
def iopage():
	return render_template("wasp-1.html")
	
@app.route('/callistro')
def callistropage():
	return render_template("callistro.html")		
	
if __name__ == "__main__":
	with app.app_context():
		cur = get_db().execute("select * from constellation")
		entries = cur.fetchall()

		for i in entries:
			print(i['name']);

	app.run()