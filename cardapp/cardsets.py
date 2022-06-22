from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from cardapp.db import get_db

bp = Blueprint('cardsets', __name__, url_prefix='/cardsets')

@bp.route('')
def index():
    return render_template('cardsets/cardsets.html')

@bp.route('/new', methods=('GET', 'POST'))
def add_cardset():
    return "Add new cardset"

