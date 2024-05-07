"""Create app configs"""
import os


class Config:
    """Creates configuration variables"""
    SECRET_KEY = os.environ.get('SECRET_KEY')\
        or 'BBLDRIZZY'
