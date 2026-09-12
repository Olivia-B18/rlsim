from flask import render_template, Blueprint
from flask_login import login_required

from . import flow

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template('home.html')

@views.route("/intro")
@login_required
@flow.step("intro")
def intro():
    return render_template('intro.html')

@views.route("/snake")
@login_required
@flow.step("snake")
def snake():
    return render_template('snake.html')

@views.route("/snakeai")
@login_required
@flow.step("snakeai")
def snakeai():
    return render_template('snakeai.html')


