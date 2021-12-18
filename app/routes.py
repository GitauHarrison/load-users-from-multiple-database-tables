from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegisterForm, LoginForm
from app.models import Student, Teacher
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/home/student')
@login_required
def index_student():
    student = Student.query.first()
    return render_template(
        'index_student.html',
        title='Home Student',
        student=student
        )


@app.route('/home/teacher')
@login_required
def index_teacher():
    teacher = Teacher.query.first()
    return render_template(
        'index_teacher.html',
        title='Home Teacher',
        teacher=teacher
        )


@app.route('/register/student', methods=['GET', 'POST'])
def register_student():
    form = RegisterForm()
    if form.validate_on_submit():
        student = Student(
            username=form.username.data,
            email=form.email.data
            )
        student.set_password(form.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, you are now a registered student!')
        return redirect(url_for('login_student'))
    return render_template(
        'register.html',
        title='Register Student',
        form=form
        )


@app.route('/register/teacher', methods=['GET', 'POST'])
def register_teacher():
    form = RegisterForm()
    if form.validate_on_submit():
        teacher = Teacher(
            username=form.username.data,
            email=form.email.data
            )
        teacher.set_password(form.password.data)
        db.session.add(teacher)
        db.session.commit()
        flash('Congratulations, you are now a registered teacher!')
        return redirect(url_for('login_teacher'))
    return render_template(
        'register.html',
        title='Register Teacher',
        form=form
        )


@app.route('/login/student', methods=['GET', 'POST'])
def login_student():
    if current_user.is_authenticated:
        return redirect(url_for('index_student'))
    form = LoginForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(username=form.username.data).first()
        if student is None or not student.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login_student'))
        login_user(student, remember=form.remember_me.data)
        return redirect(url_for('index_student'))
    return render_template(
        'login.html',
        title='Login Student',
        form=form
        )


@app.route('/login/teacher', methods=['GET', 'POST'])
def login_teacher():
    if current_user.is_authenticated:
        return redirect(url_for('index_teacher'))
    form = LoginForm()
    if form.validate_on_submit():
        teacher = Teacher.query.filter_by(username=form.username.data).first()
        if teacher is None or not teacher.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login_teacher'))
        login_user(teacher, remember=form.remember_me.data)
        return redirect(url_for('index_teacher'))
    return render_template(
        'login.html',
        title='Login Teacher',
        form=form
        )


@app.route('/logout/student')
def logout_student():
    logout_user()
    return redirect(url_for('login_student'))


@app.route('/logout/teacher')
def logout_teacher():
    logout_user()
    return redirect(url_for('login_teacher'))
