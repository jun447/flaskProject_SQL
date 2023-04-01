from flask import Blueprint,render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():  # put application's code here
    return render_template("home.html")
