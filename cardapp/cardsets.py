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
    if request.method == 'POST':
        cardsetname = request.form['cardset-name']
        error = None

        if not cardsetname:
            error = 'Cardset name is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO cardset'
                ' VALUES (?, ?)',
                (None, cardsetname)
            )
            db.commit()
            return redirect(url_for('cardsets.index'))
    return render_template('cardsets/add_cardset.html')

@bp.route('/<int:cardset_id>')
def view_cardset(cardset_id):
    db = get_db()
    cardset = db.execute(
        'SELECT name FROM cardset'
        ' WHERE id = ?',
        (cardset_id,)
    ).fetchone()

    cards = db.execute(
        'SELECT prompt, answer FROM card'
        ' WHERE card.cardset_id = ?',
        (cardset_id,)
    ).fetchall()
    return render_template('cardsets/cardset.html', cardset=cardset, cards=cards)

@bp.route('/<int:cardset_id>/learn')
def learn_cardset(cardset_id):
    pass

@bp.route('/<int:cardset_id>/edit', methods=('GET', 'POST'))
def edit_cardset(cardset_id):
    pass

