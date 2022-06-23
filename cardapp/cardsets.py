from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from cardapp.db import get_db

bp = Blueprint('cardsets', __name__, url_prefix='/cardsets')

@bp.route('')
def index():
    db = get_db()
    cardsets = db.execute(
        'SELECT * FROM cardset'
    ).fetchall()
    return render_template('cardsets/cardsets.html', cardsets=cardsets)

@bp.route('/new', methods=('GET', 'POST'))
def add_cardset():
    return render_template('cardsets/add_cardset.html')

@bp.route('/<int:cardset_id>')
def view_cardset(cardset_id):
    pass

@bp.route('/<int:cardset_id>/learn')
def learn_cardset(cardset_id):
    pass

@bp.route('/<int:cardset_id>/edit', methods=('GET', 'POST'))
def edit_cardset(cardset_id):
    pass

