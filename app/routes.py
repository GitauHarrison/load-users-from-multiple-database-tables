from app import app
from flask import render_template
from app.forms import RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register/student')
def register_student():
    form = RegisterForm()
    return render_template(
        'register.html',
        title='Register Student',
        form=form
        )


@app.route('/register/teacher', methods=['GET', 'POST'])
def register_teacher():
    form = RegisterForm()
    return render_template(
        'register.html',
        title='Register Teacher',
        form=form
        )
