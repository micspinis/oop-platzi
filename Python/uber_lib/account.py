class Account:
    def __init__(self, id: int, name: str, document: str, email: str, password: str) -> None:
        self.id       = id
        self.name     = name
        self.document = document
        self.email    = email
        self.password = password
        
class User(Account):
    def __init__(self, id: int, name: str, document: str, email: str, password: str) -> None:
        super().__init__(id, name, document, email, password)

class Driver(Account):
    def __init__(self, id: int, name: str, document: str, email: str, password: str) -> None:
        super().__init__(id, name, document, email, password)