from datetime import datetime, timedelta
from users import Users

# in hour
CLIENT_AUTH_TIMEOUT = 1


class Authentication:
    def __init__(self):
        self.users = Users()

    def is_user_exist(self, user):
        if self.users.is_exist(user):
            return True
        return False

    def get_token_data(self, user):
        user_data = self.users.get_user_data(user)
        token_datetime = user_data.get('token_datetime', None)
        verify_token = user_data.get('token', None)
        return verify_token, token_datetime

    def is_authorized(self, user, verify_token):
        if self.is_user_exist(user):
            user_token, user_datetime = self.get_token_data(user)
            if user_token == verify_token:
                dt = datetime.now()
                if dt - user_datetime > timedelta(hours=CLIENT_AUTH_TIMEOUT):
                    return 'timeout'
                self.update_token(user, verify_token, dt)
                return True
            return 'invalid token'
        return 'user not exist'

    def create_user(self, user):
        if self.is_user_exist(user):
            user_token, user_datetime = self.get_token_data(user)
            dt = datetime.now()
            if dt - user_datetime > timedelta(hours=CLIENT_AUTH_TIMEOUT):
                new_token = self.users.create_token()
                self.update_token(user, new_token, dt)
                return new_token
            return None
        new_token = self.users.insert_user(user)
        return new_token

    def update_token(self, user, token, token_datetime):
        result = self.users.update_user(user, token, token_datetime)
        return result
