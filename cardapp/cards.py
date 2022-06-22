from cardapp.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from cardapp.db import get_db

bp = Blueprint('cards', __name__, url_prefix='/cards')

@bp.route('')
def index():
    return "Not sure what goes here"

@bp.route('/new', methods=('GET', 'POST'))
def add_card():
    return "Add new card"

@bp.route('/delete/<int:card_id>', methods=('GET', 'POST'))
def delete_card(card_id):
    return "Delete a card"

@bp.route('/edit/<int:card_id>', methods=('GET', 'POST'))
def edit_card(card_id):
    return "Edit a card"
