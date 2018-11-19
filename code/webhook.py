from flask import Flask, request, abort, jsonify
from code.producer import Producer
from code.authentication import Authentication

app = Flask(__name__)

producer = Producer()
auth = Authentication()


def req_get(name):
    param = request.json.get(name)
    return param


@app.route('/api/user/is_exist', methods=['GET'])
def is_exist():
    user = req_get('user')
    if user is None:
        return jsonify({'status': 'user field is empty'}), 200
    result = auth.is_user_exist(user)
    if result is True:
        return jsonify({'status': 'user exist'}), 200
    return jsonify({'status': 'user not exist'}), 200


@app.route('/api/user/is_auth', methods=['GET'])
def is_auth():
    user = req_get('user')
    if user is None:
        return jsonify({'status': 'user is empty'}), 401
    verify_token = req_get('token')
    result = auth.is_authorized(user, verify_token)
    result_dict = {
        True: ({'status': 'authorized'}, 200),
        'timeout': ({'status': 'authorisation timeout'}, 401),
        'invalid token': ({'status': 'token invalid'}, 401),
        'user not exist': ({'status:': 'user not exist'}, 401)
    }
    response, status = result_dict.get(result, (None, 404))
    return jsonify(response), status


@app.route('/api/message/producer', methods=['GET', 'POST'])
def kafka_producer():
    if request.method == 'GET':
        user = req_get('user')
        if user is None:
            return jsonify({'status': 'user is empty'}), 401
        token = auth.create_user(user)
        if token:
            return jsonify({'token': token}), 200
        return jsonify({'status': 'username used'}), 401
    elif request.method == 'POST':
        user = req_get('user')
        if user is None:
            return jsonify({'status': 'user is empty'}), 401
        verify_token = req_get('token')
        # check is user authorized
        result = auth.is_authorized(user, verify_token)
        result_dict = {
            'timeout': ({'status': 'authorisation timeout'}, 401),
            'invalid token': ({'status': 'token invalid'}, 401),
            'user not exist': ({'status:': 'user not exist'}, 401)
        }
        if result is True:
            producer.send(request.json)
            return '', 200
        response, status = result_dict.get(result, (None, 404))
        return jsonify(response), status
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
