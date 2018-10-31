from flask import Flask, request, abort, jsonify
from producer import Producer
from authentication import Authentication

app = Flask(__name__)

producer = Producer()
auth = Authentication()


def get_user(req):
    if req.json.get('user', None):
        user = req.json['user']
        return user
    return None


@app.route('/api/user/is_exist', methods=['GET'])
def is_exist():
    user = get_user(request)
    if user is None:
        return jsonify({'status': 'user field is empty'}), 401
    result = auth.is_exist(user)
    if result is True:
        return jsonify({'status': 'user exist'}), 200
    return jsonify({'status': 'user user not exist'}), 401


@app.route('/api/user/is_auth', methods=['GET'])
def is_auth():
    user = get_user(request)
    if user is None:
        return jsonify({'status': 'user is empty'}), 401
    verify_token = request.args.get('verify_token')
    result = auth.is_authorized(user, verify_token)
    result_dict = {
        True: ({'status': 'authorized'}, 200),
        'timeout': ({'status': 'authorisation timeout'}, 401),
        'invalid token': ({'status': 'token invalid'}, 401)
    }
    response, status = result_dict.get(result)
    return jsonify(response), status


@app.route('/api/message/producer', methods=['GET', 'POST'])
def kafka_producer():
    if request.method == 'GET':
        user = get_user(request)
        if user is None:
            return jsonify({'status': 'user is empty'}), 401
        token = auth.create_user(user)
        if token:
            return jsonify({'token': token}), 200
        return jsonify({'status': 'username used'}), 401
    elif request.method == 'POST':
        user = get_user(request)
        if user is None:
            return jsonify({'status': 'user is empty'}), 401
        verify_token = request.args.get('verify_token')
        # check is user authorized
        result = auth.is_authorized(user, verify_token)
        result_dict = {
            'timeout': ({'status': 'authorisation timeout'}, 401),
            'invalid token': ({'status': 'token invalid'}, 401)
        }
        if result is True:
            producer.send(request.json)
            return '', 200
        response, status = result_dict.get(result)
        return jsonify(response), status
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
