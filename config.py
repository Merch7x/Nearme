"""Create app configs"""
import os


class Config:
    """Creates configuration variables"""
    SECRET_KEY = os.environ.get('SECRET_KEY')\
        or 'BBLDRIZZY'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://admin:admin@nm-db-1.cb0sgeak46n9.eu-west-2.rds.amazonaws.com/nearmedev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
