import mysql.connector
from flask import g, current_app


def get_db(): 
    if 'db' not in g:
        g.db = mysql.connector.connect(
            user=current_app.config['DB_USER'],
            host=current_app.config['DB_HOST'],
            username=current_app.config['DB_USER'],
            password=current_app.config['DB_PWD'],
            database=current_app.config['DB_NAME']
        )
    return g.db

def db_close(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()