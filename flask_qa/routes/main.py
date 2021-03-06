from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from flask_qa.extensions import db

from flask_qa.models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
   
    return render_template('home.html')

@main.route('/profile_user', methods=['GET', 'POST'])
@login_required
def profile_user():

    appd_users = User.query.filter_by(appd=True).all()

    context = {
        'appd_users' : appd_users
    }

    return render_template('profile_user.html', **context)

@main.route('/profile_appd_user')
@login_required
def profile_appd_user():
    if not current_user.appd:
        return redirect(url_for('main.index'))

    users = User.query.filter_by(appd=True).all()

    context = {
        'users' : users
    }

    return render_template('profile_appd_user.html', **context)

@main.route('/users')
@login_required
def users():
    if not current_user.admin:
        return redirect(url_for('main.index'))

    users = User.query.filter_by(admin=False).all()

    context = {
        'users' : users
    }

    return render_template('users.html', **context)

@main.route('/promote/<int:user_id>')
@login_required
def promote(user_id):
    if not current_user.admin:
        return redirect(url_for('main.index'))

    user = User.query.get_or_404(user_id)

    user.appd = True
    db.session.commit()

    return redirect(url_for('main.users'))