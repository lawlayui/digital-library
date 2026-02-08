def validator_froms_auth(user_data: dict):
    try:
        username = user_data['username']
        password = user_data['password']
    except:
        return {
            'status': 'error',
            'message': 'Key Error: Missing username or password'
        }

    if len(username) < 4 or len(username) > 255:
        return {
            'status': 'error',
            'message': 'Username character max 255 and username min 4'
        }
    if (len(password) < 8):
        return {
            'status': 'error',
            'message': 'Password character min 8'
        }

    return {
        'status': 'succes'
    }

def validator(user_data: dict):
    try:
        username = user_data.get('new_username')
        password = user_data.get('new_password')
        if username is None or password is None:
            raise KeyError
    except:
        return {
            'status': 'error',
            'message': 'Key Error: Missing username or password'
        }

    if len(username) < 4 or len(username) > 255:
        return {
            'status': 'error',
            'message': 'Username character max 255 and username min 4'
        }
    if (len(password) < 8):
        return {
            'status': 'error',
            'message': 'Password character min 8'
        }

    return {
        'status': 'succes'
    }