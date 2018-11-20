import json
from time import sleep
from kafka import KafkaProducer


class Producer:
    def __init__(self, **kwargs):
        self.kafka_param = dict()
        self.kafka_param['bootstrap_servers'] = 'localhost:9092'

        for key, value in kwargs.items():
            self.kafka_param[key] = value
        self.producer = None
        self._set_producer()

    def _set_producer(self):
        while not self._try_producer():
            sleep(5)

    def _try_producer(self):
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=self.kafka_param['bootstrap_servers'],
                value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            )
        except Exception as error:
            print(error)
            return False
        else:
            return True

    def _parse_json(self, json_dict):
        message = json_dict
        if message.get('topic', None):
            topic = message['topic']
            del message['topic']
        else:
            topic = 'test'
        if message.get('token', None):
            del message['token']
        # message = json.dumps(message).encode('utf-8')
        return topic, message

    def _send_to_topic(self, topic, message):
        print('message:', message,
              '\ttype:', type(message),
              '\ttopic:', topic,
              '\tserver:', self.kafka_param.get('bootstrap_servers', 'localhost:9092'))
        future = self.producer.send(topic, value=message)
        result = future.get(timeout=60)

    def send(self, json_dict):
        topic, message = self._parse_json(json_dict)
        self._send_to_topic(topic, message)

    @staticmethod
    def _read_config(file='cfg.json'):
        # cfg.json
        # {
        #     "kafka": {
        #         "ip": "ip",
        #         "port": port,
        #     }
        # }
        try:
            with open(file, 'r') as f:
                cfg = json.load(f)
        except OSError:
            pass
        else:
            return cfg
        return None

    @staticmethod
    def bootstrap_from_cfg():
        cfg = Producer._read_config()
        k_cfg = None
        if cfg is not None:
            k_cfg = cfg.get('kafka', None)
        if k_cfg is not None:
            k_ip = k_cfg.get('ip', 'localhost')
            k_port = k_cfg.get('port', 9092)
        else:
            k_ip, k_port = 'localhost', 9092
        result = '{}:{}'.format(k_ip, k_port)
        return result
