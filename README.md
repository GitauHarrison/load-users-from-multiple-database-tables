# Load Users From Multiple Flask Database Tables

Here is a simple Flask application that loads users from two different database tables, student table and teacher table. When you navigate to the home page of each individual user, you will see their personal information.

![Full Application](app/static/images/full_project.png)

## Features

- Load users from two different database tables

## Tools Used

- Flask
- SQLAlchemy
- Python3
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Bootstrap
- Flask-login
- Email Validator
- Python-dotenv

## Deployed Application

- This application has not been deployed anywhere yet.

## Testing the Application Locally

1. Clone this repository
```python
$ git clone git@github.com:GitauHarrison/load-multiple-database-users-in-flask.git
```

2. Change directory to the cloned repository
```python
$ cd load-multiple-database-users-in-flask
```
3. Create and activate a virtual environment
```python
$ mkvirtualenv venv
```
4. Install dependencies
```python
(venv) $ pip3 install -r requirements.txt
```
5. Run the application
```python
(venv) $ flask run
```

Note that if you would like to provide your own SECRET_KEY, you can do so by creating a `.env` file and add the value as seen in `.env-template`.

## Learn

If you would like to learn how to built this from scratch, you can read [this article](https://github.com/GitauHarrison/notes/blob/master/load_multiple_users.md) by yours truly. I hope you will enjoy it! 