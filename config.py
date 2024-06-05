import os

# this is a config file for this application

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' 

    """this is a variable where the flask-sqlachemy
    looks for the location of this application's database
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
