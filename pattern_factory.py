from abc import ABC, abstractmethod 

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
            pass

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (US Spec)")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (US Spec)")

us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Fusion")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Yamaha", "YZF-R1")
vehicle2.start_engine()


