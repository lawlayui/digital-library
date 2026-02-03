from dotenv import load_dotenv
from os import getenv


class Config: 
    SECRET_KEY = getenv('SECRET_KEY')
    DB_NAME = getenv('DB_NAME')
    DB_USER = getenv('DB_USER')
    DB_PWD = getenv('DB_PWD')
    DB_HOST = getenv('DB_HOST')

    DEBUG = True 