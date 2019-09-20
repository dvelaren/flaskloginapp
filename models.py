from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,email,password):
        self.email = email
        self.password = password
    @property
    def id(self):
        return self.email
    def __repr__(self):
         return f"User('{self.email}')"