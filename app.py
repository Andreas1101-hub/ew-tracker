from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    return render_template("list.html", rows = db.get_ews())

@app.route('/add', methods=['POST'])
def add_ew():
    Database.create_ew()
    return redirect('/')


# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass