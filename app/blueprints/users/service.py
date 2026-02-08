from .models import select_user, insert_user, delete_user_db, update_user
from app.core.security import generate_hash, verify_hash, generate_jwt


def register_user_service(data_user: dict):
    try:
        role = data_user['role']
    except:
        data_user['role'] = 'user'

    select_result = select_user(data_user)
    if select_result['data']:
        return {
            'status': 'error',
            'message': 'Akun alredy exis'
        }

    data_user['password'] = generate_hash(data_user['password'])

    insert_result = insert_user(data_user)

    jwt = generate_jwt(
        {'user_id': insert_result['user_id'], 'role': data_user['role']})
    return {
        'status': 'succes',
        'token': jwt.decode(),
        'message': 'Succes created your akun'
    }

def login_user_service(data_user: dict):
    select_result = select_user(data_user)['data']

    if not select_result:
        return {
            'status': 'error',
            'message': 'Akun not found'
        }
    

    if verify_hash(data_user['password'],select_result['password']):
        token = generate_jwt({'user_id': select_result['id'], 'role': select_result['role']})
        return {
            'status': 'succes',
            'message': 'Succes logined akun',
            'token': token.decode()
        }
    return {
        'status': 'error',
        'message': 'Invalid password'
    }

def delete_user_service(user_id: int):
    if not select_user(id=user_id)['data']:
        return {
            'status': 'error',
            'message': 'Akun not found'
        }
    delete_user_db(user_id)
    return {
        'status': 'succes',
        'message': 'Succes delete akun'
    }

def update_user_service(data_user: dict, new_username: str = None, new_password: str = None):
    select_result = select_user(id=data_user['user_id'])['data']
    if not select_result:
        return {
            'status': 'error',
            'message': 'Akun not found'
        }

    if new_password:
        new_password = generate_hash(new_password)

    update_user(select_result['username'], select_result['password'], new_username, new_password)

    return {
        'status': 'succes',
        'message': 'Succes update akun'
    }