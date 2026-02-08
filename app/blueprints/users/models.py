from app.core.db import get_db


def select_user(data_user: dict=None, id: int=None):
    try:
        username = data_user['username']
    except:
        username = None
    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = 'select * from users where username = %s or id = %s'
    values = (username,id)

    cursor.execute(query, values)

    result = cursor.fetchone()

    cursor.close()

    return {
        'status': 'succes',
        'data': result
    }


def insert_user(data_user: dict):
    username = data_user['username']
    password = data_user['password']
    role = data_user['role']
    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = 'insert into users(username, password, role) values(%s, %s, %s)'
    values = (username, password, role)

    cursor.execute(query, values)
    user_id = cursor.lastrowid
    db.commit()
    cursor.close()

    return {
        'status': 'succes',
        'user_id': user_id
    }


def delete_user_db(user_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = 'delete from users where id = %s'
    values = (user_id,)

    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return {
        'status': 'succes'
    }


def update_user(username: str, password: str, new_username: str = None, new_password: str = None):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = "update users set "
    values = []

    if new_username:
        query += "username = %s, "
        values.append(new_username)
    if new_password:
        query += "password = %s, "
        values.append(new_password)

    query = query.rstrip(", ")
    query += " where username = %s"
    values.append(username)

    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return {
        'status': 'succes'
    }
