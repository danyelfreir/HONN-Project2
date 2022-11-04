
class EmailSettings:
    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password

    def username(self):
        return self._username
    
    def password(self):
        return self._password