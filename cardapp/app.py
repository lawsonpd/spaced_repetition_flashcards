from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    pass

@app.route('/add-card')
def add_card():
    pass

@app.route('/delete-card/<int:card_id>')
def delete_card():
    pass

