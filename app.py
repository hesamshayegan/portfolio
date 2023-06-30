from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)

app.app_context().push()


@app.route('/')
def homepage():

    return render_template('base.html')
