import json

class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class User(JSONMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.to_json())