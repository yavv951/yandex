import random
from faker import Faker


fake = Faker()


class YandexData:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        return YandexData(login, password)
