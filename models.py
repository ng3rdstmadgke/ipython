import random

class User(object):
    def __init__(self, name, gender='m'):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def vote(self, *seq):
        return random.choice(seq)

    @classmethod
    def class_method(cls):
        return 'class method'

    @staticmethod
    def static_method():
        return 'static method'

