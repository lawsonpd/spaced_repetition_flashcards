from cardapp.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from cardapp.db import get_db

bp = Blueprint('cards', __name__)

@bp.route('')
def index():
    pass

@bp.route('/cardsets')
def cardsets():
    pass

@bp.route('/learn/<int:cardset_id>')
def learn_cardset(cardset_id):
    pass

@bp.route('/add-card', methods=('GET', 'POST'))
def add_card():
    pass

@bp.route('/delete-card/<int:card_id>', methods=('GET', 'POST'))
def delete_card(card_id):
    pass
