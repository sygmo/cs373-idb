from flask import Flask
app flask(__name__)

@app_route("/")
def hello() :
	return "Hello World!"

if __name__ == "__main__" :
	app.run()