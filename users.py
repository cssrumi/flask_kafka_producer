import os
import json
import binascii
import pymongo
from collections import namedtuple
from datetime import datetime


class Users:
    def __init__(self):
        self.cfg = self._read_config()
        self.m_cfg = self._set_mongodb_config()
        self.users = self._set_users()

    def is_exist(self, user):
        if self.users.find_one({'user': user}) is not None:
            return True
        return False

    def _read_config(self, file='cfg.json'):
        # cfg.json
        # {
        #     "mongodb": {
        #         "ip": "ip",
        #         "port": port,
        #         "user": "username",
        #         "password": "password"
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

    def _set_mongodb_config(self):
        m_cfg = None
        if self.cfg is not None:
            m_cfg = self.cfg.get('mongodb', None)
        if m_cfg is not None:
            m_ip = m_cfg.get('ip', 'localhost')
            m_port = m_cfg.get('port', 27017)
            m_user = m_cfg.get('user', 'root')
            m_pass = m_cfg.get('password', 'example')
        else:
            m_ip, m_port, m_user, m_pass = 'localhost', 27017, 'root', 'example'
        MongoConfig = namedtuple('MongoConfig', 'm_ip, m_port, m_user, m_pass')
        m_cfg = MongoConfig(m_ip=m_ip, m_port=m_port, m_user=m_user, m_pass=m_pass)
        return m_cfg

    def _set_users(self):
        ip = 'mongodb://{}:{}@{}:{}'.format(
            self.m_cfg.m_user,
            self.m_cfg.m_pass,
            self.m_cfg.m_ip,
            self.m_cfg.m_port
        )
        print(ip)
        db_client = pymongo.MongoClient(ip)
        db = db_client.users
        collection = db.users
        return collection

    def get_user_data(self, user):
        result = self.users.find_one({'user': user})
        if result is None:
            result = {}
        return result

    def create_token(self):
        token = binascii.hexlify(os.urandom(24))
        return token.decode('utf-8')

    def insert_user(self, user):
        token = self.create_token()
        token_datetime = datetime.now()
        user_data = {
            'user': user,
            'token': token,
            'token_datetime': token_datetime,
        }
        self.users.insert_one(user_data)
        return token

    def update_user(self, user, token, token_datetime):
        if self.users.count_documents({'user': user}):
            self.users.update({'user': user}, {'$set': {
                'user': user,
                'token': token,
                'token_datetime': token_datetime
            }})
            return True
        return False

    def recreate(self):
        pass
