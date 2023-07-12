from flask import Flask, render_template, redirect, send_file, send_from_directory

app = Flask(__name__)

app.app_context().push()


@app.route('/')
def root():

    return redirect('/homepage')



@app.route('/homepage')
def homepage():

    return render_template('homepage.html')

@app.route('/about')
def show_about():

    return render_template('show_about.html')

