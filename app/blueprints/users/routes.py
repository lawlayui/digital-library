from . import users_bp
from .validator import validator_froms_auth, validator
from flask import request, jsonify, url_for, g
from .service import register_user_service, login_user_service, delete_user_service, update_user_service


@users_bp.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    validation_result = validator_froms_auth(user_data)

    if validation_result['status'] == 'error':
        return jsonify(validation_result), 400

    register_result = register_user_service(user_data)
    if register_result['status'] == 'error':
        return jsonify(register_result), 400
    
    return jsonify(register_result), 200

@users_bp.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    validation_result = validator_froms_auth(user_data)
    if validation_result['status'] == 'error':
        return jsonify(validation_result), 400
    return jsonify(login_user_service(user_data)), 200

@users_bp.route('/delete', methods=['DELETE'])
def delete():
    user_id = g.user_data.get('user_id')
    delete_result = delete_user_service(user_id)
    if delete_result['status'] == 'error':
        return jsonify(delete_result), 400
    
@users_bp.route('/update', methods=['PUT'])
def update():
    user_data_new = request.get_json()
    user_data = g.user_data
    new_username = user_data_new.get('new_username')
    new_password = user_data_new.get('new_password')

    validation_result = validator(user_data_new)
    if validation_result['status'] == 'error':
        return jsonify(validation_result), 400
    
    update_result = update_user_service(user_data, new_username=new_username, new_password=new_password)
    if update_result['status'] == 'error':
        return jsonify(update_result), 400
    return jsonify(update_result), 200