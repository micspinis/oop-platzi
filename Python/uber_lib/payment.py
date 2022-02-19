class Payment:
    def __init__(self, id: int) -> None:
        self.id = id
        
        
        
class Card(Payment):
    def __init__(self, id: int, number: int, cvv: int, date: str) -> None:
        super().__init__(id)
        self.number = number
        self.cvv    = cvv
        self.date   = date

class Cash(Payment):
    pass

class Paypal(Payment):
    def __init__(self, id: int, email: str) -> None:
        super().__init__(id)
        self.email = email