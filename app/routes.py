from flask import Blueprint, render_template, request, redirect, url_for, session, Response
from . import db
from .models import User

bp = Blueprint('main', __name__)

ADMIN_PASSWORD = 'admin123'

@bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.register'))
    return render_template('register.html')


@bp.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form['password']
        if password == ADMIN_PASSWORD:
            session['is_admin'] = True
            return redirect(url_for('main.admin'))
        else:
            return render_template('admin_login.html', error='Invalid password')
    return render_template('admin_login.html')


@bp.route('/admin')
def admin():
    if not session.get('is_admin'):
        return redirect(url_for('main.admin_login'))
    users = User.query.all()
    return render_template('admin.html', users=users)


@bp.route('/logout')
def logout():
    session.pop('is_admin', None)
    return redirect(url_for('main.register'))

