from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
import sqlite3
import os

app = Flask(__name__)

app.config

@app.route("/")
def difficulty() :
    return "Hello World!"

if __name__ == "__main__" :
    app.run()