import os
import json
import binascii
import pymongo
from datetime import datetime

class Users:
    def __init__(self):
        self.users = self._users()
        self.cfg = self._read_config()

    def is_exist(self, user):
        if self.users.find({'user', user}):
            return True
        return False

    def _read_config(self, file='cfg.json'):
        with open(file, 'r') as f:
            cfg = json.load(f)
            print(cfg)
        return cfg

    def _users(self):
        m_cfg = self.cfg.get('mongodb', None)
        if m_cfg is not None:
            m_ip = m_cfg.get('ip', 'localhost')
            m_port = int(m_cfg.get('port', 27017))
        else:
            m_ip, m_port = 'localhost', 27017

        db_client = pymongo.MongoClient(m_ip, m_port)
        db = db_client.users
        collection = db.users
        return collection

    def get_user_data(self, user):
        result = self.users.find({'user', user})
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
        if self.users.count_documents({'user', user}):
            self.users.update_many({'user', user}, {'$set': {
                'token': token,
                'token_datetime': token_datetime
            }})
        return True

    def recreate(self):
        pass
