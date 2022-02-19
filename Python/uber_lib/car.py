class Car:
    def __init__(self, id: int, license: str, driver: str, passengers: int) -> None:
        self.id         = id
        self.license    = license
        self.driver     = driver
        self.passengers = passengers
    
    
class UberX(Car):
    def __init__(self, id: int, license: str, driver: str, passengers: int) -> None:
        super().__init__(id, license, driver, passengers)

class UberPool(Car):
    def __init__(self, id: int, license: str, driver: str, passengers: int) -> None:
        super().__init__(id, license, driver, passengers)

class UberBlack(Car):
    def __init__(self, id: int, license: str, driver: str, passengers: int, typeCarAccepted: list, seatsMaterials: list) -> None:
        super().__init__(id, license, driver, passengers)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterials  = seatsMaterials

class UberVan(UberBlack):
    def __init__(self, id: int, license: str, driver: str, passengers: int, typeCarAccepted: list, seatsMaterials: list) -> None:
        super().__init__(id, license, driver, passengers, typeCarAccepted, seatsMaterials)
