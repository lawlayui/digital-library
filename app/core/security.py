from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app
import uuid
import jwt
import datetime 


def generate_hash(password:str):
    hashed = generate_password_hash(password)
    return hashed 

def verify_hash(password:str, password_hashed:str):
    result = check_password_hash(password_hashed,password)
    return result 

def generate_uuid():
    value = uuid.uuid4().hex
    return value 

def generate_jwt(data: dict):
    payload = {
        'exp' : datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=100),
        'iat': datetime.datetime.now(datetime.timezone.utc),
        'data': data 
    }

    token = jwt.encode(payload,current_app.config['SECRET_KEY'],'HS256')
    return token 

def verify_jwt(token):
    try:
        claims = jwt.decode(token,current_app.config['SECRET_KEY'])
        return claims
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid Token")
    
