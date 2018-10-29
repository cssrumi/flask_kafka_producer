from flask import Flask, request, abort

from producer import Producer

app = Flask(__name__)


@app.route('/api/message/producer', methods=['POST'])
def kafka_producer():
    producer = Producer()
    if request.method == 'POST':
        producer.send(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
